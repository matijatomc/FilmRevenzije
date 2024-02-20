from django.test import TestCase
from django.contrib.auth.models import User
from .models import Film, Recenzija
from .forms import RecenzijaForm
from django.urls import reverse

class FormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.film = Film.objects.create(
            nazivFilma='Inception',
            redateljFilma='Christopher Nolan',
            godinaIzlaska=2010,
            zanr='Sci-Fi'
        )

    def test_recenzija_form(self):
        form_data = {'ocjena': 8, 'recenzija': 'This is a great movie!', 'film': self.film}
        form = RecenzijaForm(data=form_data)

        self.assertTrue(form.is_valid())

class EditReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.film = Film.objects.create(
            nazivFilma='Inception',
            redateljFilma='Christopher Nolan',
            godinaIzlaska=2010,
            zanr='Sci-Fi'
        )
        self.review = Recenzija.objects.create(
            autorRecenzije=self.user,
            recenzija='This is a great movie!',
            ocjena=8,
            film=self.film
        )
        self.url = reverse('main:edit_review', args=[self.review.id])

    def test_edit_review_view_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_edit_review_view_POST(self):
        new_data = {'ocjena': 9, 'recenzija': 'Updated review'}
        response = self.client.post(self.url, new_data)
        updated_review = Recenzija.objects.get(id=self.review.id)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_review.ocjena, 9)
        self.assertEqual(updated_review.recenzija, 'Updated review')

class DeleteReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.film = Film.objects.create(
            nazivFilma='Inception',
            redateljFilma='Christopher Nolan',
            godinaIzlaska=2010,
            zanr='Sci-Fi'
        )
        self.review = Recenzija.objects.create(
            autorRecenzije=self.user,
            recenzija='This is a great movie!',
            ocjena=8,
            film=self.film
        )
        self.url = reverse('main:delete_review', args=[self.review.id])

    def test_delete_review_view_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_delete_review_view_POST(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Recenzija.objects.filter(id=self.review.id).exists())
