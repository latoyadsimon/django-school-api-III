from django.db import models
from django.core import validators as v

# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, 
        null = False, 
        blank = False,
        validators=[
            v.RegexValidator(
                regex=r"^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$",
                message='Name must be in the format "First Middle Initial. Last"'
            )
        ]
    )
    student_email = models.EmailField(
        null = False, 
        blank = False, 
        unique=True,
        validators=[
            v.RegexValidator(
                regex=r"^[A-Za-z0-9._%+-]+@school.com$",
                message='Invalid school email format. Please use an email ending with "@school.com".'
            )
        ]     
    )
    personal_email = models.EmailField(
        null = False, 
        blank = False, 
        unique=True
    )
    locker_number = models.IntegerField(
        default = 110, 
        null = False, 
        blank = False, 
        unique=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)]
    
    )
                
    
    locker_combination = models.CharField(
        default="12-12-12",
        null = False, 
        blank = False,
        max_length=255,
        validators=[
            v.RegexValidator(
                regex=r"^[0-9]{2}-[0-9]{2}-[0-9]{2}$",
                message='Combination must be in the format "12-12-12"'
            )
        ]
        
    )
    good_student = models.BooleanField(default=True)