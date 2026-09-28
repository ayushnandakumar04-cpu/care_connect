from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from staff.models import Doctor
# Create your views here.
# superhero,doctor
class DoctorListCreateView(APIView):
    def get(self,request):
        qs=Doctor.objects.all().values()
        d_list=list(qs)
        return Response(data=d_list)

    def post(self,request):
        form_data=request.data
        Doctor.objects.create(
            name=form_data.get("name"),
            specialization=form_data.get("specialization"),
            fee=form_data.get("fee"),
            qualification=form_data.get("qualification"),
            email=form_data.get("email")
        )
        return Response(data=
                        {"message":"created"}
                    )

class DoctorListRetrieveView(APIView):
    def get(self,request,pk=None):
        qs=Doctor.objects.filter(id=pk).values()
        d_list = list(qs)
        return Response(data=d_list)
    
    def delete(self,request, pk):
             D= Doctor.objects.get(id=pk)
             D.delete()

             d_list= {
                "Message": "Deleted successfully"
            }
             return Response(data=d_list)   

    def put(self,request,pk):
        form_data =(request.data)
        doctor = Doctor.objects.get(id=pk)
        Doctor.objects.create(
                            name=form_data.get("name"),
                            specialization=form_data.get("specialization"),
                            fee=form_data.get("fee"),
                            qualification=form_data.get("qualification"),
                            email=form_data.get("email")
                    )
        
        response_data={
                "Message": "Movie updated successfully"
            }
        return Response(data=response_data)


    