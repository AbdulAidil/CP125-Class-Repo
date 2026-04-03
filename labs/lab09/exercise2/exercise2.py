import pandas as pd


def compare_averages(filename):
    # Load CSV into DataFrame
    df = pd.read_csv(filename)
    subjects = ["Math", "Science", "English"]
    
    math_mean = df["Math"].mean()
    science_mean = df["Science"].mean()
    english_mean = df["English"].mean()
    
'''    # Calculate mean for each subject, rounded to 1 decimal
    averages = {subj: round(df[subj].mean(), 1) for subj in subjects}
    
    # Identify best and worst subjects
    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)
    
    # Add best/worst to the dictionary
    averages["best_subject"] = best_subject
    averages["worst_subject"] = worst_subject
    
    return averages'''

# Example usage
result = compare_averages("labs/lab09/data/students.csv")
print(result)
