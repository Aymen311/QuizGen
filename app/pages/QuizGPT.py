import streamlit as st
import openai
import json

@st.cache_data
def generate_quiz(topic, num_questions):
    Quiz = {"questions": [], "answers": [] , "propositions": []}
    # API call    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate in the below format, "+ str(num_questions) +" questions quiz about "+ topic +" by giving 4 propositions and showing the correct answers. A question might have multiple solutions.\nExample:\nQ1. question_text?\nA. PropositionQ1_1\nB. PropositionQ1_2 \nC. PropositionQ1_3 \nD. PropositionQ1_4\nAnswerQ1: PropositionQ1_2.",
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    questions = response.choices[0].text.strip().split("\n\n")
    questions = [question.split("\n") for question in questions]
    for i in range(0, len(questions)):
        Quiz["questions"].append(questions[i][0])
        Quiz["propositions"].append(questions[i][1:5])
        Quiz["answers"].append(questions[i][-1])
    #Add quizz to json file
    data = json.load(open('./pages/quiz.json'))    
    data["Quizz"].append(Quiz)
    data["topic"].append(topic)
    data["num_questions"].append(num_questions)
    #save quizz to json file
    json.dump(data, open('./pages/quiz.json', 'w'))
    return Quiz


#Set a title for the app
st.title("QuizGPT", "A GPT-3 powered quiz generator app")
st.markdown("## Dynamic generator features")

topics = ["Machine learning", "Quadratic functions", "ANOVA"]

# Create a form for the user to select the topic and number of questions
# topic = st.selectbox("Select a topic", topics)
topic = st.text_input("Select a topic", "Machine learning")
num_questions = st.slider("Select the number of questions", 1, 5)
# Create a button to start the quiz
# start_quiz = st.button("Start Quiz")
if "start_quiz" not in st.session_state:
    st.session_state["start_quiz"] = False

if st.button("Generate Quiz"):
    st.session_state["start_quiz"] = not st.session_state["start_quiz"]

if st.session_state["start_quiz"]:
    quizz = generate_quiz(topic, num_questions)
    print(quizz)
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