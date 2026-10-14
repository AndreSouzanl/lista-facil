
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProdutoForm
from .models import Produto



@login_required
def lista(request):
    produtos = Produto.objects.filter(
        criado_por=request.user,
        status__in=[
            Produto.Status.ATIVO,
            Produto.Status.EDITADO,
            Produto.Status.FINALIZADO,
        ],
    )

    total_produtos = produtos.count()

    total_comprados = produtos.filter(
        status=Produto.Status.FINALIZADO
    ).count()

    total_pendentes = total_produtos - total_comprados

    contexto = {
        "produtos": produtos,
        "total_produtos": total_produtos,
        "total_comprados": total_comprados,
        "total_pendentes": total_pendentes,
    }

    return render(request, "produtos/lista.html", contexto)


@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, usuario=request.user)

        if form.is_valid():
            if form.produto_removido:
                return render(
                    request,
                    "produtos/formulario.html",
                    {
                        "form": form,
                        "produto_removido": form.produto_removido,
                    },
                )
            produto = form.save(commit=False)
            produto.criado_por = request.user
            produto.save()

            messages.success(
                request,
                "Produto adicionado à sua lista com sucesso!",
            )

            return redirect("produtos:lista")
    else:
        form = ProdutoForm(usuario=request.user)

    return render(
        request,
        "produtos/formulario.html",
        {"form": form},
    )


@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        id=produto_id,
        criado_por=request.user,
    )

    if produto.status == Produto.Status.REMOVIDO:
        messages.error(
            request,
            "Este produto não está mais disponível.",
        )
        return redirect("produtos:lista")

    if request.method == "POST":
        form = ProdutoForm(
            request.POST,
            instance=produto,
            usuario=request.user
        )

        if form.is_valid():
            produto = form.save(commit=False)
            produto.status = Produto.Status.EDITADO
            produto.atualizado_por = request.user
            produto.save()

            messages.success(
                request,
                "Produto atualizado com sucesso!",
            )

            return redirect("produtos:lista")
    else:
        form = ProdutoForm(
            instance=produto,
            usuario=request.user,
        )

    return render(
        request,
        "produtos/formulario.html",
        {
            "form": form,
            "produto": produto,
        },
    )


@login_required
@require_POST
def excluir_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        id=produto_id,
        criado_por=request.user,
    )

    if produto.status != Produto.Status.REMOVIDO:
        produto.status = Produto.Status.REMOVIDO
        produto.removido_por = request.user
        produto.save()

        messages.success(
            request,
            "Produto removido da sua lista.",
        )

    return redirect("produtos:lista")


@login_required
@require_POST
def alternar_comprado(request, produto_id):
    produto = get_object_or_404(
        Produto,
        id=produto_id,
        criado_por=request.user,
    )

    if produto.status == Produto.Status.REMOVIDO:
        messages.error(
            request,
            "Este produto não está mais disponível.",
        )
        return redirect("produtos:lista")

    if produto.status == Produto.Status.FINALIZADO:
        produto.status = Produto.Status.ATIVO
        mensagem = "Produto marcado como pendente."
    else:
        produto.status = Produto.Status.FINALIZADO
        mensagem = "Produto marcado como comprado."

    produto.atualizado_por = request.user
    produto.save()

    messages.success(request, mensagem)

    return redirect("produtos:lista")

@login_required
@require_POST
def reativar_produto(request, produto_id):
    produto = get_object_or_404(
        Produto,
        id=produto_id,
        criado_por=request.user,
        status=Produto.Status.REMOVIDO,
    )

    produto.status = Produto.Status.ATIVO
    produto.atualizado_por = request.user
    produto.save()

    messages.success(
        request,
        f"{produto.nome} foi reativado na sua lista!",
    )

    return redirect("produtos:lista")
