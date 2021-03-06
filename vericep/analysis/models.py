from django.db import models


# Create your models here.

class Analysis(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name='Kullanıcı')
    date = models.DateTimeField(
        auto_now_add=True, verbose_name="Analiz Tarihi")

    class Meta():
        verbose_name = 'Analizler'
        verbose_name_plural = 'Analizler'
