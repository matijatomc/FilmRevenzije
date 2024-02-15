import factory
from django.contrib.auth.models import User
from .models import Film, Recenzija

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')

class FilmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Film

    nazivFilma = factory.Sequence(lambda n: f'Film {n}')
    redateljFilma = factory.Faker('name')
    godinaIzlaska = factory.Faker('year')
    zanr = factory.Iterator(['Akcija', 'Drama', 'Komedija', 'Horor'])

    @factory.post_generation
    def preporukeFilma(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for film in extracted:
                self.preporuke.add(film)
        else:
            broj_preporuka = 1
            filmovi = Film.objects.exclude(id=self.id).order_by('?')[:broj_preporuka]
            for film in filmovi:
                self.preporuke.add(film)


class RecenzijaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recenzija

    autorRecenzije = factory.Iterator(User.objects.all())
    recenzija = factory.Faker('text')
    ocjena = factory.Faker('pyint', min_value=0, max_value=10)
    film = factory.Iterator(Film.objects.all())

