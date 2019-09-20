from django.db import models

# Create your models here.


class IPanelAuth(models.Model):
    onyen = models.CharField(max_length=20, unique=True, verbose_name='Onyen')
    passcode = models.CharField(
        max_length=20, unique=True, verbose_name='Passcode')

    def __str__(self):
        return f'{self.onyen}: {self.passcode}'


class Vote(models.Model):
    YES = 'Y'
    NO = 'N'
    ABSTAIN = 'A'
    VOTE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
        (ABSTAIN, 'Abstain')
    ]

    vote_onyen = models.ForeignKey(
        'IPanelAuth', on_delete=models.CASCADE, verbose_name='Vote Onyen')
    pnm_number = models.IntegerField(verbose_name='PNM Number')
    vote = models.CharField(
        max_length=10, choices=VOTE_CHOICES, default=ABSTAIN)

    def __str__(self):
        return f'{self.pnm_number} : {self.vote}'


class PNMIPanel(models.Model):
    LOCKED = 'L'
    OPEN = 'O'
    STATUS_CHOICES = [
        (LOCKED, 'Locked'),
        (OPEN, 'Open')
    ]

    number = models.IntegerField(verbose_name='Number', unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Status')
    # TODO future: make this link to PNM or a name to easily tell who made it

    def __str__(self):
        return f'{self.number}: {self.status}'