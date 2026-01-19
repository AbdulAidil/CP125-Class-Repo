
def find_largest_drop(readings):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    drop = []
    for i in range (len(readings)-1):
        if readings[i] > readings[i+1]:
            drop_found = readings[i] - readings[i+1]
            drop.append(drop_found)

    if len(drop) == 0:
        return 0.0
    
    largest_drop = max(drop)
    return largest_drop



# Test
readings = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(readings)
print(f"Largest Drop: {result}")  # Expected: 3.5
