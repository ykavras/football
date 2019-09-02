from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
import base64
from django.core.files.base import ContentFile

from .forms import ApplicationForm


class ApplyView(View):
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        # image = request.POST['imagebase64']
        # print(image)
        # format, imgstr = image.split(';base64,')
        # ext = format.split('/')[-1]

        # image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        # form['id_image'] = image
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
        else:
            messages.error(request, 'Formdaki zorunlu alanların tümünü doldurduğunuza ve girilen '
                                    'tüm bilgilerin doğru girildiğine emin olun!')

            messages.error(request, form.non_field_errors())
            for error in form.errors:
                if error != '__all__':
                    try:
                        messages.error(request, form.fields[error].errors)
                    except:
                        pass
        print(form)
        print(form.errors)
        return HttpResponseRedirect('/')

    def get(self, request, *args, **kwargs):
        payload = {
            'title': 'Başvuru Formu',
            'body_id': 'form'
        }
        return render(request, 'apply.html', payload)
