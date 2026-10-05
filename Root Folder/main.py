from utils import generate_secret_number, check_user_guess
from score import decrease_score, get_rating


secret_number = generate_secret_number()
score = 100

while True:
    if check_user_guess(secret_number):
        rating = get_rating(score)
        print(f"Final score: {score}")
        print(f"Rating: {rating}")
        break
    else:
        score = decrease_score(score)