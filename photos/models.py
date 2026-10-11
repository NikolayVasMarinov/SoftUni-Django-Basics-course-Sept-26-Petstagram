from django.core.validators import MinLengthValidator

from photos.validators import validate_file_size
from django.db import models

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(validators=[validate_file_size])
    description = models.CharField(max_length=300, validators=[MinLengthValidator(10)], blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField('pets.Pet', blank=True)

    date_of_publication = models.DateField(auto_now_add=True, editable=False)

