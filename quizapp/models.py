from django.db import models

# Create your models here.
# Databse layer

class Question(models.Model):
    content = models.CharField(blank=False, max_length=200, help_text="Enter teh Question")

    def __str__(self):
        return  self.content


class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False, blank=False)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content