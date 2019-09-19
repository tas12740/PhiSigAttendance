from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class Sibling(models.Model):
    HOUSE_CHOICES = [
        ('Rollawood', 'Rollawood'),
        ('Torchia', 'Torchia'),
        ('Harryhill', 'Harryhill'),
        ('Bigelow', 'Bigelow'),
        ('No House', 'No House')
    ]

    INACTIVITY_CHOICES = [
        ('Active', 'Active')
    ]

    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    onyen = models.CharField(max_length=20, unique=True, verbose_name='Onyen')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Phone Number')
    preferred_contact = models.CharField(
        max_length=10, choices=[('Text', 'Text'), ('Email', 'Email')], null=True, blank=True)
    pronouns = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Pronouns')
    house = models.CharField(
        max_length=10, choices=HOUSE_CHOICES, null=True, blank=True, verbose_name='House')
    status = models.CharField(
        max_length=20, choices=INACTIVITY_CHOICES, null=True, blank=True, verbose_name='Status')
    pledge_class = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Pledge Class')
    big = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Big (Currently Active)')
    big_alumni = models.ForeignKey(
        'Alumni', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Big (Alumni)')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.onyen})'


class GPATracker(models.Model):
    sibling = models.OneToOneField(
        'Sibling', unique=True, on_delete=models.CASCADE, verbose_name='Sibling')
    gpa = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name='GPA')
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return f'{self.sibling.first_name} {self.sibling.last_name} - {self.gpa} - {self.last_updated}'


class Alumni(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'


class Event(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    unique_id = models.CharField(max_length=4, unique=True, validators=[
                                 MinLengthValidator(4)], verbose_name='Event Code')
    description = models.CharField(
        max_length=100, blank=True, verbose_name='Description')
    event_type = models.ForeignKey(
        'EventType', on_delete=models.CASCADE, verbose_name='Event Type')
    date_time = models.DateTimeField(verbose_name='Date and Time')

    def __str__(self):
        return f'{self.name} ({self.unique_id}) - {self.event_type} - {self.date_time}'


class EventType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')

    def __str__(self):
        return f'{self.name}'


class CheckIn(models.Model):
    sibling = models.ForeignKey(
        'Sibling', on_delete=models.CASCADE, verbose_name='Sibling')
    event = models.ForeignKey(
        'Event', on_delete=models.CASCADE, verbose_name='Event')
    date_time = models.DateTimeField(
        auto_now_add=True, verbose_name='Date and Time')

    def __str__(self):
        return f'{self.sibling.first_name} {self.sibling.last_name} - {self.event.name} - {self.date_time}'
