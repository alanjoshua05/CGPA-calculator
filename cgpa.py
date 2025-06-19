import streamlit as st

# Function to calculate GPA
def calculate_gpa(grades, credit_hours):
    total_grade_points = sum(grade * credit for grade, credit in zip(grades, credit_hours))
    total_credit_hours = sum(credit_hours)
    gpa = total_grade_points / total_credit_hours
    return gpa


# Streamlit app layout
st.title("GPA Calculator")
num_courses = st.number_input("Number of Courses", min_value=1, step=1, value=1)

grades = []
credit_hours = []

for i in range(num_courses):
    st.header(f"Subject {i+1}")
    grade = st.number_input(f"Grade Point", min_value=0, max_value=10, step=1, key=f"grade_{i}")
    credit = st.number_input(f"No.of credit", min_value=1, step=1, key=f"credit_{i}")
    grades.append(grade)
    credit_hours.append(credit)

if st.button("Calculate GPA"):
    gpa = calculate_gpa(grades, credit_hours)
    st.subheader(f"The GPA is: {gpa:.2f}")

