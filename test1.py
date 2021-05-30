import my_code

def test_code():
    math = ['Algebra']
    output= []
    def mock_input(s):
        output.append(s)
        return math.pop(0)

    my_code.input = mock_input
    my_code.print = lambda s : output.append(s)

    my_code.fix_errors()
    assert output == ["What math class are you taking? ",
                      'I love Algebra!']

