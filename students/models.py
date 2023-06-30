from django.db import models

COHORT_SUBJECTS = [
    ('SEI', 'Software Engineering Immersive'),
    ('UXDI', 'User Experience Development Immersive'),
    ('DSI', 'Data Science Immersive'),
]

# Create your models here.
class Cohort(models.Model):
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=5, choices=COHORT_SUBJECTS)

class Student(models.Model):
    name = models.CharField(max_length=128)
    cohort = models.ForeignKey(
        Cohort,
        on_delete=models.CASCADE,
        related_name='students'
    )
    
def __str__(self):
    return f'{self.subject} - {self.name}'