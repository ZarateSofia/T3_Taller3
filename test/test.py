from .. import main

def test_calculate_total_cost_family():
    membresia = "Family"
    features = ["Personal training sessions"]
    response = main.calculate_total_cost(membresia, features)
    assert response == 325

def test_calculate_total_cost_basic():
    membresia = "Basic"
    features = ["Personal training sessions", "Group classes"]
    response = main.calculate_total_cost(membresia, features)
    assert response == 155

def test_calculate_total_cost_premium():
    membresia = "Premium"
    features = []
    response = main.calculate_total_cost(membresia, features)
    assert response == 200




