from django.shortcuts import render
# boridan olish qismi
from .models import Klass, Teacher, Student
from .serializers import KlassSerializer, TeacherSerializer, StudentSerializer, UserSerializer, UserRegistrationSerializer, TokenPairSerializer

# restga tegishli
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken




class KlassViewSet(viewsets.ModelViewSet):
    
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class TeacherViewSet(viewsets.ModelViewSet):
    
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class StudentViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer



class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response(TokenPairSerializer({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }).data, status=status.HTTP_200_OK)
    


def home(request):
    return render(request, 'home.html')