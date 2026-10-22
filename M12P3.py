# Kirill M12P3 10/22/2026

# List of last names and exam scores
last_names = ['Smith', 'Garcia', 'Patel', 'Chen', 'Müller', 'Nguyen', 'Rossi', 'Connor', 'Dubois', 'Kim']
exam_scores = [75, 55, 61, 91, 100, 27, 43, 87, 79, 80]

# Define function display
def display(name, score):
    print("Students score")

# Define variables
    high_var = 0
    high_index = 0

    low_var = 999
    low_index = 0

# For loop which goes throught the list and compare it
    for i in range(len(score)):
        if score[i] > high_var:
            high_var = score[i]
            high_index = i

        if score[i] < low_var:
            low_var = score[i]
            low_index = i

# Printing both category of highest and lowest score
    print(f"Highest Score: Last name: {name[high_index]} | Score: {high_var}")
    print(f"Lowest Score: Last name: {name[low_index]} | Score: {low_var}")

# Calling function
display(last_names, exam_scores)