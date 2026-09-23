
def update_score(current_score):
    new_score = current_score - 10

    if new_score < 0:
        new_score = 0

    return new_score


def get_rating(final_score):
        if final_score >= 80:
            return "Excellent"
        elif final_score >= 50:
            return "Good"
        else:
            return "Keep Practicing"

if __name__ == "__main__":
    score = 100

    score = update_score(score)
    print(f"Score ater incorrect guess: {score}")

    print(f"Rating: {get_rating(score)}")