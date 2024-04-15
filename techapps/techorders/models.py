from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _

def upload_to(instance,filename):
    return 'image/{filename}'.format(filename=filename)

# Create your models here.
class Orders(models.Model):
    pass

class ProjectUpload(models.Model):
    file_name = models.CharField(max_length=50)
    img_url = models.ImageField(upload_to=upload_to)


class Testimonials(models.Model):
    firstname = models.CharField(max_length=50, verbose_name=_('Firstname'), null=True)
    lastname = models.CharField(max_length=50, verbose_name=_('Lastname'), null=True)
    email = models.EmailField(verbose_name=_('senders email'))
    message = models.TextField(max_length=500)
    positive = models.BooleanField(default=False, verbose_name=_(''))
    date = models.DateTimeField(verbose_name=_("date posted"), default=datetime.datetime.now)

    def __str__(self):
        return "%s - %s" %(self.lastname,self.firstname)
    
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-date']

    # def save(self,*args,**kwargs):
    #     return super(Comments).save(*args,**kwargs)
        
class Contact(models.Model):
    firstname = models.CharField(max_length=50, verbose_name = _("Firstname"))
    lastname = models.CharField(max_length=50, verbose_name = _("Lastname"))
    phone = models.CharField(max_length=50, verbose_name = _("Phone no"))
    email = models.EmailField(max_length=50, verbose_name = _("Email"))
    message = models.TextField(verbose_name = _("message"))
    date = models.DateField(auto_now_add = True, verbose_name = _("date sent"))

    def __str__(self):
        return "%s - %s" %(self.lastname,self.firstname)
    
    class Meta:
        ordering = ['-date']
