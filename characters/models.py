from django.db import models


class Characters(models.Model):

    class StatusChoices(models.TextChoices):
        ALIVE = "Alive", "Alive"
        DEAD = "Dead", "Dead"
        UNKNOWN = "Unknown", "Unknown"

    class GenderChoices(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        GENDERLESS = "Genderless", "Genderless"
        UNKNOWN = "Unknown", "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    species = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)
    image = models.URLField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.name
