from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class Sibling(models.Model):
    HOUSE_CHOICES = [
        ('Rollawood', 'Rollawood'),
        ('Torchia', 'Torchia'),
        ('Harryhill', 'Harryhill'),
        ('', '')
    ]

    INACTIVITY_CHOICES = [
        ('Active', 'Active')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    onyen = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    house = models.CharField(
        max_length=10, choices=HOUSE_CHOICES, null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=INACTIVITY_CHOICES, null=True, blank=True)
    big = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    big_alumni = models.ForeignKey(
        'Alumni', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.onyen})'


class GPATracker(models.Model):
    sibling = models.OneToOneField(
        'Sibling', unique=True, on_delete=models.CASCADE)
    gpa = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sibling.first_name} {self.sibling.last_name} - {self.gpa} - {self.last_updated}'


class Alumni(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'


class Event(models.Model):
    name = models.CharField(max_length=20)
    unique_id = models.CharField(max_length=4, validators=[
                                 MinLengthValidator(4)])
    description = models.CharField(max_length=100, blank=True)
    event_type = models.ForeignKey('EventType', on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.name} ({self.unique_id}) - {self.event_type} - {self.date_time}'


class EventType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class CheckIn(models.Model):
    sibling = models.ForeignKey('Sibling', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sibling.first_name} {self.sibling.last_name} - {self.event.name} - {self.date_time}'
