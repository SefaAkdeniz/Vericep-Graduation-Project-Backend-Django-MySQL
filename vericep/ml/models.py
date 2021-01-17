from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('Str', 'String'),
    ('Int', 'İnteger'),
    ('Db', 'Double'),
)


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

    class Meta:
        verbose_name = 'Machine Learning Model'
        verbose_name_plural = 'Machine Learning Model'


class ModelInput(models.Model):
    model_id = models.ForeignKey(
        MlModel, on_delete=models.CASCADE, verbose_name="ML Modeli")
    input_name = models.CharField(max_length=100, verbose_name="Değişken Adı")
    parameter_name = models.CharField(max_length=100, verbose_name="Parametre Adı")
    typed = models.CharField(
        max_length=20, choices=TYPE_CHOICES, verbose_name="Değişken Tipi")
    description = models.CharField(max_length=50,verbose_name="Değişken Açıklaması")

    def __str__(self):
        return self.input_name

    class Meta:
        verbose_name = 'Model Değişkenleri'
        verbose_name_plural = 'Model Değişkenleri'
