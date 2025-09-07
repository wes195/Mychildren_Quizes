import streamlit as st

# Questions and options
ques = [
    "How many elements in periodic table?",
    "How many bones in human body?",
    "What is the hottest planet in solar system?",
    "What is the animal lays biggest egg?",
    "What is the most abundant gas in atmosphere?"
]

options = [
    ("A- 116", "B- 117", "C- 118", "D- 119"),
    ("A- 206", "B- 207", "C- 208", "D- 209"),
    ("A- Mercury", "B- Earth", "C- Jupiter", "D- Venus"),
    ("A- Whale", "B- Crocodile", "C- Elephant", "D- Ostrich"),
    ("A- Nitrogen", "B- Oxygen", "C- Helium", "D- Carbon")
]

ans = ["C", "A", "D", "D", "A"]

# Streamlit app
st.title("Quiz Game")

score = 0
user_answers = []

with st.form("quiz_form"):
    for i, q in enumerate(ques):
        st.write(f"**{i+1}. {q}**")
        choice = st.radio("Choose an option:", options[i], key=i)
        user_answers.append(choice[0])  # just the letter

    submitted = st.form_submit_button("Submit")

if submitted:
    st.subheader("Results")
    for i, q in enumerate(ques):
        correct = ans[i]
        user_choice = user_answers[i]
        if user_choice == correct:
            st.success(f"Q{i+1}: Correct ✅ ({user_choice})")
            score += 1
        else:
            st.error(f"Q{i+1}: Incorrect ❌ (Your answer: {user_choice}, Correct: {correct})")

    final_score = int(score / len(ques) * 100)
    st.write(f"### Your Final Score: {final_score}%")