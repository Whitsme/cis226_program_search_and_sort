import pytest
import main

def test_main(capsys):
    main.main(1, 7, 4, 2, 9, 8, 10, -4, 0, 3)
    captured = capsys.readouterr()
    assert ("8") in captured.out

# pytest
def test_reg(capsys):
    main.main(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    captured = capsys.readouterr()
    assert ("8") in captured.out

# pytest
def test_rev(capsys):
    main.main(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    captured = capsys.readouterr()
    assert ("8") in captured.out