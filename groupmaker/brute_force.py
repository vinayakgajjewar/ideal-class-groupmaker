import random as rnd

def randomize(prefs_dict):
    # Give everyone a random choice, but split it up so that there are an equal
    # number of choices

    # Dict containing the choice given to each student
    results = []

    # To keep track of how many students are assigned each choice
    choice_counter = [0, 0, 0, 0]

    # Each element corresponds to a different student
    num_of_students = len(prefs_dict)

    for student_prefs in prefs_dict:
        given_choice = rnd.randint(1, 4)
        results.append(given_choice)
        # Increment the counter
        choice_counter[given_choice - 1] = choice_counter[given_choice - 1] + 1

    return results
