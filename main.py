def add_membership_plan(plans, name, cost, available=True):
    plans[name] = {"cost": cost, "available": available}

def add_additional_feature(features, name, cost, available=True):
    features[name] = {"cost": cost, "available": available}

def display_membership_plans(plans):
    print("Available Membership Plans:")
    for name, details in plans.items():
        status = "Available" if details["available"] else "Unavailable"
        print(f"{name} - ${details['cost']} ({status})")

def display_additional_features(features):
    print("Available Additional Features:")
    for name, details in features.items():
        status = "Available" if details["available"] else "Unavailable"
        print(f"{name} - ${details['cost']} ({status})")

def select_membership_plan(plans, plan_name):
    if plan_name in plans and plans[plan_name]["available"]:
        return {"name": plan_name, **plans[plan_name]}
    print(f"Membership plan '{plan_name}' is not available.")
    return None

def select_additional_features(features, feature_names):
    selected_features = []
    for feature_name in feature_names:
        if feature_name in features and features[feature_name]["available"]:
            selected_features.append({"name": feature_name, **features[feature_name]})
        else:
            print(f"Feature '{feature_name}' is not available.")
            return []
    return selected_features

def calculate_total_cost(selected_plan, selected_features):
    total_cost = selected_plan["cost"] if selected_plan else 0
    for feature in selected_features:
        total_cost += feature["cost"]
    return total_cost

def apply_discounts(total_cost):
    discount = 0
    if total_cost > 400:
        discount = 50
    elif total_cost > 200:
        discount = 20
    return total_cost - discount

def apply_premium_surcharge(total_cost):
    return total_cost * 1.15

def confirm_membership(selected_plan, selected_features):
    if not selected_plan:
        print("No membership plan selected.")
        return

    total_cost = calculate_total_cost(selected_plan, selected_features)
    total_cost = apply_discounts(total_cost)
    if any(feature["name"] == "Premium" for feature in selected_features):
        total_cost = apply_premium_surcharge(total_cost)

    print("Membership Confirmation:")
    print(f"Selected Plan: {selected_plan['name']}")
    print("Selected Features:", [feature["name"] for feature in selected_features])
    print(f"Total Cost: ${total_cost:.2f}")

    confirmation = input("Confirm membership plan? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        print("Membership plan confirmed.")
    else:
        print("Membership plan cancelled. Please make your selections again.")
        return None, []

# Example usage
membership_plans = {}
additional_features = {}

# Add membership plans
add_membership_plan(membership_plans, "Basic", 100)
add_membership_plan(membership_plans, "Standard", 200)
add_membership_plan(membership_plans, "Premium", 300)

# Add additional features
add_additional_feature(additional_features, "Pool Access", 50)
add_additional_feature(additional_features, "Personal Trainer", 100)
add_additional_feature(additional_features, "Premium", 200)

# Display available membership plans and additional features
display_membership_plans(membership_plans)
display_additional_features(additional_features)

# Select membership plan and additional features based on user input
selected_plan_name = input("Enter the name of the membership plan you want to select: ").strip()
selected_plan = select_membership_plan(membership_plans, selected_plan_name)

if selected_plan:
    selected_feature_names = input("Enter the names of the additional features you want to select (comma separated): ").strip().split(',')
    selected_feature_names = [name.strip() for name in selected_feature_names]
    selected_features = select_additional_features(additional_features, selected_feature_names)
    if selected_features:
        confirm_membership(selected_plan, selected_features)
