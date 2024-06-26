import pytest
import main 

def test_total_cost_family():
    membresia = "Family"
    features = []
    response = calculateTotal(membresia, features)
    assert response == 2

def test_total_cost_basic():
    membresia = "Basic"
    features = []
    response = calculateTotal(membresia, features)
    assert response == 2

def test_total_cost_premium():
    membresia = "Premium"
    features = []
    response = calculateTotal(membresia, features)
    assert response == 2


def test_special_offer():
    totalCost = 220
    response = calculate_discount(totalCost)
    assert response == 2

def test_especial_offer():
    totalCost = 600
    response = calculate_discount(totalCost)
    assert response == 550

