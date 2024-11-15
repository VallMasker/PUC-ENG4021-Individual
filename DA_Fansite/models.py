from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Personagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  
    nome = models.CharField(max_length=100)
    icone_URL = models.URLField(max_length=100)
    descricao = models.TextField(blank=True)
    raca = models.CharField(max_length=50, choices=[('humano', 'Humano'), ('elfo', 'Elfo'), ('anao', 'Anão'), ('qunari', 'Qunari')])
    idade = models.IntegerField(validators=[MinValueValidator(1)])
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
      verbose_name_plural = "personagens"
    
    def __str__(self):
        return self.nome

class Classe(models.Model):
  nome = models.CharField(max_length=100)
  icone_URL = models.URLField(max_length=100)
  descricao = models.TextField(blank=True)
  tipo = models.CharField(max_length=50, choices=[('magico', 'Mágico'), ('fisico', 'Físico')])
  quantidade_especializacoes = models.IntegerField()
  link = models.URLField()
  ativo = models.BooleanField()

  def __str__(self):
      return self.nome

class ReferenciasPersonagem(models.Model):
  nome = models.CharField(max_length=100)
  link = models.URLField()
  personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)
  data_atualizacao = models.DateTimeField(auto_now=True)
  classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

  class Meta:
    verbose_name = "referencia do personagem"
    verbose_name_plural = "referencias dos personagens"

  def __str__(self):
      return self.nome

