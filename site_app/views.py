import csv
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Classificacao

def index(request):
    """ Página inicial para escolher o ano """
    return render(request, 'index.html')

def select_csv(request, ano):
    """ Página para escolher o tema dentro do ano selecionado """
    return render(request, 'select_csv.html', {'ano': ano})

def visualizar_csv(request, ano, arquivo):
    """ Abre o CSV escolhido dentro do ano selecionado """
    csv_path = os.path.join(settings.BASE_DIR, 'site_app', 'templates', str(ano), arquivo)
    questoes = []

    # Lendo o CSV
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        header = next(leitor)  # Ignorar cabeçalhos
        
        for linha in leitor:
            contexto = linha[1]  # Número do contexto usado para buscar a pasta de imagens
            imagem_dir = os.path.join(settings.BASE_DIR, 'site_app', 'templates', str(ano), f"{contexto}-images")
            imagens = []

            # Verifica se a pasta de imagens existe dentro do ano escolhido
            if os.path.exists(imagem_dir):
                for i in range(2):  # Pode ter até duas imagens (0 e 1)
                    img_filename = f"context_img_{i}.jpg"
                    img_path = os.path.join(imagem_dir, img_filename)
                    if os.path.exists(img_path):
                        imagens.append(f"{ano}/{contexto}-images/{img_filename}")  # Caminho relativo para o template

            # Verifica se a questão já foi classificada
            classificacao_obj = Classificacao.objects.filter(numero_questao=linha[0]).first()
            classificacao = classificacao_obj.classificacao if classificacao_obj else "Não classificado"

            questao = {
                'numero': linha[0],  # Número da questão
                'contexto': contexto,  # Contexto
                'enunciado': linha[2],  # Pergunta
                'A': linha[3],  # Alternativa A
                'B': linha[4],  # Alternativa B
                'C': linha[5],  # Alternativa C
                'D': linha[6],  # Alternativa D
                'E': linha[7],  # Alternativa E
                'imagens': imagens,  # Lista de imagens do contexto
                'classificacao': classificacao  # Classificação da questão
            }
            questoes.append(questao)

    return render(request, 'home.html', {'questoes': questoes, 'ano': ano, 'arquivo': arquivo})

def salvar_classificacao(request):
    """ Salva a classificação da questão no banco de dados via AJAX """
    if request.method == "POST":
        numero_questao = request.POST.get("numero_questao")
        classificacao = request.POST.get("classificacao")

        # Atualiza ou cria a classificação para a questão
        obj, created = Classificacao.objects.update_or_create(
            numero_questao=numero_questao,
            defaults={"classificacao": classificacao}
        )

        return JsonResponse({"status": "success", "message": "Classificação salva!"})
    return JsonResponse({"status": "error", "message": "Método inválido."})
