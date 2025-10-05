import pytest

from django.contrib.auth.models import User
from ..models import Journal, Observation, JournalEntry, Trigger


@pytest.fixture
def user() -> User:
    return User.objects.create_user("test-user", password="my-pw")


@pytest.fixture
def authenticated_client(user, client):
    client.login(username="test-user", password="my-pw")
    return client


@pytest.fixture
def empty_journal(user) -> Journal:
    journal = Journal.objects.create(author=user)

    return journal


@pytest.fixture
def journal(user, empty_journal):
    Trigger.objects.create(name="Family")
    Trigger.objects.create(name="Friends")
    entry = JournalEntry.objects.create(journal=empty_journal)

    Observation.objects.create(feeling="good", journal_entry=entry)
    return empty_journal
