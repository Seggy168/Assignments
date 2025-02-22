import streamlit as st

st.title('Student Score tracker')
st.write('Add Score and filter by minimum score.')

# Initialize the session state for 'students' if it doesn't exist
if 'students' not in st.session_state:
    st.session_state['students'] = []

# Create a form to collect student name and score
name = st.text_input('Student name')
score = st.number_input('Score (0 - 100)', min_value=0, max_value=100, value=0)

# Create a button to submit the form
if st.button('Add student'):
    if name:  # Ensure a name is provided
        # Append the student name and score to the list
        st.session_state['students'].append({'name': name, 'score': score})
        st.success(f"Added student: {name}, Score: {score}")
    else:
        st.error("Please enter a valid name.")


# Student Data Table
st.title('Student Data')
students_data = [student for student in st.session_state['students']]
st.table(students_data)

# Create a slider to filter the data by minimum score
st.title('Filter by Minimum Score')
min_score = st.slider('Minimum score', min_value=0, max_value=100, value=0)

# Create a table to preview the data
st.write('Students with scores  > ', min_score)
filtered_students = [student for student in st.session_state['students'] if student['score'] >= min_score]
if filtered_students:
    st.table(filtered_students)
else:
    st.write("No students meet the criteria.")

# Create a button to clear the data
if st.button('Clear'):
    # Clear the students list
    st.session_state['students'] = []
    st.success("All data cleared.")

# Create a button to delete the last student
if st.button('Delete last student'):
    if st.session_state['students']:
        removed_student = st.session_state['students'].pop()
        st.success(f"Removed last student: {removed_student['name']}")
    else:
        st.warning("No students to remove.")
