# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, mydb, TimelinePost


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        mydb.create_tables([TimelinePost])

    def tearDown(self):
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Amanda Xi</title>" in html
        # TODO Add more tests relating to the home page
        assert "Amanda Xi" in html
        assert response.content_type.startswith("text/html")

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        post_response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!",
        })
        assert post_response.status_code == 200
        posted = post_response.get_json()
        assert posted["name"] == "John Doe"
        assert posted["email"] == "john@example.com"
        assert posted["content"] == "Hello world, I'm John!"

        get_response = self.client.get("/api/timeline_post")
        json = get_response.get_json()
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "John Doe"

        # TODO Add more tests relating to the timeline page
        timeline_page = self.client.get("/timeline")
        assert timeline_page.status_code == 200
        assert "<title>Timeline</title>" in timeline_page.get_data(as_text=True)

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html


if __name__ == '__main__':
    unittest.main()