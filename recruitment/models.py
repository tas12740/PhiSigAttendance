from django.db import models

# Create your models here.


class PNM(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    onyen = models.CharField(max_length=20, unique=True, verbose_name='Onyen')
    email = models.EmailField(verbose_name='Email')

    open_one = models.BooleanField(
        verbose_name='Open Recruitment One', null=True, blank=True)
    open_two = models.BooleanField(
        verbose_name='Open Recruitment Two', null=True, blank=True)
    open_three = models.BooleanField(
        verbose_name='Open Recruitment Three', null=True, blank=True)
    open_friday = models.BooleanField(
        verbose_name='Open Recruitment Friday', null=True, blank=True)

    closed_one = models.BooleanField(
        verbose_name='Closed Recruitment One', null=True, blank=True)
    closed_two = models.BooleanField(
        verbose_name='Closed Recruitment Two', null=True, blank=True)
    closed_three = models.BooleanField(
        verbose_name='Closed Recruitment Three', null=True, blank=True)
    potluck = models.BooleanField(
        verbose_name='Potluck', null=True, blank=True)

    fact_sheet = models.BooleanField(
        verbose_name='Fact Sheet', null=True, blank=True)
    ipanel_number = models.IntegerField(
        verbose_name='IPanel Order Number', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.onyen})'
