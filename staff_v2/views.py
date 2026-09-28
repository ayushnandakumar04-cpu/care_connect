from django.shortcuts import render
from rest_framework.views import APIView
from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer
from rest_framework.response import Response
# Create your views here.
class DoctorListCreateview(APIView):

    def get(self,request):
        qs=Doctor.objects.all()
        serializer_instants=DoctorSerializer(qs)
        return Response(data=serializer_instants.data)
    
    def post(self,request):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Doctor.objects.create(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(serializer_instance.errors)

class DoctorRetrieveUpdateDelete(APIView):
    def get(self,request,pk=None):
        qs=Doctor.objects.get(id=pk)
        serializer_instance=DoctorSerializer(qs)
        return Response(data=serializer_instance.data)


