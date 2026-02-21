import pytest
from grade import calculate_grade

def test_invalid_low():
    assert calculate_grade(-1) == "Invalid Score"

def test_invalid_high():
    assert calculate_grade(101) == "Invalid Score"

def test_grade_A():
    assert calculate_grade(90) == "A"

def test_grade_A_boundary():
    assert calculate_grade(80) == "A"

def test_grade_B():
    assert calculate_grade(75) == "B"

def test_grade_B_boundary():
    assert calculate_grade(70) == "B"

def test_grade_C():
    assert calculate_grade(65) == "C"

def test_grade_C_boundary():
    assert calculate_grade(60) == "C"

def test_grade_D():
    assert calculate_grade(55) == "D"

def test_grade_D_boundary():
    assert calculate_grade(50) == "D"

def test_grade_F():
    assert calculate_grade(40) == "F"

def test_grade_F_boundary():
    assert calculate_grade(0) == "F"