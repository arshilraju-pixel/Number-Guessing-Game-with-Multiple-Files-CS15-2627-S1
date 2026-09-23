from utils import generate_secret_number, check_user_guess

from score import update_score, get_rating

def main():
    secret_number = generate_secret_number()
    score = 100

    while True:
        correct = check_user_guess(secret_number)

        if correct:
            print(f"Final score: {score}")
            print(f"Rating: {get_rating(score)}")

        else:
            score = update_score(score)

if __name__ == "__main__":
    main()