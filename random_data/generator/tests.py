from django.test import TestCase, Client
from django.urls import reverse
from channels.testing import WebsocketCommunicator
from .models import RandomNumber
from .consumers import NumberConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
import generator.routing
import json
from asgiref.sync import sync_to_async


# Tests for models
class RandomNumberModelTest(TestCase):
    def test_string_representation(self):
        number = RandomNumber(number=42)
        self.assertEqual(str(number), "42 at None")

    def test_create_random_number(self):
        number = RandomNumber.objects.create(number=42)
        self.assertEqual(number.number, 42)


# Tests for views
class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse("index")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.generate_url = reverse("generate_random_number")
        self.latest_url = reverse("get_latest_number")
        self.all_numbers_url = reverse("get_all_numbers")

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login because of LoginRequiredMixin

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "generator/login.html")

    def test_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_generate_random_number_view(self):
        response = self.client.get(self.generate_url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn("number", data)

    def test_get_latest_number_view(self):
        RandomNumber.objects.create(number=42)
        response = self.client.get(self.latest_url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data["number"], 42)

    def test_get_all_numbers_view(self):
        RandomNumber.objects.create(number=42)
        response = self.client.get(self.all_numbers_url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data["numbers"]), 1)
        self.assertEqual(data["numbers"][0]["number"], 42)


# Tests for WebSocket consumers
class ConsumersTestCase(TestCase):
    async def test_number_consumer(self):
        application = ProtocolTypeRouter(
            {
                "websocket": URLRouter(generator.routing.websocket_urlpatterns),
            }
        )

        communicator = WebsocketCommunicator(application, "ws/number/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)

        await sync_to_async(RandomNumber.objects.create)(number=42)
        await communicator.send_json_to({"type": "test.message"})
        response = await communicator.receive_json_from()
        self.assertEqual(response["number"], 42)

        await communicator.disconnect()
