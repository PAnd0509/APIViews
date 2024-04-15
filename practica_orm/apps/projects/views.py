from django.shortcuts import render

#self modules
from .models import *
# Create your views here.
#Utils
from datetime import datetime

#Other modules
from rest_framework.views import APIView
from rest_framework.response import Response

class ProjectAPIView(APIView):
    #Que me traiga todos los proyectos
    def get(self, request):

        projects=Project.objects.all()
        #Jason
        data=[
            {
                "id":project.id,
                "name":project.name
            }
            for project in projects
        ]
        return Response(data)
    
    def post(self, request):
        
        project = Project()
        project.name=request.data.get('name', "")
        project.init_date=datetime.now()
        end_date=request.data.get('end_date',"")
        project.end_date=datetime.strptime(end_date,'%d-%m-%YT%H:%M:%S')
        project.save()
        return Response({})
    
    def delete(self, request):
        id = request.data.get("id")
        #Lista de objetos con algo en especifico
        #project=Project.objects.filter()

        project=Project.objects.get(id=id)

        project.delete()

        return Response({})
    
    def patch(self, request):
        id = request.data.get("id")
        project=Project.objects.get(id=id)
        project.name=request.data.get("name",project.name)
        project.save()
        return Response({
            "id":project.id,
            "name":project.name
        })

""" TAREA """
class TaskAPIView(APIView):
    #Que me traiga todos los proyectos
    def get(self, request):

        tasks=Task.objects.all()
        #Jason
        data=[
            {
                "id":task.id,
                "description":task.description,
                "project":task.project.name
            }
            for task in tasks
        ]
        return Response(data)
    
    def post(self, request):
        
        task=Task()
        id = request.data.get("project")
        task.project=Project.objects.get(id=id)
        task.description=request.data.get('description', "")
        end_date=request.data.get('end_date',"")
        task.end_date=datetime.strptime(end_date,'%d-%m-%YT%H:%M:%S')
        task.task_type=request.data.get('task_type',"")
        
        task.save()
        return Response({})
    
    def delete(self, request):
        id = request.data.get("id")
        task=Task.objects.get(id=id)

        task.delete()

        return Response({})
    
    def patch(self, request):
        id = request.data.get("id")
        task=Task.objects.get(id=id)
        task.description=request.data.get("description",task.description)
        task.save()
        return Response({
            "id":task.id,
            "description":task.description
        })