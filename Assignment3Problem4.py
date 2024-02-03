# Problem # 4
def compute_rewards_and_dollar_value(points, redemption_code):
    if redemption_code.lower() == 'c':
        rewards_points = 2 * points
    elif redemption_code.lower() == 'x':
        rewards_points = 3 * points
    else:
        rewards_points = 1.5 * points

    dollar_value = 1.50 * rewards_points


    return rewards_points, dollar_value

points = int(input("Enter the number of points: "))
redemption_code = input("Enter the redemption code: ")

rewards_points, dollar_value = compute_rewards_and_dollar_value(points, redemption_code)

print("Points entered:", points)
print("Redemption code entered:", redemption_code)
print("Rewards points:", rewards_points)
print("Dollar value: $", dollar_value)
