from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factory import FilmFactory, RecenzijaFactory

brojFilmova = 20
brojRecenzija = 25

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Film, Recenzija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(brojFilmova):
            film = FilmFactory()

        for _ in range(brojRecenzija):
            recenzija = RecenzijaFactory()
