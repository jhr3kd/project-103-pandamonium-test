from django.db import models

class Profile(models.Model):
    registration_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/images/profile_pictures/')
    year_choices = [('1','1st Year'), ('2','2nd Year'),('3','3rd Year'),('4','4th Year'),('Grad', 'Graduate Student'),('Alumni','Alumni')]
    year = models.CharField(choices=year_choices)
    bio = models.TextField(max_length=500)
