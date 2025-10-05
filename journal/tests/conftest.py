import pytest

from django.contrib.auth.models import User
from ..models import Journal


@pytest.fixture
def user() -> User:
    return User.objects.create_user("test-user", password="my-pw")


@pytest.fixture
def authenticated_client(user, client):
    client.login(username="test-user", password="my-pw")
    return client


@pytest.fixture
def journal(user) -> Journal:
    journal = Journal.objects.create(author=user)

    return journal
