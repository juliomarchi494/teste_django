from django.core.management.base import BaseCommand
from chatbot.models import Categoria, Informacao


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # Categorias
        categorias = [
            "Lentes",
            "Tratamentos",
            "Materiais",
            "Campo de visão",
            "Exame de vista",
            "Informações sobre a Ótica Renew",
            "Orçamento"
        ]

        for nome in categorias:
            Categoria.objects.get_or_create(nome=nome)

        # Informações
        dados = [
            {
                "categoria": "Tratamentos",
                "titulo": "Antirreflexo",
                "resposta": "O tratamento antirreflexo reduz reflexos nas lentes e melhora o conforto visual."
            },
            {
                "categoria": "Tratamentos",
                "titulo": "Filtro azul",
                "resposta": "O filtro azul é um tratamento que pode ser aplicado às lentes."
            },
            {
                "categoria": "Lentes",
                "titulo": "Lentes multifocais",
                "resposta": "As lentes multifocais permitem enxergar em diferentes distâncias."
            }
        ]

        for item in dados:

            categoria = Categoria.objects.get(
                nome=item["categoria"]
            )

            Informacao.objects.get_or_create(
                categoria=categoria,
                titulo=item["titulo"],
                defaults={
                    "resposta": item["resposta"]
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Banco populado com sucesso!"
            )
        )