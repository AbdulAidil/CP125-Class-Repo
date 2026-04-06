'''import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)

    # Filter students with >85 in ALL subjects
    filtered = df[
        (df["Math"] > 85) &
        (df["Science"] > 85) &
        (df["English"] > 85)
    ]

    # Get names as a set
    names = set(filtered["Name"])
    count = len(names)

    return {"\n"
        "count": count,"\n"
        "names": names 
    }

result = high_performers("labs/lab09/data/students.csv")
print(result)'''

import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    filtered = df[
        (df["Math"] > 85) &
        (df["Science"] > 85) &
        (df["English"] > 85) &
        (df["Physics"] > 85) &
        (df["Chemistry"] > 85)]
    
    names = set(filtered["Name"])
    count = len(names)
    return {
        "count": count,
        "names": names 
    }

result = high_performers("labs/lab09/data/students.csv")
print(f"count: {result["count"]}")
print(f"names: {result["names"]}")
