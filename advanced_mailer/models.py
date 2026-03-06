from django.db import models

class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message_html = models.TextField(help_text="HTML content for the email body")

    def __str__(self):
        return self.name

class SentEmail(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]
    to_email = models.CharField(max_length=500)
    cc_emails = models.CharField(max_length=500, blank=True, default='')
    bcc_emails = models.CharField(max_length=500, blank=True, default='')
    subject = models.CharField(max_length=200)
    message_html = models.TextField()
    attachment_name = models.CharField(max_length=255, blank=True, default='')
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SUCCESS')

    def __str__(self):
        return f"To: {self.to_email} | {self.subject} | {self.status}"

    class Meta:
        ordering = ['-date_sent']
