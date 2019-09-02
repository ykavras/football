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
            instance = form.save(commit=False)
            if form.reference_code_id:
                instance.reference_code_id = form.reference_code_id
                instance.save()

                reference_instance = instance.reference_code
                reference_instance.is_used = True
                reference_instance.save()

            messages.success(request, 'Kaydınız başarıyla alındı. Sonuçlar kesinleştiğinde bizimle paylaştığınız '
                                      'iletişim kanallarından biri ile sizi bilgilendireceğiz.')
            process_status = True
        else:
            if form.errors:
                messages.error(request, form.non_field_errors())
                for error in form.errors:
                    if error != '__all__':
                        try:
                            messages.error(request, form.fields[error].errors)
                        except:
                            pass
            else:
                messages.error(request, 'Formdaki zorunlu alanların tümünü doldurduğunuza ve girilen '
                                        'tüm bilgilerin doğru olduğuna emin olun!')
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
