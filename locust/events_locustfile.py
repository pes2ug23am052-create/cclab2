from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # Simulate realistic user think time
    wait_time = between(1, 3)

    @task(3)  # weight = 3 → runs more often
    def view_events(self):
        # Use params dict for clarity & flexibility
        self.client.get("/events", params={"user": "locust_user"})

    @task(1)  # optional extra task for variety
    def homepage(self):
        self.client.get("/")
