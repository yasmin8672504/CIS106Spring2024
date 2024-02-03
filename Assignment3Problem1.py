
# Problem #1
def compute_rewards_points(points, redemption_code):
    if redemption_code.lower() == 'c':
        rewards_points = 2 * points
    elif redemption_code.lower() == 'x':
        rewards_points = 3 * points
    else:
        rewards_points = 1.5 * points

    return rewards_points

points = int(input("Enter the number of points: "))
redemption_code = input("Enter the redemption code: ")

rewards_points = compute_rewards_points(points, redemption_code)

print("Points entered:", points)
print("Redemption code entered:", redemption_code)
print("Rewards points:", rewards_points)
