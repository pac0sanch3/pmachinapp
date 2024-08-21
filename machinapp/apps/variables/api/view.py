from rest_framework import viewsets

from apps.variables.models import Variable
from apps.variables.api.serializer import VariablesSerializador

class VariableModelViewSet(viewsets.ModelViewSet):
    serializer_class = VariablesSerializador
    queryset = Variable.objects.all()
    http_method_names = ['post', 'get', 'put']

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)