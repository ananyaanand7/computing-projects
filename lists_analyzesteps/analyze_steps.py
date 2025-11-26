def total_steps(step_data):
    """Total steps taking in a day"""
    return sum(step_data)

def active_hours(step_data, threshold):
    """Count hours where steps above threshold"""
    count = 0
    for steps in step_data:
         if steps > threshold:
              count += 1
    return count 

def best_hour(step_data):
    """Find the hour with the most steps"""
    max_steps = max(step_data)
    best_hour = step_data.index(max_steps)
    return (best_hour)

def analyze_one_day(step_data):
        print('\tTotal:', total_steps(step_data))
        print('\tActive hours:', active_hours(step_data, 500))
        print('\tBest hour:', best_hour(step_data))

def main():
    step_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 551, 1764, 1259, 253, 4470, 4919, 1905, 1038, 14, 606, 56, 782, 1132, 918, \
                 39, 0, 27, 0, 0, 0, 0, 0, 6, 73, 2850, 4854, 24, 118, 19, 510, 510, 96, 4100, 1756, 477, 147, 214, 1286, \
                 54, 53, 0, 0, 0, 0, 0, 53, 212, 2832, 43, 220, 181, 12, 44, 205, 152, 226, 516, 559, 1104, 252, 0, 3305]
    n_hours = 24
    for i in range(len(step_data) // n_hours):
        print(f'Analyze day {i+1}:')
        curr_day = step_data[i*n_hours:i*n_hours+n_hours]
        analyze_one_day(curr_day)

if __name__ == '__main__':
    main()
