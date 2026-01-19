import math

def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    mean = sum(times) / len(times)
    variance = 0
    for t in times:
        variance += (t - mean) ** 2
    variance = variance / len(times)
    std_dev = math.sqrt(variance)
    upper_limit = mean + std_dev

    filtered_times = []
    for t in times:
        if t <= upper_limit:
            filtered_times.append(t)
    filtered_times.sort()
    return filtered_times


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")
# Expected: [12, 45, 47, 48, 50, 51, 52]
