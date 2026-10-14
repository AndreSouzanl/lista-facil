from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views

app_name = "usuarios"

urlpatterns = [
    path(
        "cadastro/",
        views.cadastrar,
        name="cadastro",
    ),

    path(
        "senha/esqueci/",
        auth_views.PasswordResetView.as_view(
            template_name="usuarios/senha_esqueci.html",
            email_template_name="usuarios/email_redefinir_senha.txt",
            subject_template_name="usuarios/assunto_redefinir_senha.txt",
            success_url=reverse_lazy("usuarios:senha_enviada"),
        ),
        name="senha_esqueci",
    ),

    path(
        "senha/enviada/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="usuarios/senha_enviada.html",
        ),
        name="senha_enviada",
    ),

    path(
        "senha/redefinir/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="usuarios/senha_redefinir.html",
            success_url=reverse_lazy("usuarios:senha_redefinida"),
        ),
        name="senha_redefinir",
    ),

    path(
        "senha/redefinida/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="usuarios/senha_redefinida.html",
        ),
        name="senha_redefinida",
    ),
]