from django.contrib import admin
from .models import Advertisement



class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'auction', 'created_dare']
    list_filter=['auction', 'create_at']
    actions = ['make_auction_as_false', 'make_auction_as_True']
    fieldsets=(
        ('Общее', {'fields': ('title', 'description')}),
        ('Финансы',{'fields': ('price', 'auction'), 'classes': ['collapse']})
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_True(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)