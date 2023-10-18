from project import scramble
from project import accuracy
from project import get_length
import mock
import builtins

def main():
    test_scramble()
    test_accuracy()
    test_get_length()

def test_scramble():
    assert scramble("I am here") == " I ma hree"
    assert scramble("You are here") == " Yuo aer hree"
    assert scramble("He is cute") == " eH si ctue"

def test_accuracy():
    assert accuracy("I am here", "I am here") == 100.0
    assert accuracy("Alexander the Great was an epeltepic", "Alexander the Great was an epileptic") == 83.33
    assert accuracy("In 1945, a seven ocune bathroom cup was the first item Tupperware marketed", "In 1945, a seven ounce bathroom cup was the first item Tupperware marketed") == 92.31

def test_get_length():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert get_length() == 1
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        assert get_length() == 2
    with mock.patch.object(builtins, 'input', lambda _: '3'):
        assert get_length() == 3
    with mock.patch.object(builtins, 'input', lambda _: '10'):
        assert get_length() == 2
    with mock.patch.object(builtins, 'input', lambda _: '-5'):
        assert get_length() == 2





if __name__ == "__main__":
    main()