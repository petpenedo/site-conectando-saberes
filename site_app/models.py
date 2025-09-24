from django.db import models

class Classificacao(models.Model):
    numero_questao = models.IntegerField()
    classificacao = models.CharField(max_length=20)
    ano = models.IntegerField()
    area_conhecimento = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['numero_questao', 'ano', 'area_conhecimento'],
                name='unique_classificacao'
            )
        ]

    def __str__(self):
        return f"Questão {self.numero_questao} - {self.classificacao} ({self.ano}, {self.area_conhecimento})"
