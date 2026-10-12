
from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "quantidade", "unidade"]

        labels = {
            "nome": "Nome do produto",
            "descricao": "Descrição",
            "quantidade": "Quantidade",
            "unidade": "Unidade de medida",
        }

        widgets = {
            "nome": forms.TextInput(
                attrs={"placeholder": "Ex.: Arroz"}
            ),
            "descricao": forms.Textarea(
                attrs={
                    "placeholder": "Marca ou observações (opcional)",
                    "rows": 3,
                }
            ),
            "quantidade": forms.NumberInput(
                attrs={"min": "0.01", "step": "0.01"}
            ),
        }
