from django import forms
from .models import EmailTemplate

class EmailForm(forms.Form):
    template = forms.ModelChoiceField(
        queryset=EmailTemplate.objects.all(),
        required=False,
        label='Load Template',
        empty_label='-- Select a template (optional) --',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'template-select',
        })
    )
    to = forms.EmailField(
        label='Recipient Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'recipient@example.com'
        })
    )
    cc = forms.CharField(
        required=False,
        label='CC (comma separated)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'cc1@example.com, cc2@example.com'
        })
    )
    bcc = forms.CharField(
        required=False,
        label='BCC (comma separated)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'bcc1@example.com, bcc2@example.com'
        })
    )
    subject = forms.CharField(
        max_length=200,
        label='Subject',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email subject',
            'id': 'subject-input',
        })
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control tinymce-editor',
            'rows': 8,
            'placeholder': 'Enter your message here...',
            'id': 'message-editor',
        })
    )
    attachment = forms.FileField(
        required=False,
        label='Attachment',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
        })
    )
