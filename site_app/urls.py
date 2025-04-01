from django.urls import path
from .views import index, select_csv, visualizar_csv, salvar_classificacao

urlpatterns = [
    path('', index, name='index'),  # Página inicial
    path('<int:ano>/', select_csv, name='select_csv'),  # Escolher tema dentro do ano
    path('<int:ano>/<str:arquivo>/', visualizar_csv, name='visualizar_csv'),  # Exibir CSV selecionado
    path('salvar-classificacao/', salvar_classificacao, name='salvar_classificacao'),  # Rota para salvar classificação
]
