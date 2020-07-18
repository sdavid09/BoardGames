from django.test import TestCase
from django.urls import reverse

class TestChessPage(TestCase):
    def test_chess_page(self):
        response = self.client.get(reverse("chess"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chess/index.html')
        self.assertTemplateUsed(response, 'chess/base.html')
        # self.assertContains(response, 'Chess')