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