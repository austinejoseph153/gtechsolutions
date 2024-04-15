from django.db import models

# Create your models here.
class EmailQueue(models.Model):
    sent = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True,verbose_name="date sent")
    recipient = models.EmailField()
    from_email = models.EmailField(verbose_name="sender")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,verbose_name="phone number")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "email queue"
        verbose_name_plural = "email queues"
        ordering = ["date"]







    
