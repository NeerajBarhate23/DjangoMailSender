from django.contrib import admin
from .models import EmailTemplate, SentEmail

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject')

@admin.register(SentEmail)
class SentEmailAdmin(admin.ModelAdmin):
    list_display = ('to_email', 'subject', 'status', 'date_sent')
    list_filter = ('status', 'date_sent')
    search_fields = ('to_email', 'subject')
    readonly_fields = ('to_email', 'cc_emails', 'bcc_emails', 'subject', 'message_html', 'attachment_name', 'date_sent', 'status')
