import pandas as pd
def explore_data(filename):
    df = pd.read_csv(filename)
    # Total students (number of rows)
    total_students = len(df)
    
    # Subjects (only specific columns)
    subjects = ["Math", "Science", "English"]
    
    # Math average (rounded to 1 decimal)
    math_average = df["Math"].mean()
    
    # Student with highest Math score
    highest_math_student = df.loc[df["Math"].max(), ["Name"]]
    
    # 3. Return dictionary
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }

result = explore_data("labs/lab09/data/students.csv")
print(result)
