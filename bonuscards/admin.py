from django.contrib import admin

from .models import BonusCard, Purchase


@admin.register(BonusCard)
class BonusCardAdmin(admin.ModelAdmin):

    list_display = ('card_series', 'card_number', 'release_date',
                    'expire_date', 'last_active_date', 'total_purchases',
                    'status',)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):

    list_display = ('card', 'item', 'total_price',)
