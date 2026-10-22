# Kirill M12P2 10/22/2026

# List of last names and exam scores
last_names = ['Smith', 'Garcia', 'Patel', 'Chen', 'Müller', 'Nguyen', 'Rossi', 'Connor', 'Dubois', 'Kim']
exam_scores = [75, 55, 61, 91, 100, 27, 43, 87, 79, 80]

# Define function print_all
def print_all(name, score):
    print()
    print("Students score")
# Printing last_name and exam_scores and use zip for combine them
    for name, score in zip(name, score):
        print(f"Last names: {name} | Exam score: {score}")

# Define function print_all_reversed
def print_all_reversed(name, score):
    print()
    print("Students score reversed")
# Printing last_name and exam_scores, use zip for combine them and reversed them
    for name, score in zip(reversed(name), reversed(score)):
        print(f"Last names: {name} | Exam score: {score}")

# Calling for the function
print_all(last_names, exam_scores)
print_all_reversed(last_names, exam_scores)