from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .models import Borrowing
from .serializers import BorrowingSerializer
# Create your views here.
from django.http import HttpResponse




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class BorrowingList(APIView):
    def get(self, request):
        queryset = Borrowing.objects.all()
        serializer = BorrowingSerializer(queryset, many=True)
        return Response(serializer.data)

class BorrowingGet(APIView):
    def get(self, request, borrowing_id):
        queryset = Borrowing.objects.filter(id=borrowing_id)
        serializer = BorrowingSerializer(queryset, many=True)
        return Response(serializer.data)

class BorrowingCreate(CreateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

class BorrowingUpdate(UpdateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

class BorrowingDelete(DestroyAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer