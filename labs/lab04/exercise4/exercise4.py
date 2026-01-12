
def analyze_performance(lap_times):
    """Analyze lap times to determine if athlete faded in second half."""
    """half_times = len(lap_times) / 2
    total_lap = 0
    for i in range(int(half_times), len(lap_times)):
        total_lap = total_lap + lap_times[i]
        average1 = total_lap / half_times
        
    
    total_lap2 = 0
    for j in range(int(half_times), len(lap_times)):
        total_lap2 = total_lap2 + lap_times[j]
        average2 = total_lap2 / half_times
        return average2"""
    
    n = len(lap_times)
    mid = (n + 1) // 2   # first half larger if odd

    first_half = 0
    for i in range(mid):
        first_half = first_half + lap_times[i]
    average1 = first_half / mid

    second_half = 0
    for i in range(mid, n):
        second_half = second_half + lap_times[i]
    average2 = second_half / (n - mid)

    return average2 > average1

# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
