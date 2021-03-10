from locust import HttpUser, task, between
from random import randint


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(2)
    def get_available_pets(self):
        self.client.get("/v2/pet/findByStatus?status=available")

    @task(3)
    def get_pending_pets(self):
        self.client.get("/v2/pet/findByStatus?status=pending")

    @task
    def get_sold_pets(self):
        self.client.get("/v2/pet/findByStatus?status=sold")

    @task
    def get_pet_by_id(self):
        pet_id = randint(1, 20)
        self.client.get(f"/v2/pet/{pet_id}")

    def on_start(self):
        pass
