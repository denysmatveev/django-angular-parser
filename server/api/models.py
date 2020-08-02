from django.db import models


class DataList(models.Model):

    title = models.CharField(max_length=60,
                             verbose_name='Balance Sheet')

    date_2019 = models.CharField(max_length=60,
                                 verbose_name='12/30/2019')

    date_2018 = models.CharField(max_length=60,
                                 verbose_name='12/30/2018')

    date_2017 = models.CharField(max_length=60,
                                 verbose_name='12/30/2017')

    date_2016 = models.CharField(max_length=60,
                                 verbose_name='12/30/2016')

    class Meta:
        verbose_name = 'Данные компании'
        verbose_name_plural = 'Данные компании'
