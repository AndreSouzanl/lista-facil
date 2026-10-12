
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    username = forms.CharField(
        label="Nome de usuário",
        max_length=150,
        help_text="Use até 150 caracteres: letras, números e @/./+/-/_.",
    )

    email = forms.EmailField(
        label="E-mail",
        required=True,
    )

    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        help_text=(
            "A senha deve ter pelo menos 8 caracteres, "
            "não pode ser muito comum, totalmente numérica "
            "ou muito semelhante aos seus dados pessoais."
        ),
    )

    password2 = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput,
        help_text="Digite novamente a mesma senha.",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
