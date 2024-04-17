from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_events(self):
        self.client.get("http://localhost:8000/events/")

    @task(3)
    def view_event_details(self):
        self.client.get("http://localhost:8000/events/1/")

    @task
    def create_event(self):
        self.client.post("/events/", json={
            "event_name": "Новое мероприятие",
            "event_date": "2024-05-01",
            "location": "Худжанд",
            "description": "Описание нового мероприятия",
            "organizer": "Организатор"
        })
