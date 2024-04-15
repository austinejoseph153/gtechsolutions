from .models import Testimonials
from .forms import TestimonialsForm
from django.http import JsonResponse
import datetime

def get_reviews(request):
    if request.method == "POST":
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            return JsonResponse({"response": "success","reviews":""}, status=200)
        else:
            print(form.errors)
            return JsonResponse({"response": "error"}, status=400)        
    else:
        return JsonResponse({"response": "error"}, status=405)
