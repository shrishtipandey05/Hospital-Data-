import pandas as pd
import matplotlib.pyplot as plt

# Hospital Dataset
data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [25, 40, 35, 60, 50, 22, 45, 55],
    "Gender": ["Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male"],
    "Department": ["Cardiology", "Neurology", "Orthopedic",
                   "Cardiology", "Neurology", "ENT",
                   "Orthopedic", "Cardiology"],
    "Admission_Month": ["January", "January", "February",
                        "February", "March", "March",
                        "April", "April"],
    "Bill_Amount": [5000, 7000, 4500, 9000,
                    6000, 3000, 5500, 8000]
}

df = pd.DataFrame(data)

# Display Hospital Data
print("HOSPITAL DATA")
print(df)

# Total Patients
print("\nTotal Patients:", len(df))

# Average Age
print("Average Patient Age:", df["Age"].mean())

# Gender Analysis
print("\nGender Distribution:")
print(df["Gender"].value_counts())

# Department Analysis
print("\nDepartment Wise Patients:")
print(df["Department"].value_counts())

# Total Hospital Revenue (sample bills)
print("\nTotal Bill Amount:", df["Bill_Amount"].sum())

# Department Graph
df["Department"].value_counts().plot(
    kind="bar",
    title="Department Wise Patients"
)

plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Gender Pie Chart
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Gender Distribution"
)

plt.ylabel("")
plt.show()

# Age Group Analysis

def age_group(age):
    if age <= 18:
        return "0-18"
    elif age <= 30:
        return "19-30"
    elif age <= 45:
        return "31-45"
    elif age <= 60:
        return "46-60"
    else:
        return "Above 60"

df["Age_Group"] = df["Age"].apply(age_group)

print("\nAge Group Analysis:")
print(df["Age_Group"].value_counts())

# Age Group Graph
df["Age_Group"].value_counts().sort_index().plot(
    kind="bar",
    title="Patients by Age Group"
)

plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Age Group Analysis

def age_group(age):
    if age <= 18:
        return "0-18"
    elif age <= 30:
        return "19-30"
    elif age <= 45:
        return "31-45"
    elif age <= 60:
        return "46-60"
    else:
        return "Above 60"

df["Age_Group"] = df["Age"].apply(age_group)

print("\nAge Group Analysis:")
print(df["Age_Group"].value_counts())

# Age Group Graph
df["Age_Group"].value_counts().sort_index().plot(
    kind="bar",
    title="Patients by Age Group"
)

plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Monthly Patient Analysis

monthly_patients = df["Admission_Month"].value_counts()

month_order = ["January", "February", "March", "April"]

monthly_patients = monthly_patients.reindex(month_order)

print("\nMonthly Patient Admissions:")
print(monthly_patients)

monthly_patients.plot(
    kind="line",
    marker="o",
    title="Monthly Hospital Admissions"
)

plt.xlabel("Month")
plt.ylabel("Number of Patients")
plt.grid(True)
plt.tight_layout()
plt.show()
