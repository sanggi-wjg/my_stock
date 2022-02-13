from django.contrib import admin

from stocks.models import Market


@admin.register(Market)
class StocksAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('upper_case_market_name',)

    @admin.display(description = 'Market 명')
    def upper_case_market_name(self, obj):
        # return f"{obj.market_name.upper()}"
        return "%s" % obj.market_name.upper()
