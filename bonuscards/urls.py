from django.urls import path
from . import views
urlpatterns = [
    path('', views.CardsView.as_view(), name='index'),
    path('view/<card_series>/<card_number>', views.CardUpdateView.as_view(), name='card_detail'),
    path('view/<card_series>', views.show_card2, name='series_detail'),
    path('cretecards/', views.create_mult_cards, name='create_mult_cards'),

]