# Kirill M12P4 10/22/2026

# Creaing list of platers names and batting average
players_name = ['Tom', 'Bob', 'Ben', 'Peter', 'Parker', 'Sam', 'Josh', 'John', 'Wilson', 'Davis']
batting_average = [0.285, 0.312, 0.245, 0.290, 0.330, 0.265, 0.220, 0.305, 0.275, 0.295]

# Define function display_both
def display_both(name, average):
    print()
    print("Players list")
# Display both arrays by using zip to combine them
    for name, average in zip(name, average):
        print(f"Last names: {name} | Exam score: {average}")

# Define function search_player for searching specific player
def search_player(names, averages, target_name):
    found = False 

# Using for loop for finding specific player based on his index
    for i in range(len(names)):
        if names[i].lower() == target_name.lower():
            print(f"Founded: Last name: {names[i]} | Batting Average: {averages[i]}")
            found = True
            break

# Calling for function display_both
display_both(players_name, batting_average)

# While loop for continue or not searching user
while True: 
    user_search = input("Enter last name to search: ")

# Break program if enter space
    if user_search == " ":
        break

# Calling for function search_player
    search_player(players_name, batting_average, user_search)