import sys

extra_features = {}
plans = {}

plans["Basic"] = {"cost": 100, "available": True}
plans["Premium"] = {"cost": 200, "available": True}
plans["Family"] = {"cost": 300, "available": False}

extra_features["Personal training sessions"] = {"cost": 25, "premium": False, "available": True}
extra_features["Group classes"] = {"cost": 30, "premium": False, "available": True}
extra_features["Specialized training programs"] = {"cost": 70, "premium": True, "available": True}
extra_features["Pool Access"] = {"cost": 60, "premium": True, "available": False}

def show_elements(elements_list, reference_dictionary):
    for index, element in enumerate(elements_list):
        option_number = index + 1
        element_cost = reference_dictionary[element]["cost"]
        print(f"{option_number}. {element} ${element_cost}")

def calculate_base_cost(plan):
    return plans[plan]["cost"]

def calculate_features_cost(features):
    extra_cost = 0
    for feature in features:
        extra_cost += extra_features[feature]["cost"]
    return extra_cost

def calculate_total_cost(plan, features):
    return calculate_base_cost(plan) + calculate_features_cost(features)

def calculate_group_discount(group_size, membership_cost):
    discount = 0
    if group_size >= 2:
        discount = 0.10 * membership_cost
    return discount

def calculate_special_discount(total_cost):
    discount = 0
    if total_cost > 400:
        discount = 50
    elif total_cost > 200:
        discount = 20
    return discount

def calculate_premium_surcharge(total_cost):
    return total_cost * 0.15

def check_availability(plan, features):
    is_available_plan = plans[plan]["available"]
    are_available_features = True
    for feature in features:
        is_available_feature = extra_features[feature]["available"]
        are_available_features = are_available_features and is_available_feature
    return is_available_plan and are_available_features

def validate_features(user_input, features):
    options = user_input.strip().split(",")
    option_numbers = []
    for option in options:
        valid_option = validate_option(option, features)
        option_numbers.append(valid_option)
    return option_numbers

def get_features(premium):
    features = []
    for key, value in extra_features.items():
        if value["premium"] is premium:
            features.append(key)
    return features

def validate_option(user_input, options):
    number = 0
    try:
        number = int(user_input)
        if number > len(options) or number < 1:
            print("ERROR: A non valid option was provided")
            sys.exit(-1)
        return number - 1
    except ValueError:
        print("ERROR: A non numeric option was provided")
        sys.exit(-1)

def validate_group_input(group_size_input):
    try:
        size = int(group_size_input)
        if size < 1:
            print("ERROR: At least one person must subscribe")
            sys.exit(-1)
        return size
    except ValueError:
        print("ERROR: A non numeric option was provided")
        sys.exit(-1)

def apply_discounts(total_cost, *discounts):
    for discount in discounts:
        if total_cost - discount >= 0:
            total_cost -= discount
        else:
            print("ERROR: Invalid total cost calculated")
            sys.exit(-1)
    return total_cost

def apply_surcharge(surcharge, total_cost):
    return total_cost + surcharge

def get_selected_plan(plans_list):
    show_elements(plans_list, plans)
    plan_input = input("Enter the number of the plan that you want: ")
    selected_plan_index = validate_option(plan_input, plans_list)
    return plans_list[selected_plan_index]

def get_selected_basic_features():
    basic_features = get_features(False)
    show_elements(basic_features, extra_features)
    basic_features_input = input("Enter the number of the basic features that you want separated by comma: ")
    selected_basic_features_indexes = validate_features(basic_features_input, basic_features)
    return [basic_features[i] for i in selected_basic_features_indexes]

def get_selected_premium_features():
    premium_features_list = get_features(True)
    show_elements(premium_features_list, extra_features)
    premium_features_input = input("Enter the number of the premium features that you want separated by comma: ")
    selected_premium_features_indexes = validate_features(premium_features_input, premium_features_list)
    return [premium_features_list[i] for i in selected_premium_features_indexes]

def confirm_membership(selected_plan, selected_basic_features, selected_premium_features, group_size, total_cost):
    print("\n--- Membership Summary ---")
    print(f"Selected Plan: {selected_plan}")
    print(f"Selected Basic Features: {', '.join(selected_basic_features)}")
    if selected_premium_features:
        print(f"Selected Premium Features: {', '.join(selected_premium_features)}")
    print(f"Group Size: {group_size}")
    print(f"Total Cost: ${total_cost}")

    confirm = input("Do you confirm the membership? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Membership canceled.")
        return -1

    print("Membership confirmed. Thank you!")
    return total_cost

def main():
    print("Welcome to the Gym Membership Management System")
    plans_list = list(plans.keys())

    selected_plan = get_selected_plan(plans_list)
    selected_basic_features = get_selected_basic_features()

    if not check_availability(selected_plan, selected_basic_features):
        print("ERROR: Selected plan or features are not available")
        sys.exit(-1)

    selected_premium_features = []
    premium_surcharge = 0
    base_cost = calculate_base_cost(selected_plan)
    extra_features_cost = calculate_features_cost(selected_basic_features)
    total_cost = base_cost + extra_features_cost

    if selected_plan == "Premium":
        selected_premium_features = get_selected_premium_features()

        if not check_availability(selected_plan, selected_premium_features):
            print("ERROR: Selected plan or features are not available")
            sys.exit(-1)

        total_cost += calculate_features_cost(selected_premium_features)
        premium_surcharge = calculate_premium_surcharge(total_cost)

    group_size_input = input("Enter the number of persons that will buy the membership: ")
    group_size = validate_group_input(group_size_input)

    special_discount = calculate_special_discount(total_cost)
    group_discount = calculate_group_discount(group_size, total_cost)

    total_cost = apply_discounts(total_cost, special_discount, group_discount)
    total_cost = apply_surcharge(premium_surcharge, total_cost)

    final_cost = confirm_membership(selected_plan, selected_basic_features, selected_premium_features, group_size, total_cost)
    if final_cost == -1:
        return -1

    return final_cost

if __name__ == "__main__":
    main()
