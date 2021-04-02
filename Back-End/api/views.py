import os
from django.conf import settings
from django.shortcuts import render
from rest_framework import generics
from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .serializers import UsersSerializer,ProjectsSerializer,FileUploadSerializer
from .models import Users,Projects,FileUpload
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist, FieldError
from rest_framework.decorators import api_view, schema,parser_classes
from haystack.query import SearchQuerySet
from . import tika_db_parallel_process
from mysql import connector
from tika import parser



# class UsersDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer

# class UsersData(generics.ListAPIView):
#        queryset = Users.objects.all()
#        serializer_class = UsersSerializer


class UsersData(APIView):
    @action(detail=True, methods=["GET"])
    def get(self, request):
        try:
            userDataQuerySet = Users.objects.all()
            serializer = UsersSerializer(userDataQuerySet, many=True)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            return Response({"message": "No Users Found!"}, status=status.HTTP_404_NOT_FOUND)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # Must be authenticated in order to create new User.
    @action(detail=True, methods=["POST"])
    @csrf_exempt
    def post(self, request):
        serializer = UsersSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({"message": "User Created Successfully!."}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetails(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    @action(detail=True, methods=["GET"])
    def get(self, request, pk):
        try:
            userDataQuerySet = Users.objects.get(pk=pk)
            serializer = UsersSerializer(userDataQuerySet)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            return Response({"message": "User with id `{}` does not exist!.".format(pk)}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=["DELETE"])
    def delete(self, request, pk):
        try:
            userDataQuerySet = Users.objects.get(pk=pk)
            userDataQuerySet.delete()
            return Response({"message": "User with id `{}` has been deleted successfully!.".format(pk)}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"message": "User with id `{}` does not exist!.".format(pk)}, status=status.HTTP_404_NOT_FOUND)
    

    @action(detail=True, methods=["PUT"])
    @csrf_exempt
    def put(self, request, pk):
        userDataQuerySet = Users.objects.get(pk=pk)
        serializer = UsersSerializer(
            userDataQuerySet, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({"message": "User data with id `{}` has been successfully updated!.".format(pk)}, status=200)
        return JsonResponse({"message": "User with id `{}` does not exist! Invalid operation.".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["PATCH"])
    @csrf_exempt
    def patch(self, request, pk):
        try:
            userDataQuerySet = Users.objects.get(pk=pk)
            serializer = UsersSerializer(
                userDataQuerySet, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return JsonResponse({"message": "Data value for user with id `{}` has been successfully updated!.".format(pk)}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "Wrong parametars or invalid data provided!"}, status=status.HTTP_400_BAD_REQUEST)


class ProjectsData(APIView):
    @action(detail=True, methods=["GET"])
    def get(self, request):
        try:
            projectsDataQuerySet = Projects.objects.all()
            serializer = ProjectsSerializer(projectsDataQuerySet, many=True)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            return Response({"message": "No Projects Found!"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["POST"])
    @csrf_exempt
    def post(self, request):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({"message": "Project Created Successfully!."}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsDetails(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # Must be authenticated in order to create new Project.
    @action(detail=True, methods=["GET"])
    def get(self, request, pk, *args, **kwargs):
        try:
            projectsDataQuerySet = Projects.objects.get(pk=pk)
            serializer = ProjectsSerializer(projectsDataQuerySet)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            return Response({"message": "Project with id `{}` does not exist!.".format(pk)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["DELETE"])
    def delete(self, request, pk):
        try:
            projectsDataQuerySet = Projects.objects.get(pk=pk)
            projectsDataQuerySet.delete()
            return Response({"message": "Project with id `{}` has been deleted successfully!.".format(pk)}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"message": "Project with id `{}` does not exist!.".format(pk)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["PUT"])
    @csrf_exempt
    def put(self, request, pk):
        projectsDataQuerySet = Projects.objects.get(pk=pk)
        serializer = ProjectsSerializer(
            projectsDataQuerySet, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({"message": "Project data with id `{}` has been successfully updated!.".format(pk)}, status=200)
        return JsonResponse({"message": "Project with id `{}` does not exist! Invalid operation.".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["PATCH"])
    @csrf_exempt
    def patch(self, request, pk):
        try:
            projectsDataQuerySet = Projects.objects.get(pk=pk)
            serializer = ProjectsSerializer(
                projectsDataQuerySet, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return JsonResponse({"message": "Data value for project with id `{}` has been successfully updated!.".format(pk)}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "Wrong parametars or invalid data provided!"}, status=status.HTTP_400_BAD_REQUEST)



class FileUploadData(APIView):
    permission_classes = (permissions.IsAuthenticated,) # Must be authenticated in order to create upload Data!.
    @action(detail=True, methods=["GET"])
    def get(self, request):
        try:
            projectsDataQuerySet = FileUpload.objects.all()
            serializer = FileUploadSerializer(projectsDataQuerySet, many=True)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            return Response({"message": "No Files Found!"}, status=status.HTTP_404_NOT_FOUND)

#     @action(detail=True, methods=["POST"])
#     @csrf_exempt
#     def post(self, request):
#         serializer = FileUploadSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return JsonResponse({"message": "Document Uploaded Successfully!."}, status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class FileUploadData(APIView):
#     #permission_classes = (permissions.IsAuthenticated,) # Must be authenticated in order to create upload Data!.
#     @action(detail=True, methods=["GET"])
#     def get(self, request):
#         try:
#             projectsDataQuerySet = FileUpload.objects.filter(id=1)
#             serializer = FileUploadSerializer(projectsDataQuerySet, many=True)
#             return Response(serializer.data, status=200)
#         except ObjectDoesNotExist:
#             return Response({"message": "No Files Found!"}, status=status.HTTP_404_NOT_FOUND)

# class FileParser(APIView):
#     @action(detail=True, methods=["GET"])
#     def get(self, request):
#         tika_db_parallel_process.tika_parser('test.pdf') 
#         return ""


#     query = 'SELECT pdf_doc_path from api_fileupload;'
#     cnx = connector.connect(database='melondataDB', user='melon', password='Melon123!')
#     cur = cnx.cursor()
   
#     cur.execute(query)
#     paths = cur.fetchall()
#     i=0
#     while i < len(paths):
#         cp = os.getcwd()
#         cp=os.path.realpath(paths[i][i])
#         print("Current File Path :" ,cp)       
#         #file_data = parser.from_file(cp)
#         # Get files text content
#         #text = file_data['content']
#         print(cp)                                                          
#         file_data=tika_db_parallel_process.tika_parser('files/cv_pdf_doc/Dejan_Ivanovski_Melon_CV.pdf') #paths[i][i]
#         i+=1
  
