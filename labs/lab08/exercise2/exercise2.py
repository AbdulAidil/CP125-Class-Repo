# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """ Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names """
    '''result = []
    f = open(file1, "r")
    if lines in f:
        result.append(lines)
    f.close()
    return lines'''

    f = open(file1, "r") 
    f2 = open(file2, "r")
    f3 = open(output_file, "w")

    lines = f.readlines() 
    lines2 = f2.readlines() 

    unique = set(lines + lines2)
    sorted_names = sorted(unique)
    f3.writelines(sorted_names)

    return len(sorted_names)

# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
