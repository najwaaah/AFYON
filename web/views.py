from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from web.forms import ContactForm
import json
from .models import Services, Rating, Products


class IndexView(TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Services.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'web/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating'] = Rating.objects.all()
        context['is_about'] = True
        return context


class ServicesView(TemplateView):
    template_name = 'web/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Services.objects.all()
        context['is_services'] = True
        return context


class ContactView(View):
    template_name = 'web/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'is_contact': True, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type="application/javascript")


# URL configuration example:
# path('', IndexView.as_view(), name='index')
# path('about/', AboutView.as_view(), name='about')
# path('services/', ServicesView.as_view(), name='services')
# path('contact/', ContactView.as_view(), name='contact')
