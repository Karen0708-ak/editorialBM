from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Libros
from .serializers import LibrosSerializer

class LibrosAPI(APIView):

    def get(self, request):
        libros = Libros.objects.all()
        serializer = LibrosSerializer(libros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        libro_id = request.data.get("id")
        if not libro_id:
            return Response({"error": "Debes enviar el id"}, status=400)

        try:
            libro = Libros.objects.get(id=libro_id)
        except Libros.DoesNotExist:
            return Response({"error": "Libro no encontrado"}, status=404)

        serializer = LibrosSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def delete(self, request):
        libro_id = request.data.get("id")
        if not libro_id:
            return Response({"error": "Debes enviar el id"}, status=400)

        try:
            libro = Libros.objects.get(id=libro_id)
        except Libros.DoesNotExist:
            return Response({"error": "Libro no encontrado"}, status=404)

        libro.delete()
        return Response({"mensaje": "Eliminado correctamente"})
