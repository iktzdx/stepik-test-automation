def test_input_text(expected, actual):
    assert expected == actual, f"expected {expected}, got {actual}"

test_input_text(8, 11)
test_input_text(11, 11)
test_input_text(11, 15)
