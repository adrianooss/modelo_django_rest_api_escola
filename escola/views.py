from escola.models import Estudante, Curso, Matricula
from escola.serializers import \
    EstudanteSerializer,CursoSerializer, MatriculaSerializer, \
    ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para CRUD de estudantes.
    
    Campos de ordenação:
    -nome : permite ordenar os resultados por nome.
    
    Campos de busca:
    -nome : permite buscar estudantes pelo nome.
    -cpf : permite buscar estudantes pelo CPF.
    
    Métodos HTTP permitidos:
    - GET, POST, PUT, PATCH, DELETE
    
    Classe de Serializer:
    - EstudanteSerializer: usado para serializar e desserializar dados de estudantes.
    - Se API for 'v2', EstudanteSerializerV2 será usado.
    """
    queryset = Estudante.objects.all().order_by("id")
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para CRUD de cursos.

    Métodos HTTP permitidos:
    - GET, POST
    Throttle: Classes:
    - UserRateThrottle: Limita a taxa de requisições por usuário autenticado.
    - MatriculaAnonRateThrottle: Limita a taxa de requisições por usuários anônimos.
    """
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - ViewSet de Matrículas
    Parâmetros:
    - queryset: Retorna todas as matrículas ordenadas pelo campo id
    """
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get","post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
