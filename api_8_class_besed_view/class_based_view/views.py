from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class student_api(APIView):
    def get(self, request, format=None, pk=None):
        id = request.data.get('id')  # sourcery skip: avoid-builtin-shadow
        if id is not None:
            stu = Student.objects.get(id=id)
            serialize = StudentSerializer(stu)
            return Response(serialize.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data post successfully"}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk  # sourcery skip: avoid-builtin-shadow
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data updated successfully"}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        id = pk  # sourcery skip: avoid-builtin-shadow
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data updated partially successfully"}
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk  # sourcery skip: avoid-builtin-shadow
        stu = Student.objects.get(id=pk)
        stu.delete()
        res = {"msg": "data deleted successfully"}
        return Response(res, status=status.HTTP_201_CREATED)
