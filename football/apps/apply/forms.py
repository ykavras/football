from django import forms

from .models import Application, ReferenceCode


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'last_name', 'email', 'phone', 'city', 'address', 'id_photo')

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        reference_code = request['reference_code_string']
        if reference_code:
            try:
                reference_instance = ReferenceCode.objects.get(code=reference_code)  # check it! is it exist or not

                if reference_instance.is_used:
                    self.add_error('__all__', 'Referans kodunuz daha önceden kullanılmış. Tekrar kullanamazsınız!')
                else:
                    self.reference_code_id = reference_instance.id
            except ReferenceCode.DoesNotExist:
                self.add_error('__all__',
                               'Referans Kodunuz Eşleşmedi. Lütfen kontrol edin eğer referans kodunuz yoksa alanı boş bırakınız')
        else:
            self.reference_code_id = None
