import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

def current_year():
    return datetime.date.today().year

class StudentInfo(models.Model):
    full_name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    contact_number = PhoneNumberField(blank=True, region="BD")

    semester_choices = [
        ('', 'Select Semester'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
        ('spring', 'Spring'),
    ]

    semester = models.CharField(
        max_length = 10,
        choices = semester_choices,
        blank = False,
        null = False,
    )

    year = models.PositiveIntegerField(
        default = current_year,
        validators = [
            MinValueValidator(2015),
            MaxValueValidator(current_year)
        ],
        help_text = "Use the following formate: YYYY"
    )

    is_2nd_installment = models.BooleanField(default=False)
    is_3rd_installment = models.BooleanField(default=False)
    is_add_drop = models.BooleanField(default=False)

    reason_of_late = models.TextField(max_length=300)