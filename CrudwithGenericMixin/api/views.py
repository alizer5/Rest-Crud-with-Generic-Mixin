from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
import requests

class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        def get(self, request,*args,**kwargs):
            return self.list(request,*args,**kwargs)
    
        def post(self, request,*args,**kwargs):
        
            return self.create(request,*args,**kwargs)
        


class StudentUpDel(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
      queryset=Student.objects.all()
      serializer_class=StudentSerializer
      def put(self, request,*args,**kwargs):
            return self.update(request,*args,**kwargs)
      
      def delete(self, request,*args,**kwargs):
            return self.destroy(request,*args,**kwargs)
     
      def get(self, request,*args,**kwargs):
            return self.retrieve(request,*args,**kwargs)
      