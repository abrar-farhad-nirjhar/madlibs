from django.db import models

# Create your models here.

class Paragraph(models.Model):
    title = models.CharField(max_length=255,blank=False, null=False)
    paragraph = models.TextField(blank=False, null=False)


    def __str__(self):
        return str(self.title)

class Question(models.Model):
    question = question = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.question)
class ParagraphQuestion(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name="paragraph_question")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="paragraph_question")