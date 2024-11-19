import pytest
from apostrophe_checker.checker import ApostropheChecker

@pytest.fixture
def checker():
    return ApostropheChecker()

def test_correct_text(checker):
    input_text = "Лукяна п’ять підюний"
    expected = "Лук'яна п’ять під'юний"
    assert checker.correct_text(input_text) == expected

def test_highlight_errors(checker):
    input_text = "Лукяна п’ять підюний"
    expected = "Лук<span style=\"color: red; font-weight: bold;\">я</span>на п’ять під<span style=\"color: red; font-weight: bold;\">ю</span>ний"
    assert checker.highlight_errors(input_text) == expected

def test_empty_text_error(checker):
    with pytest.raises(ValueError, match="Помилка: Текст не введено або він порожній!"):
        checker.correct_text("")

def test_find_errors(checker):
    input_text = "Лукяна підюний"
    errors = checker.find_errors(input_text)
    assert len(errors) > 0
    assert errors[0] == (0, 3, "Лук")
