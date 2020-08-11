from django.db import models

# Create your models here.


class MlModel(models.Model):
    model_name = models.CharField(max_length=100, verbose_name="Modelin Adı")
    heroku_url = models.CharField(
        max_length=100, verbose_name="Modelin URL' si")
    model_description = models.TextField(verbose_name="Modelin Açıklması")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Eklenme Tarihi")
    isPublished = models.BooleanField(
        default=True, verbose_name="Yayınlansın Mı ?")

    def __str__(self):
        return self.model_name
