from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task()
    def get_available_pets(self):
        self.client.get("/v2/pet/findByStatus?status=available")

    def on_start(self):
        pass
