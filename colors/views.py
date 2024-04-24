from rest_framework import generics
from colors.models import Color
from colors.serializers import ColorSerializer


class ColorCreateListView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
