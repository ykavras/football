from django.db import models
from django.core.validators import RegexValidator

from ...utils.file_rename import PathAndRename


class ReferenceCode(models.Model):
    code = models.CharField(verbose_name='Kod', max_length=20, unique=True)
    is_used = models.BooleanField(verbose_name='Kullanılma Durumu')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Referans Kodu'
        verbose_name_plural = 'Referans Kodları'


class Application(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='Telefon numarası "+999999999" formatında olmalı.')
    string_regex = RegexValidator(regex=r'^[a-zA-ZıİğĞüÜçÇöÖşŞ ]{2,25}$',
                                 message='Bu alana yalnızca harf ve boşluk karakteri girebilirsiniz (Max 25 karakter).')
    name = models.CharField(verbose_name='Adı', max_length=20, validators=[string_regex])
    last_name = models.CharField(verbose_name='Soyadı', max_length=20, validators=[string_regex])
    email = models.EmailField(verbose_name='E-mail', unique=True)
    phone = models.CharField(verbose_name='Telefon Numarası', max_length=15, validators=[phone_regex], unique=True)
    city = models.CharField(verbose_name='Şehir', max_length=25, validators=[string_regex])
    address = models.CharField(verbose_name='Adres', max_length=1000)
    reference_code = models.OneToOneField(ReferenceCode, verbose_name='Referans Kodu', related_name='application',
                                          on_delete=models.CASCADE,
                                          null=True,
                                          blank=True)
    id_photo = models.ImageField(verbose_name='Kimlik Fotoğrafı', upload_to=PathAndRename('application/id_photos/'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Başvuru Tarihi')
    confirm = models.BooleanField(verbose_name='Onay', default=False)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def has_reference_code(self):
        return 'Kullanıldı' if self.reference_code else '-'

    has_reference_code.short_description = 'Referans Kodu Var Mı?'

    class Meta:
        verbose_name = 'Başvuru'
        verbose_name_plural = 'Başvurular'


