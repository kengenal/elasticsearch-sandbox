from django.urls import reverse


def test_index(client):
    rq = client.get(reverse("package"))

    assert rq.status_code == 200
