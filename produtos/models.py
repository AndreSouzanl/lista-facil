from django.db import models
from django.conf import settings



class Produto(models.Model):
    class Unidade(models.TextChoices):
        UNIDADE = "un", "Unidade"
        QUILOGRAMA = "kg", "Quilograma"
        GRAMA = "g", "Grama"
        LITRO = "lt", "Litro"
        CAIXA = "cx", "Caixa"
        METRO = "m", "Metro"
        PACOTE = "pc", "Pacote"

    class Status(models.TextChoices):
        ATIVO = "ativo", "Ativo"
        EDITADO = "editado", "Editado"
        REMOVIDO = "removido", "Removido"
        FINALIZADO = "finalizado", "Finalizado"

    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    quantidade = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    unidade = models.CharField(
        max_length=2,
        choices=Unidade.choices,
        default=Unidade.UNIDADE,
    )

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ATIVO,
    )

    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="produtos_criados",
    )

    atualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="produtos_atualizados",
        null=True,
        blank=True,
    )

    removido_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="produtos_removidos",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["nome"]
        constraints = [
            models.UniqueConstraint(
                fields=["nome", "criado_por"],
                name="produto_nome_unico_por_usuario",
            ),
        ]

    def __str__(self):
        return self.nome
