from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    def __init__(self, *args, usuario=None, **kwargs):
        self.usuario = usuario
        self.produto_removido = None
        super().__init__(*args, **kwargs)

    class Meta:
        model = Produto
        fields = ["nome", "quantidade", "unidade"]

        labels = {
            "nome": "Nome do produto",
            "quantidade": "Quantidade",
            "unidade": "Unidade de medida",
        }

        widgets = {
            "nome": forms.TextInput(
                attrs={"placeholder": "Ex.: Arroz"}
            ),
            "quantidade": forms.NumberInput(
                attrs={"min": "0.01", "step": "0.01"}
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data["nome"].strip()

        if self.usuario:
            produtos = Produto.objects.filter(
                criado_por=self.usuario,
                nome__iexact=nome,
            )

            if self.instance.pk:
                produtos = produtos.exclude(pk=self.instance.pk)

            produto_removido = produtos.filter(
                status=Produto.Status.REMOVIDO
            ).first()

            if produto_removido:
                self.produto_removido = produto_removido
                return nome

            if produtos.exists():
                raise forms.ValidationError(
                    "Você já possui um produto com esse nome na sua lista."
                )

        return nome
