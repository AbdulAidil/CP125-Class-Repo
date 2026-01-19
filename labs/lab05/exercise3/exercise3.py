
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    max_jump = 0
    bottle_index = 0
    for i in range (len(traceroute)-1):
        current_latency = traceroute[i][1]
        next_latency = traceroute[i+1][1]
        jump = next_latency - current_latency

        max_latency = traceroute[bottle_index][1]
        next_max_latency = traceroute[bottle_index + 1][1]
        max_jump = next_max_latency - max_latency

        if jump > max_jump:
            bottle_index = i  
        return bottle_index



# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
