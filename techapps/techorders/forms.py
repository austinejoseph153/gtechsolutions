from django import forms
from .models import Contact, Testimonials

class ContactForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    message = forms.TextInput()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def save(self):
        pass
        # data = self.cleaned_data
        # contact = Contact(
            
        # )
        # contact.save()

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        exclude = ['date']