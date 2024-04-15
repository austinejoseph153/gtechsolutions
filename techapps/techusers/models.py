from django.db import models
from django.core.cache import cache


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



# creating models for email queue

class EmailQueue(TimeStampedModel):

    subject = models.CharField(max_length=255, help_text=('max 255 chars'))
    from_email = models.EmailField(verbose_name =("email"))
    recipients = models.TextField(verbose_name=("recivers email"))
    reply_to = models.EmailField()
    message = models.TextField()
    template = models.IntegerField()
    sent_timestamp = models.DateTimeField(null=True)
    attachment1 = models.TextField(blank=True)
