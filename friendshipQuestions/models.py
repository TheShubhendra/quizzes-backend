from django.db import models


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    choice_id = models.AutoField(primary_key=True)
    choice = models.CharField(max_length=30)

    def __str__(self):
        return self.choice


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    data = models.JSONField(default=dict)
    def __str__(self):
        return self.name


class Response(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="responses"
        )
    response_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=dict)

    def __str__(self):
        return self.answers
