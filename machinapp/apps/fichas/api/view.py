from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

#permisos
from apps.fichas.api.permisos import IsAdmin
from rest_framework.permissions import IsAuthenticated
#fin de permisos

### modelo y serializadores
from apps.fichas.models import Ficha
from apps.fichas.api.serializer import FichaSerializerAmb, FichaSerializerDetalle, FichaSerializerRegisterUpdate, FichaLisar
 

#registrar y actualizar una ficha tecnica.
# url //http://127.0.0.1:8000/api/ficha/2/
class FichaRegisterUpdate(viewsets.ModelViewSet):

    serializer_class = FichaSerializerRegisterUpdate
    queryset = Ficha.objects.all()
    http_method_names = ['post', 'put']
    parser_classes = [MultiPartParser, FormParser]


#listar todas las  fichas
class FichaListar(viewsets.ModelViewSet):

    serializer_class = FichaLisar
    queryset = Ficha.objects.all()
    http_method_names = ['get']


# fichas buscadadas por el id del ambiente
#http://127.0.0.1:8000/api/fichas/ambiente/{id} 
class FichasAmbienteGet(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        ficha = Ficha.objects.filter(fk_ambiente=id)
        serializar = FichaSerializerAmb(ficha, many= True)
        
        if not serializar.data:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "No se encontraron fichas para este ambiente"})
        
        return Response(status=status.HTTP_200_OK, data=serializar.data)





""" -------------------------------------------------------------------- """
# crear un nuevo registro de la ficha tecnica de una maquina o equipo
class FichasPostSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = FichaSerializerDetalle
    queryset = Ficha.objects.all()
    http_method_names = ['post', 'put']
    parser_classes = [MultiPartParser,]




# detalle de la fichas
class FichasModelViewSet(APIView): 
    #permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id:
            ficha = Ficha.objects.filter(id=id)
            serializar = FichaSerializerDetalle(ficha, many= True)
            
        return Response(status=status.HTTP_200_OK, data=serializar.data)
