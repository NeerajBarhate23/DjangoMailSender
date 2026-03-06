from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm
from django.contrib import messages

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            try:
                # Send the email using the configured SMTP settings
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,  # From email
                    [recipient],             # To email list
                    fail_silently=False,
                )
                # Redirect to the success page (PRG pattern)
                return redirect('success')
            except Exception as e:
                # If something goes wrong, show an error message
                messages.error(request, f'Failed to send email: {e}')
    else:
        # If it is a GET request, just show the empty form
        form = EmailForm()

    return render(request, 'mailer/form.html', {'form': form})

def success_view(request):
    # This is the 'Get' part of PRG
    return render(request, 'mailer/success.html')
