def get_score():
    score = float(input("Enter score: "))
    return score

def main():
    score = get_score()
    if score < 0 or score > 100:
        print("Invalid score")
    if score >= 50 and score < 90:
        print("Passable")
    elif score >= 90 and score <= 100:
        print("Excellent")
    else:
        print("Bad")

main()
