from django.shortcuts import render
from rest_framework.views import APIView
from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializers
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
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

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):
        qs=Doctor.objects.get(id=pk)
        serializer_instance=DoctorSerializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Doctor.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)


class AdminRegister(APIView):

    def post(self,request):

        form_data = request.data

        serializers_instant = UserSerializers(data=form_data)

        if serializers_instant.is_valid():

            cleeaned_data = serializers_instant.validated_data

            User.objects.create_superuser(**cleeaned_data)

            return Response(data=serializers_instant.validated_data)

        else:

            return Response(serializers_instant.errors)



#turf_booking
#app_turf 