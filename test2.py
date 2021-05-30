import my_code

def test_my_code(capsys):
    input_value = ["Algebra"]

    def mock_input(s):
        return input_value.pop(0)

    my_code.input = mock_input

    my_code.fix_errors()

    out, err = capsys.readouterr()

    assert out == 'I love Algebra!\n'
    assert err == ''
