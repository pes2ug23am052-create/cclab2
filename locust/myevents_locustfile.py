from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    # Simulate realistic user think time with a wider range
    wait_time = between(1, 3)

    @task(3)  # Weighted: runs more often
    def view_events(self):
        # Use params dict for clarity and scalability
        self.client.get("/events", params={"user": "locust_user"})

    @task(1)  # Additional task for variety
    def view_homepage(self):
        self.client.get("/")

    def on_start(self):
        # Optional: simulate login or setup before tasks
        self.client.post("/login", json={"username": "locust_user", "password": "test"})
