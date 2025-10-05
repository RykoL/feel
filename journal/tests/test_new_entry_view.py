import pytest

from django.contrib.auth.models import User
from ..models import Journal, JournalEntry


@pytest.mark.django_db
def test_creates_journal_for_user_if_it_doesnt_exist_yet(client, user):
    client.login(username="test-user", password="my-pw")

    resp = client.get("/journal/")
    assert resp.status_code == 200

    assert Journal.objects.filter(author=user.id).exists()


@pytest.mark.django_db
def test_creates_journal_entry_upon_successful_submission(client, journal):
    client.login(username="test-user", password="my-pw")

    data = {"journal": journal.id, "feeling": "good"}
    resp = client.post(f"/journal/{journal.id}/entry/new", data=data)

    assert resp.status_code == 302

    entry = JournalEntry.objects.get(journal_id=journal.id)
    observation = entry.observation_set.first()

    assert observation.feeling == "good"
    assert resp.url == f"/journal/{journal.id}/entry/{entry.id}/triggers"


@pytest.mark.django_db
def test_returns_404_if_journal_does_not_exist(client, journal):
    client.login(username="test-user", password="my-pw")

    data = {"journal_id": journal.id, "feeling": "good"}
    resp = client.get("/journal/300/entry/new", data=data)

    assert resp.status_code == 404


@pytest.mark.django_db
def test_returns_404_if_user_tries_to_access_journal_of_another_user(client, journal):
    second_user = User.objects.create_user(username="second-user", password="other-pw")
    journal = Journal.objects.create(author=second_user)

    client.login(username="second-user", password="other-pw")

    # Check if we can access the journal from the author user
    resp = client.get(f"/journal/{journal.id}/entry/new")
    assert resp.status_code == 200

    # Log in as other user
    client.login(username="test-user", password="my-pw")

    resp = client.get(f"/journal/{journal.id}/entry/new")

    assert resp.status_code == 404
