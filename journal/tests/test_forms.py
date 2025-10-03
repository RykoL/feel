from ..forms import NewJournalEntryForm


def test_new_journal_entry_form_returns_error_if_feeling_is_invalid():
    data = {
        'journal_id': 1,
        'feeling': 'gOd'
    }
    form = NewJournalEntryForm(data=data)
    assert not form.is_valid()
