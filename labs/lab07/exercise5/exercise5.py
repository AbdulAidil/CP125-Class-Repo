'''def find_at_risk_departments(departments, threshold):
    at_risk = []
    for dept, students in departments.items():
        avg_score = sum(students.values()) / len(students)
        if avg_score < threshold:
            at_risk.append(dept)
    return at_risk

departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))
print(find_at_risk_departments(departments, 70))
print(find_at_risk_departments(departments, 80))'''

def find_at_risk_departments(departments, threshold):
    at_risk = []

    for dept, students in departments.items():

        scores = students.values()
        total_students = len(scores)

        # Count students below threshold
        below_count = 0
        for score in scores:
            if score < threshold:
                below_count += 1

        # Check if more than half are below threshold
        if below_count > total_students / 2:
            at_risk.append(dept)

    at_risk.sort()
    return at_risk


departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}

print(find_at_risk_departments(departments, 65))
print(find_at_risk_departments(departments, 70))
print(find_at_risk_departments(departments, 80))
