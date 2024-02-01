from locust import HttpUser, task, between

class IndexTasks(HttpUser):

    wait_time = between(0.5, 2.5)

    @task
    def index(self):
        self.client.get("/") # home da página


    