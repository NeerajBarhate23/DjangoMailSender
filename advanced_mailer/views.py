from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .forms import EmailForm
from .models import SentEmail, EmailTemplate
from django.utils.html import strip_tags

def send_email_view(request):
    templates = EmailTemplate.objects.all()

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipient = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            message_html = form.cleaned_data['message']
            cc_raw = form.cleaned_data.get('cc', '')
            bcc_raw = form.cleaned_data.get('bcc', '')
            attachment = request.FILES.get('attachment')

            # Parse comma-separated CC and BCC into lists
            cc_list = [e.strip() for e in cc_raw.split(',') if e.strip()] if cc_raw else []
            bcc_list = [e.strip() for e in bcc_raw.split(',') if e.strip()] if bcc_raw else []

            # Create a plain text fallback by stripping HTML tags
            plain_text = strip_tags(message_html)

            try:
                # Use EmailMultiAlternatives for HTML + attachments
                email = EmailMultiAlternatives(
                    subject=subject,
                    body=plain_text,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[recipient],
                    cc=cc_list,
                    bcc=bcc_list,
                )
                # Attach the HTML version
                email.attach_alternative(message_html, "text/html")

                # Attach file if provided
                if attachment:
                    email.attach(attachment.name, attachment.read(), attachment.content_type)

                email.send(fail_silently=False)

                # Log to database
                SentEmail.objects.create(
                    to_email=recipient,
                    cc_emails=cc_raw,
                    bcc_emails=bcc_raw,
                    subject=subject,
                    message_html=message_html,
                    attachment_name=attachment.name if attachment else '',
                    status='SUCCESS',
                )

                return redirect('advanced_success')

            except Exception as e:
                # Log the failed attempt
                SentEmail.objects.create(
                    to_email=recipient,
                    cc_emails=cc_raw,
                    bcc_emails=bcc_raw,
                    subject=subject,
                    message_html=message_html,
                    attachment_name=attachment.name if attachment else '',
                    status='FAILED',
                )
                messages.error(request, f'Failed to send email: {e}')
    else:
        form = EmailForm()

    return render(request, 'advanced_mailer/form.html', {
        'form': form,
        'templates': templates,
    })

def success_view(request):
    return render(request, 'advanced_mailer/success.html')

def history_view(request):
    sent_emails = SentEmail.objects.all()
    return render(request, 'advanced_mailer/history.html', {'sent_emails': sent_emails})

def template_data_view(request, pk):
    """API endpoint to get template data for auto-filling the form."""
    try:
        template = EmailTemplate.objects.get(pk=pk)
        return JsonResponse({
            'subject': template.subject,
            'message_html': template.message_html,
        })
    except EmailTemplate.DoesNotExist:
        return JsonResponse({'error': 'Template not found'}, status=404)
