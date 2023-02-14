import streamlit as st
import openai
import random

import json

#load quizz data from json file
data = json.load(open('../app/quiz.json'))


#Set a title for the app
st.title("QuizGen", "A quiz generator app")
st.markdown("## Static generator feature")

topics = ["Machine learning", "Quadratic functions", "ANOVA"]

# Create a form for the user to select the topic and number of questions
topic = st.selectbox("Select a topic", topics)
num_questions = st.slider("Select the number of questions", 1, 10)
quizz = data["Quizz"][random.randint(0, len(data["Quizz"])-1)]
# Create a button to start the quiz
# start_quiz = st.button("Start Quiz")
if "start_quiz" not in st.session_state:
    st.session_state["start_quiz"] = False

if st.button("Start Quiz"):
    st.session_state["start_quiz"] = not st.session_state["start_quiz"]

if st.session_state["start_quiz"]:
    #Display the quiz questions and multiple choice answers
    st.markdown(f"## {topic} Quiz")

    for i, question in enumerate(quizz["questions"]):
        st.write(f"### {question}")
        #write propositions
        for j, proposition in enumerate(quizz["propositions"][i]):
            st.write(f"- {proposition}")
            
        # Add a button to show the correct answer
        if "show_answer"+str(i) not in st.session_state:
            st.session_state["show_answer"+str(i)] = False
        if st.session_state["start_quiz"]:
            if st.button("Show/Hide answer", key=str(i)):
                st.session_state["show_answer"+str(i)] = not st.session_state["show_answer"+str(i)]
        
        if st.session_state["show_answer"+str(i)]:
            # Retrieve the correct answer for the current question
            # (in this example, we'll just use the first answer choice)
            correct_answer = quizz["answers"][i]
            st.markdown(f"**{correct_answer}**")