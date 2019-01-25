from rest_framework import viewsets

from .models import *

from .serializers import *

from .permissions import *

class ParagraphViewset(viewsets.ModelViewSet):

    queryset = Paragraph.objects.all()

    serializer_class = ParagraphSerializer

    permission_classes = (madlibsPermission,)


class QuestionViewset(viewsets.ModelViewSet):

    queryset = Question.objects.all()

    serializer_class = QuestionSerializer

    permission_classes = (madlibsPermission,)


class ParagraphQuestionViewset(viewsets.ModelViewSet):

    queryset = ParagraphQuestion.objects.all()

    serializer_class = ParagraphQuestionSerializer

    permission_classes = (madlibsPermission,)

