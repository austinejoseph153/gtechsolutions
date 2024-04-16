from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from techapps.techorders.models import Contact, Testimonials
from techapps.techorders.forms import ContactForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from .utils import fetch_testimonies_from_files

class HomeTemplateView(TemplateView):
    """
    Pagina de quienes somos
    """
    template_name = "techpages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        testimonies = Testimonials.objects.filter(positive=True).order_by("-id")[:5]
        if not testimonies:
            testimonies = fetch_testimonies_from_files()
        context["testimonies"] = testimonies
        return context

class AboutTemplateView(TemplateView):
    """
    Pagina de quienes somos
    """
    template_name = "techpages/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        testimonies = Testimonials.objects.filter(positive=True).order_by("-id")[:5]
        if not testimonies:
            testimonies = fetch_testimonies_from_files()
        context["testimonies"] = testimonies
        return context

class ContactTemplateView(FormMixin,TemplateView):
    """
    Pagina de quienes somos
    """
    template_name = "techpages/contact.html"
    model = Contact
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactTemplateView, self).get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse('techpages:contact')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, _('Thank you for contacting us. your message will be reviewed and you will receive a response shortly'))
            return self.form_valid(form)
        else:
            messages.error(request, _('Error procesing your message'))
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ContactTemplateView, self).form_valid(form)
