import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/student_performance.csv")

print("\nSTUDENT PERFORMANCE ANALYSIS")
print("--------------------------------")

# Subjects
subjects = ["Math", "Science", "English", "Computer"]

# Calculate Total and Average
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df["Total"] / len(subjects)

# Pass / Fail
df["Result"] = df[subjects].apply(
    lambda row: "Pass" if all(row >= 40) else "Fail",
    axis=1
)

# Grade
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Display result
print(df)

# Top student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Student:")
print(top_student["Name"])
print("Average:", round(top_student["Average"], 2))

# Subject averages
print("\nSubject Averages:")
print(df[subjects].mean())

# Pass / Fail count
print("\nResult Count:")
print(df["Result"].value_counts())

# Save result
df.to_csv("student_performance_result.csv", index=False)

# Chart
df[subjects].mean().plot(kind="bar")
plt.title("Subject Average")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("subject_average.png")
plt.close()

print("\nAnalysis completed successfully!")
print("Result saved in student_performance_result.csv")
