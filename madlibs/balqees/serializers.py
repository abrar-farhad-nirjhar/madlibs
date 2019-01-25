from rest_framework import serializers
from .models import *



class ParagraphSerializer(serializers.ModelSerializer):

    paragraph_question = serializers.SerializerMethodField()

    def get_paragraph_question(self, obj):
        l =[]

        for pq in obj.paragraph_question.all():
            l.append(QuestionSerializer(instance=pq.question).data)
        return l

    class Meta:
        fields = ('id', 'title', 'paragraph', 'paragraph_question')
        model = Paragraph



 


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','question')
        model = Question


class ParagraphQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'paragraph', 'question')
        model = ParagraphQuestion