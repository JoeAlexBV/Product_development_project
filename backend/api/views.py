from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Risk
from .serializers import RiskSerializer


class RiskDetail(APIView):
    """
    Get, update, or delete a single risk instance
    """
    def get_object(self, pk):
        try:
            risk = Risk.objects.get(pk=pk)
            return(risk)
        except Risk.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # get details of a single risk
        risk = self.get_object(pk)
        serializer = RiskSerializer(risk)
        return Response(serializer.data)

    def put(self, request, pk):
        # update details of a single risk
        risk = self.get_object(pk)
        serializer = RiskSerializer(risk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        risk = self.get_object(pk)
        risk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RiskList(APIView):
    """
    List all risks, or create a new risk
    """
    def get(self, request):
        risk = Risk.objects.all()
        serializer = RiskSerializer(risk, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
