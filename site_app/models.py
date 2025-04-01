from django.db import models

class Classificacao(models.Model):
    numero_questao = models.IntegerField(unique=True)  # Número da questão
    classificacao = models.CharField(max_length=20)  # Classe escolhida (ex: "Classe 1")

    def __str__(self):
        return f"Questão {self.numero_questao} - {self.classificacao}"
