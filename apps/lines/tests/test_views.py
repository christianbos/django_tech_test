# STDLIB IMPORTS
import json

# DJANGO CORE IMPOTS
from django.urls import reverse

#THIRD-PARTY IMPOTS
from rest_framework.test import APITestCase

# URBVAN IMPORTS
from ..models import LineModel, RouteModel
from apps.users.factories import UserFactory, TokenFactory


class LinesModelTests(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )
        instance, created = LineModel.objects.get_or_create(name='South', color='Red')
    
        self.create_read_url = reverse('lines:lines-list')
        self.read_update_delete_url = reverse(
            'lines:lines-detail', kwargs={'pk': instance.pk}
        )
    
    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertContains(response, 'South')
    
    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        post = {
            'color': 'Black',
            'name': 'East'
        }
        response = self.client.post(self.create_read_url, post)
        self.assertEquals(response.status_code, 201)
    
    def test_delete(self):
        response = self.client.delete(self.read_update_delete_url)
        self.assertEquals(response.status_code, 403) # ONLY URBVAN ADMINS HAVE PERMISSION TO DELETE