from django.db import models

class Question(models.Model):

    """
    questions and their options , only one option is currect and it 
    will be in "currect_option" column.
    """
    question_text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

