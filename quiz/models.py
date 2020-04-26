from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length = 264, blank=True)

    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    option = models.CharField(max_length=264, blank=True)


    def __str__(self):
        return self.option

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.answer
