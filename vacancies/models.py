from django.db import models


class Company(models.Model):
    # id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE, null=True)
    skills = models.CharField(max_length=64)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField()
