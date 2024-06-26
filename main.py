plans = {"Basic":100,"Premium":200,"Family":300}
extraFeatures = {"Personal training sessions":25,"Group classes":30}

def show_plans():
    for index,plan in enumerate(plans.keys()):
        print(str(index)+")",plan)

def calculate_total_cost(plan,extra_features):
    plan_cost = plans[plan]
    extra_cost = 0
    for extra in extra_features:
        extra_cost += extraFeatures[extra]
    return plan_cost + extra_cost

def calculate_group_discount(users,membership_cost):
    discount = 0
    if users >=2:
        discount = 0.10 * membership_cost
    return discount

def calculate_special_discount(total_cost):
    discount = 0
    if total_cost>400:
        discount = 50
    elif total_cost>2:
        discount = 20
    return discount
