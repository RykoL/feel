from ..forms import NewJournalEntryForm


def test_new_journal_entry_form_returns_error_if_feeling_is_invalid():
    data = {"journal_id": 1, "feeling": "gOOd"}
    form = NewJournalEntryForm(data=data)
    assert not form.is_valid()
    assert form.errors["feeling"] == ["gOOd is not a valid choice"]


def test_new_journal_entry_form_fails_if_no_feeling_is_specified():
    data = {
        "journal_id": 1,
    }
    form = NewJournalEntryForm(data=data)
    assert not form.is_valid()
    assert form.errors["feeling"] == ["This field is required."]


def test_new_journal_entry_form_fails_if_journal_id_is_missing():
    data = {"feeling": "good"}
    form = NewJournalEntryForm(data=data)
    assert not form.is_valid()
    assert form.errors["journal_id"] == ["This field is required."]
