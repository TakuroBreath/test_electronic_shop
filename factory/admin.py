from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import NetworkNode, Product


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'supplier_link')
    list_filter = ('city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>',
                               reverse('admin:network_networknode_change', args=[obj.supplier.id]), obj.supplier.name)
        else:
            return '-'

    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f'{updated_count} objects debt cleared successfully.')

    clear_debt.short_description = "Clear debt for selected objects"


admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(Product)
