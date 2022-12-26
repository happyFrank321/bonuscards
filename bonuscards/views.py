from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView

from .forms import CardStatusForm, CreateMULTCardForm
from .models import BonusCard, Purchase
from .filters import CardFilter


class CardsView(ListView):

    model = BonusCard
    context_object_name = 'bonuscards'
    template_name = 'main_page_with_filters_and_stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_cards = CardFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = filtered_cards.form
        context['filter_items_count'] = filtered_cards.qs.count()
        paginator = Paginator(filtered_cards.qs, 50)
        page = self.request.GET.get('page')
        try:
            context['filter_qs'] = paginator.page(page)
        except PageNotAnInteger:
            context['filter_qs'] = paginator.page(1)
        except EmptyPage:
            context['filter_qs'] = paginator.page(paginator.num_pages)
        context['total_cards'] = BonusCard.objects.all().count
        context['active_cards'] = BonusCard.objects.filter(status='ACTIVE').count()
        context['deactive_cards'] = BonusCard.objects.filter(status='DEACTIVE').count()
        context['not_active_cards'] = BonusCard.objects.filter(status='NOT ACTIVE').count()
        return context


# def show_card(request, card_series, card_number):
#     card = get_object_or_404(BonusCard, card_series=card_series, card_number=card_number)
#     form = CardStatusForm(request.POST or None)
#     if request.method == 'POST':
#         form = CardStatusForm(request.POST or None)
#         if form.is_valid():
#             card.status = form.cleaned_data['status']
#             card.save()
#
#     context = {
#         'card': card,
#         'form': form,
#     }
#
#     return render(request, '../templates2/../templates/single_card_view_and_change_status.html', context=context)


def show_card2(request, card_series):
    cards = BonusCard.objects.filter(card_series=card_series)
    if cards:
        context = {
            'cards': cards,
        }
    else:
        raise Http404("There are no cards with this series")

    return render(request, '../templates2/view2.html', context=context)


def create_mult_cards(request):
    form = CreateMULTCardForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            card_series = str(form.cleaned_data['card_series']).zfill(4)
            expire_in = form.cleaned_data['expires_in']
            amount = form.cleaned_data['amount']
            cards = BonusCard.objects.filter(card_series=card_series)
            if cards:
                max_number = int(
                    cards.filter(card_series=card_series).values_list('card_number').order_by('card_number').last()[0]
                ) + 1
            else:
                max_number = 0
            list_cards = [BonusCard(
                card_series=card_series,
                card_number=str(max_number + i).zfill(12),
                expire_date=(datetime.now(timezone.utc) + relativedelta(months=+int(expire_in)))
            ) for i in range(amount)]
            BonusCard.objects.bulk_create(list_cards)
            return HttpResponseRedirect(reverse_lazy('index'))
    return render(request, 'create_mult_cards_form.html', {'form': form})


class CardUpdateView(UpdateView):
    model = BonusCard
    fields = ['status']
    template_name = 'single_card_view_and_change_status.html'
    context_object_name = 'bonuscard'

    def get_object(self, queryset=None):
        obj = self.model.objects.get(card_series=self.kwargs['card_series'], card_number=self.kwargs['card_number'])
        return obj

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_purchase'] = Purchase.objects.filter(card=context['bonuscard'])
        return context


class CardsListView(ListView):
    model = BonusCard
    template_name = ''



