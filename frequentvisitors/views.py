from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import VisitorsTable
from .serializers import VisitorSerializer

#
# class VisitView(viewsets.ModelViewSet):
#     queryset = VisitorsTable.objects.all()
#     serializer_class = VisitorSerializer


class VisitView(generics.ListAPIView):
    serializer_class = VisitorSerializer
    queryset = VisitorsTable.objects.all()
