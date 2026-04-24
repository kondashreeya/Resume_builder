from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    career_objective = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    projects = models.TextField()
    internships = models.TextField()
    certifications = models.TextField()
    interpersonal_skills = models.TextField()

    def __str__(self):
        return self.name