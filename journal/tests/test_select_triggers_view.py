from django.template.loader import render_to_string

from ..models import Trigger

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
