# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):

    f = open("labs/lab08/exercise1/data", "r")
    content = f.read()
    print(content)
    print(type(content))  # <class 'str'>
    f.close()
    
    '''with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            student_id, score = line.split()   
            score = int(score)
            if score >= 80:
                f_out.write(f"{student_id} {score}\n")
                count += 1
    return count'''
result = filter_passing_scores("data/scores.txt", "data/passing.txt")
print(f"Passing students: {result}")
