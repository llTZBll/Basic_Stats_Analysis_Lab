def score_to_gpa(score):
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0

scores = [98, 93, 89, 73, 66]
for s in scores:
    print(f"成绩 {s} -> 绩点 {score_to_gpa(s)}")