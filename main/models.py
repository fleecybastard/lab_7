from django.db import models
from django.db.models import Sum


class AirLine(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def total_capacity(self):
        capacity = self.aircrafts.aggregate(Sum('capacity'))
        capacity = capacity.get('capacity__sum')
        if capacity is None:
            capacity = 0
        return capacity

    @property
    def total_payload(self):
        payload = self.aircrafts.aggregate(Sum('payload'))
        payload = payload.get('payload__sum')
        if payload is None:
            payload = 0
        return payload


class AirCraft(models.Model):
    class AirCraftModel(models.TextChoices):
        AN158 = 'AN158'
        Boeing747 = 'Boeing747'
        DouglasDC3 = 'DouglasDC3'
        AirbusA380 = 'AirbusA380'
        Boeing777X = 'Boeing777X'

    airline = models.ForeignKey(AirLine, on_delete=models.CASCADE, related_name='aircrafts')
    model = models.CharField(max_length=12, choices=AirCraftModel.choices, default=AirCraftModel.AN158)
    capacity = models.IntegerField()
    payload = models.IntegerField()
    flight_distance = models.IntegerField()
    fuel_per_hour = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-flight_distance']

    def __str__(self):
        return f'{self.model} id: {self.id}'

