# Initialize an empty dictionary to store student IDs and their scores
students_data = {}

# Collect IDs and their math, science, and history scores for 5 students
for i in range(5):
    student_id = input(f"Enter the ID of student {i+1}: ")
    math_score = int(input(f"Enter Math score for student {student_id}: "))
    science_score = int(input(f"Enter Science score for student {student_id}: "))
    history_score = int(input(f"Enter History score for student {student_id}: "))
    
    # Store the scores as a tuple (math, science, history) in the dictionary
    students_data[student_id] = (math_score, science_score, history_score)

# Function to calculate the total score for a student
def total_score(scores):
    return sum(scores)

# Print all student IDs whose total score is greater than 100
print("Students with total scores greater than 100:")
for student_id, scores in students_data.items():
    if total_score(scores) > 100:
        print(student_id)