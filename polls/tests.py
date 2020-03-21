from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from polls import apiviews

# Create your tests here.

class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        
    
    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                        'Expected Response Code 200, recived {0} instead.'
                        .format(response.status_code))
        
        
    
    def test_list2(self):
        self.client.login(username = "test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200, "Expected Response Code 200, received {0} instead.".format(response.status_code))
        
        
    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you",
            "cretaed_by": 1
        }
        
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201, "Expected Response Code 201, received {0} instead"
                         .format(response.status_code))