from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from staff_doctor.models import Appointment
from staff_doctor.serializers import AppointmentSerializer
# Create your views here.

class AppointmentListCreateviews(APIView):
    def get(self,request):
        qs=Appointment.objects.all()# qs type qs => pynt
        serializer_instance=AppointmentSerializer(qs,many=True)
        return Response(data=serializer_instance.data) 