from django.http import HttpResponse
from django.shortcuts import render
from .forms import EnviarArquivoForm
from .models import EnviarArquivo, Transacoes


def enviar_arquivo(request):
    if request.method == "POST":
        form = EnviarArquivoForm(request.POST, request.FILES)
        arquivo = request.FILES["file"]

        arquivo_cnab = EnviarArquivo.objects.create(arquivo_cnab=arquivo)
        arquivo_cnab.save()

        lista_de_arquivos = []

        with open(
            f"enviars/{str(arquivo_cnab.arquivo_cnab)}", "r", encoding="utf-8"
        ) as read_file:
            for lista in read_file:
                lista_de_arquivos.append(lista)

        for lista in lista_de_arquivos:
            type = lista[:1]
            year = lista[1:5]
            month = lista[5:7]
            day = lista[7:9]
            value = lista[9:19]
            cpf = lista[19:30]
            card = lista[30:42]
            hour = lista[42:44]
            minute = lista[44:46]
            second = lista[46:48]
            owner = lista[48:62]
            store = lista[62:81]

            data = f"{day}/{month}/{year}"
            valor = int(value) / 100
            horario = f"{hour}:{minute}:{second}"

            if type == "1":
                type = "Débito"

            elif type == "2":
                type = "Boleto"

            elif type == "3":
                type = "Financiamento"

            elif type == "4":
                type = "Crédito"

            elif type == "5":
                type = "Empréstimo"

            elif type == "6":
                type = "Vendas"

            elif type == "7":
                type = "TED"

            elif type == "8":
                type = "DOC"

            elif type == "9":
                type = "Aluguel"

            reader = Transacoes.objects.create(
                type=type,
                date=data,
                value=valor,
                cpf=cpf,
                card=card,
                hour=horario,
                owner=owner,
                store=store,
            )

            reader.save()

        operacoes = Transacoes.objects.values(
            "type", "value", "date", "cpf", "hour", "owner", "store"
        )

        saldo_total = 0

        for operacao in operacoes:
            if (
                operacao["type"] == "Boleto"
                or operacao["type"] == "Financiamento"
                or operacao["type"] == "Aluguel"
            ):
                saldo_total -= operacao["value"]
            else:
                saldo_total += operacao["value"]

        return render(
            request,
            "results.html",
            context={"operacoes": operacoes, "saldo_total": saldo_total},
        )

    else:
        form = EnviarArquivoForm()
    return render(request, "enviarFile.html", {"form": form})