import pytest

from django.contrib.auth.models import User
from ..models import Journal, JournalEntry


@pytest.fixture
def user() -> User:
    return User.objects.create_user("test-user", password="my-pw")


@pytest.fixture
def journal(user) -> Journal:
    return Journal.objects.create(author=user)


@pytest.mark.django_db
def test_creates_journal_for_user_if_it_doesnt_exist_yet(client, user):
    client.login(username="test-user", password="my-pw")

    resp = client.get("/journal/")
    assert resp.status_code == 200

    assert Journal.objects.filter(author=user.id).exists()


@pytest.mark.django_db
def test_creates_journal_entry_upon_successful_submission(client, journal):
    client.login(username="test-user", password="my-pw")

    data = {"journal_id": journal.id, "feeling": "good"}
    resp = client.post(f"/journal/{journal.id}/entry/new", data=data)

    entry = JournalEntry.objects.get(journal_id=journal.id)
    observation = entry.observation_set.first()

    assert observation.feeling == "good"
    assert resp.status_code == 302
    assert resp.url == f"/journal/entry/{entry.id}/feelings"
