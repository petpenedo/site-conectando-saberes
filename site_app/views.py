import csv
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Classificacao

def index(request):
    anos = list(range(2009, 2024))
    return render(request, 'index.html', {'anos': anos})

def select_csv(request, ano):
    return render(request, 'select_csv.html', {'ano': ano})

def visualizar_csv(request, ano, arquivo):
    pasta = f"enem-{ano}"

    mapa_areas = {
        'ciencias-humanas.csv': 'Ciências Humanas',
        'matematica.csv': 'Matemática',
        'ciencias-natureza.csv': 'Ciências da Natureza',
        'linguagens.csv': 'Linguagens'
    }
    area_conhecimento = mapa_areas.get(arquivo, 'Área Desconhecida')

    csv_path = os.path.join(settings.BASE_DIR, 'site_app', 'templates', pasta, arquivo)
    questoes = []

    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            leitor = csv.reader(csvfile)
            header = next(leitor)

            for linha in leitor:
                contexto = linha[1]
                imagens = []
                imagem_dir = os.path.join(settings.BASE_DIR, 'site_app', 'templates', pasta, f"{contexto}-images")

                if os.path.exists(imagem_dir):
                    for i in range(2):
                        img_filename = f"context_img_{i}.jpg"
                        img_path = os.path.join(imagem_dir, img_filename)
                        if os.path.exists(img_path):
                            imagens.append(f"{pasta}/{contexto}-images/{img_filename}")

                classificacao_obj = Classificacao.objects.filter(
                    numero_questao=linha[0],
                    area_conhecimento=area_conhecimento,
                    ano=ano
                ).first()

                classificacao = classificacao_obj.classificacao if classificacao_obj else "Não classificado"

                questao = {
                    'numero': linha[0],
                    'contexto': contexto,
                    'enunciado': linha[2],
                    'question': linha[3],
                    'A': linha[4],
                    'B': linha[5],
                    'C': linha[6],
                    'D': linha[7],
                    'E': linha[8],
                    'resposta': linha[9],
                    'imagens': linha[10],
                    'classificacao': classificacao
                }
                questoes.append(questao)

    except FileNotFoundError:
        return render(request, 'home.html', {
            'questoes': [],
            'ano': ano,
            'area_conhecimento': area_conhecimento,
            'arquivo': arquivo,
            'erro': f"Arquivo {arquivo} não encontrado para o ano {ano}."
        })

    return render(request, 'home.html', {
        'questoes': questoes,
        'ano': ano,
        'area_conhecimento': area_conhecimento,
        'arquivo': arquivo
    })

def salvar_classificacao(request):
    if request.method == "POST":
        numero_questao = int(request.POST.get("numero_questao"))
        classificacao = request.POST.get("classificacao")
        ano = int(request.POST.get("ano"))
        area_conhecimento = request.POST.get("area_conhecimento")

        Classificacao.objects.update_or_create(
            numero_questao=numero_questao,
            ano=ano,
            area_conhecimento=area_conhecimento,
            defaults={'classificacao': classificacao}
        )

        return JsonResponse({"status": "success", "message": "Classificação salva ou atualizada com sucesso!"})

    return JsonResponse({"status": "error", "message": "Método inválido."})
