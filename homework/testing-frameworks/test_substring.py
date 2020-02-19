def test_substring(full_string, substring):
    assert str(substring) in str(full_string), \
            f'expected \'{substring}\' to be substring of \'{full_string}\''

#test_substring('fulltext', 'some_value')
#test_substring('some_text', 'some')
test_substring(1, 1)
