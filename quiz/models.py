from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30)


class Quizzes(models.Model):
    category =models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

class Questions(models.Model):
    pass
class Answer(models.Model):
    answer_text = models.CharField(max_length=150)
