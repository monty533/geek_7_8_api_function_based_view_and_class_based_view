from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_details(request):  # sourcery skip: avoid-builtin-shadow
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            print('monty')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data created"}
            return Response(res)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer. is_valid():
            serializer.save()
            res = {"msg": "updated"}
            return Response(res)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        res = {"msg": "deleted"}
        return Response(res)
