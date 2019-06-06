from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from talkApp.models import Talk
from api.serializers import TalkSerializer
from rest_framework import generics




# class TalkList(generics.ListAPIView):
#     queryset = Talk.objects.all()
#     serializer_class = TalkSerializer


# class TalkDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Talk.objects.all()
#     serializer_class = TalkSerializer


# @api_view(['GET', 'UPDATE', 'DELETE'])
# def GetTalk(request,pk):

#     if pk is '':
#         talks = Talk.objects.all()
#         serializer = TalkSerializer(talks, many=True)
#         return Response(serializer.data)
#     try:
#         talk = Talk.objects.get(pk=pk)
#     except Talk.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # get details of a single puppy
#     if request.method == 'GET':
#         serializer = TalkSerializer(talk)
#         return Response(serializer.data)



# @api_view(['GET', 'DELETE', 'PUT'])
# def get_delete_update_talk(request, pk):
#     try:
#         talk = Talk.objects.get(pk=pk)
#     except Talk.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # get details of a single Talk
#     if request.method == 'GET':
#         return Response({})
#     # delete a single Talk
#     elif request.method == 'DELETE':
#         return Response({})
#     # update details of a single Talk
#     elif request.method == 'PUT':
#         return Response({})



@api_view(['Get'])
def GetTalks(request):
    "get all Talks"
    if request.method == 'GET':
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response(serializer.data)
    

@api_view(['Get'])
def GetTalk(request,pk):
    "get a talk with id:pk"
    try:
        talk = Talk.objects.get(pk=pk)
    except Talk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TalkSerializer(talk)
        return Response(serializer.data)


@api_view(['POST'])
def Insert(request):
    "insert a talk using POST/CREATE"

    if request.method == 'POST':
        serializer = TalkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Update(request,pk):
    "Update a talk using id:pk,  PUT/UPDATE"

    try:
        talk = Talk.objects.get(pk=pk)
    except Talk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TalkSerializer(talk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def Delete(request,pk):
    "DELETE a talk using id:pk,  DELETE/Delete"

    try:
        talk = Talk.objects.get(pk=pk)
    except Talk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        talk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def talk_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TalkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def talk_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        talk = Talk.objects.get(pk=pk)
    except Talk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TalkSerializer(talk)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TalkSerializer(talk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        talk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)