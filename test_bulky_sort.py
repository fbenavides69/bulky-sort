from bulky_sort import sort


def test_standard_packages():
    assert sort(10, 10, 10, 1) == "STANDARD"
    assert sort(100, 100, 9, 19) == "STANDARD"


def test_special_packages():
    assert sort(10, 10, 10, 20) == "SPECIAL"
    assert sort(160, 10, 10, 1) == "SPECIAL"
    assert sort(10, 160, 10, 1) == "SPECIAL"
    assert sort(10, 10, 160, 1) == "SPECIAL"
    assert sort(150, 100, 100, 10) == "SPECIAL"

def test_rejected_packages():
    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(160, 10, 10, 25) == " REJECTED"
