from disk import Disk


def test_constructor():
    dc = Disk(1, 2, 0)
    assert dc.row == 1
    assert dc.column == 2
    assert dc.color == 0
