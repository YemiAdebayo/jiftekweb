from django.contrib import admin
from .models import GetAQuote
from .forms import QuoteFormForAdmin

class QuoteAdminInterface(admin.ModelAdmin):

    form = QuoteFormForAdmin
    list_display = ('name', 'phone_number', 'project_type', 'id','timestamp',
                    'quote_is_processed',)
    list_filter = ('quote_is_processed',)

    fieldsets = (

        ('Bio Data', {
         'fields': ('name',)}),
        ('Contact Info', {
         'fields': ('phone_number', 'email',)}),
         ('Study Interest', {
         'fields': ('project_type',)}),
        ('Status', {
         'fields': ('quote_is_processed',)}),
    )

    add_fieldsets = (

        ('Bio Data', {
         'fields': ('name',)}),
        ('Contact Info', {
         'fields': ('phone_number', 'email',)}),
         ('Study Interest', {
         'fields': ('project_type',)}),
        ('Status', {
         'fields': ('quote_is_processed',)}),
    )

    search_fields = ('name','phone_number','email', 'id')

    ordering = ('-timestamp',)
    filter_horizontal = ()

admin.site.register(GetAQuote, QuoteAdminInterface)
