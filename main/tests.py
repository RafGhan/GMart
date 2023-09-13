from django.test import TestCase

from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_templates_contain_title(self):
        response = Client().get('/main/')
        self.assertContains(response, '<h1>GMart Page</h1>')
