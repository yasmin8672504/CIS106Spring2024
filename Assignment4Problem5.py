# Problem # 5
def compute_total_points(score1, score2):
    total_points = (0.6 * score1) + (0.4 * score2)
    return total_points

while True:
    yes_no = input("Do you want to run the program? (yes/no): ").lower()
    if yes_no == 'yes' or yes_no == 'y':
        score1 = float(input("Enter first exam score (0-100): "))
        score2 = float(input("Enter second exam score (0-100): "))
        
        if score1 < 0 or score1 > 100 or score2 < 0 or score2 > 100:
            print("Invalid entry. Scores must be within the range of 0 to 100.")
            continue
        
        total_points = compute_total_points(score1, score2)
        print("Total points:", total_points)

    else:
        print("Exiting the program.")
        break