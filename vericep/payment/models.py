from django.db import models

# Create your models here.

MONTH_CHOICES = (
    ("1", '01'),
    ("2", '02'),
    ("3", '03'),
    ("4", '04'),
    ("5", '05'),
    ("6", '06'),
    ("7", '07'),
    ("8", '08'),
    ("9", '09'),
    ("10", '10'),
    ("11", '11'),
    ("12", '12'),
)

YEAR_CHOICES = (
    ("20", '20'),
    ("21", '21'),
    ("22", '22'),
    ("23", '23'),
    ("24", '24'),
)


class Balance(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name='Kullanıcı')
    amaount = models.DecimalField(
        decimal_places=2, max_digits=5, verbose_name="Bakiye")

    class Meta():
        verbose_name = 'Bakiyeler'
        verbose_name_plural = 'Bakiyeler'


class CreditCard(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name='Kullanıcı')
    card_name = models.CharField(max_length=100, verbose_name="Kart Adı")
    card_number = models.CharField(max_length=16, verbose_name="Kart Numarası")
    expiration_date_month = models.CharField(
        max_length=2, choices=MONTH_CHOICES, verbose_name="Son Geçerlilik Tarih (Ay)")
    expiration_date_year = models.CharField(
        max_length=2, choices=YEAR_CHOICES, verbose_name="Son Geçerlilik Tarih (Yıl)")
    cvc = models.CharField(max_length=3, verbose_name="CVC")

    def __str__(self):
        return self.card_name

    class Meta():
        verbose_name = 'Kredi Kartları'
        verbose_name_plural = 'Kredi Kartları'


class PastPayments(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Ödeme Tarihi")
    amaount = models.DecimalField(
        decimal_places=2, max_digits=5, verbose_name="Miktar")
    card = models.ForeignKey(
        CreditCard, on_delete=models.CASCADE, verbose_name='Kullanılan Kart')

    class Meta():
        verbose_name = 'Geçmiş Ödemeler'
        verbose_name_plural = 'Geçmiş Ödemeler'
