import main 

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

def test_calculate_group_discount():
    users = 2
    membership_cost = 100
    response = main.calculate_group_discount(users, membership_cost)
    assert response == 10

def test_apply_discounts():
    total_cost = 500
    response = main.apply_discounts(total_cost)
    assert response == 450

def test_failed_confirm_membership():
    response = main.confirm_membership("Some Membership", [])
    assert response == -1
