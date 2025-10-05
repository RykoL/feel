import pytest

from django.template.loader import render_to_string

from ..models import Trigger, Journal

from unbrowsed import parse_html, get_by_label_text


def test_renders_one_pill_per_trigger():
    context = {"triggers": [Trigger(name="Family"), Trigger(name="Friends")]}
    rendered_string = render_to_string("journal/entry/select_triggers.html", context)
    print(rendered_string)
    dom = parse_html(rendered_string)

    expected_labels = [
        "Family",
        "Friends",
    ]

    for label in expected_labels:
        get_by_label_text(dom, label)


@pytest.mark.django_db
def test_assigns_triggers_to_observation(authenticated_client, journal: Journal):
    entry = journal.journalentry_set.first()

    data = {"trigger": [1, 2]}
    resp = authenticated_client.post(
        f"/journal/{journal.id}/entry/{entry.id}/triggers", data=data
    )

    assert resp.status_code == 302
    assert resp.url == "/journal/"

    assert entry.observation.triggers.first().id == 1
    assert entry.observation.triggers.last().id == 2
