from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ApplicationForm


class ApplyView(View):
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            if form.reference_code_id:
                instance.reference_code_id = form.reference_code_id
                instance.save()

                reference_instance = instance.reference_code
                reference_instance.is_used = True
                reference_instance.save()

            process_status = True
        else:
            messages.error(request, form.non_field_errors())
            messages.error(request, form.errors)
            process_status = False

        payload = {
            'title': 'Başvuru Formu',
            'body_id': 'form',
            'process_status': process_status,
        }
        return render(request, 'apply.html', payload)

    def get(self, request, *args, **kwargs):
        payload = {
            'title': 'Başvuru Formu',
            'body_id': 'form'
        }
        return render(request, 'apply.html', payload)
