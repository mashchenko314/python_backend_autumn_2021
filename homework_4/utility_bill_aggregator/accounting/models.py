from django.db import models

class Service(models.Model):
    type = models.CharField(max_length=64, verbose_name='Тип')
    organization = models.CharField(max_length=64, verbose_name='Организация')
    address = models.TextField(verbose_name='Адрес организации', null=True, blank=True)
    
    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class Account(models.Model):
    MONTHS = [
        ('January', 'Январь'),
        ('February', 'Февраль'),
        ('March', 'Март'),
        ('April', 'Апрель'),
        ('May', 'Май'),
        ('June', 'Июнь'),
        ('July', 'Июль'),
        ('August', 'Август'),
        ('September', 'Сентябрь'),
        ('October', 'Октябрь'),
        ('November', 'Ноябрь'),
        ('December', 'Декабрь')
    ]
    personal_account = models.CharField(max_length=15, verbose_name='Лицевой счет')
    month =  models.CharField(max_length=10, verbose_name='Месяц', choices=MONTHS)
    year = models.CharField(max_length=4, verbose_name='Год')
    payment_amount = models.FloatField(verbose_name='Сумма платежа')
    indications = models.TextField(verbose_name='Показания счетчиков', null=True)
    electronic_receipt_filename = models.TextField(verbose_name='Название файла с электронной квитанцией', null=True)
    address = models.TextField(verbose_name='Адрес квартиры', null=True) 
    is_paid = models.BooleanField(verbose_name='Оплачено', default=False)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Тип услуги')

    def __str__(self):
        return self.personal_account

    class Meta:
        ordering = ['-year']
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'



