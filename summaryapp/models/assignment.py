from tkinter import SE
from django.db import models
from django.contrib.auth.models import User
from summaryapp.models import ServiceModel

class AssingmentModel(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ManyToManyField(ServiceModel, related_name='service')
    created_at = models.DateTimeField(auto_now_add=True)
    tip = models.DecimalField(max_digits = 4, decimal_places = 2)

    class Meta:
        db_table = 'assignment'
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return "Assignement"