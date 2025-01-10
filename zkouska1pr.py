# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
    result = []
    for string in strings:
        if string == "STOP":
            break
        if len(string) > 3:
            result.append(string.upper())
    return result


# Pytest testy pro Příklad 2
import pytest
from zkouska1pr import process_strings
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]
    assert process_strings([]) == []
    assert process_strings(["hello"]) == ["HELLO"]

if __name__ == "__main__":
    pytest.main()