from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import Userfrom

from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


#Serializeri olusturdduk simdi views i yaziyoruz

class RegisterAPI(CreateAPIView):
    queryset =User.objects.all()
    serializer_class =RegisterSerializer

# Create your views here.
