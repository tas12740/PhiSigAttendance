from django.db import models


class ConsSubmission(models.Model):
    onyen = models.CharField(max_length=20, verbose_name='Onyen')
    created = models.DateTimeField(auto_now_add=True)


class Box(models.Model):
    submission = models.CharField(max_length=1000, verbose_name='Submission')

    def __str__(self):
        return f'{self.submission}'
