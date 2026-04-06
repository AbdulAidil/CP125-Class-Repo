import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)
    avg_performance = round(df['PerformanceScore'].mean(), 1)
    min_years = 2
    
    condition = (df['PerformanceScore'] > avg_performance) & (df['YearsOfService'] >= min_years)
    qualified_df = df[condition]
    
    candidate_names = set(qualified_df['EmployeeName'])
    candidate_count = len(candidate_names)
    
    return {
        "average_performance": avg_performance,
        "min_years_required": min_years,
        "candidate_count": candidate_count,
        "candidate_names": candidate_names
    }

result = promotion_candidates("labs/lab09/data/employees.csv")
print(f"average_performance: {result["average_performance"]}")
print(f"min_years_required: {result["min_years_required"]}")
print(f"candidate_count: {result["candidate_count"]}")
print(f"candidate_names: {result["candidate_names"]}")

# result = promotion_candidates("labs/lab09/data/employees.csv")
# print(result)
