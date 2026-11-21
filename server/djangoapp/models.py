from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Many-to-one: one car make can have many car models
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Refers to a dealer id in the Mongo database
    dealer_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2026), MinValueValidator(2015)]
    )

    def __str__(self):
        return self.car_make.name + " " + self.name