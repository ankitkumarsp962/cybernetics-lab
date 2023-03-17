from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

apiclient = APIClient()

class PrettifyNumberTestCase(APITestCase):
    '''
    Test cases for all numeric type till quadrillion.
    '''

    def test_for_less_then_1000(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 500})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "500")
    
    def test_for_thousand(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 3400})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "3.5K")
        data = apiclient.get(url,{'q': 15000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "15K")       
        data = apiclient.get(url,{'q': 1000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1K")   

    def test_for_million(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 1500000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1.5M")
        data = apiclient.get(url,{'q': 15000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "15M")       
        data = apiclient.get(url,{'q': 1000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1M")
    
    def test_for_billion(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 2500000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "2.5B")
        data = apiclient.get(url,{'q': 15000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "15B")       
        data = apiclient.get(url,{'q': 1000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1B") 
    
    def test_for_trillion(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 1500000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1.5T")
        data = apiclient.get(url,{'q': 15000000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "15T")       
        data = apiclient.get(url,{'q': 1000000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1T")  

    def test_for_quadrillion(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 1500000000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1.5Q")
        data = apiclient.get(url,{'q': 15000000000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "15Q")       
        data = apiclient.get(url,{'q': 1000000000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "1Q")  

    def test_for_above_quadrillion(self):
        url= reverse("prettfy_number")
        data = apiclient.get(url,{'q': 15000000000000000000})
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.json()["query"], "Number above quadrillion")    
        