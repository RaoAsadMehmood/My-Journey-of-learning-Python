# import streamlit as st
# import random 
# import time

# st.title("Quiz Application")

# questions = [
#     {
#         "question": "What is the capital of Pakistan?",
#         "options": ["Karachi", "Lahore", "Peshawar", "Islamabad"],
#         "answer": "Islamabad",
#     },
#     {
#         "question": "In which year did Pakistan gain independence?",
#         "options": ["1945", "1946", "1947", "1948"],
#         "answer": "1947",
#     },
#     {
#         "question": "Who was the first Governor-General of Pakistan?",
#         "options": ["Liaquat Ali Khan", "Muhammad Ali Jinnah", "Iskander Mirza", "Khawaja Nazimuddin"],
#         "answer": "Muhammad Ali Jinnah",
#     },
#     {
#         "question": "Which historical event is known as 'The Great Divide' in Pakistani history?",
#         "options": ["Independence Day", "Partition of Bengal", "Separation of East Pakistan", "Creation of Bangladesh"],
#         "answer": "Creation of Bangladesh",
#     },
#     {
#         "question": "Who is known as 'Poet of the East' (Shaair-e-Mashriq) in Pakistan?",
#         "options": ["Faiz Ahmad Faiz", "Allama Iqbal", "Ahmed Faraz", "Mirza Ghalib"],
#         "answer": "Allama Iqbal",
#     },
#     {
#         "question": "Which important resolution in 1940 demanded a separate homeland for Muslims of British India?",
#         "options": ["Delhi Resolution", "Lahore Resolution", "Karachi Resolution", "Lucknow Pact"],
#         "answer": "Lahore Resolution",
#     }
# ]

# # Initialize the current question if not already in session state
# if "current_question" not in st.session_state:
#     st.session_state.current_question = random.choice(questions)

# question = st.session_state.current_question
# st.subheader(question["question"])

# selected_option = st.radio("Choose your answer", question["options"], key="answer")

# if st.button("Submit Answer"):
#     if selected_option == question["answer"]:
#         st.success("✔ Correct!")
#         st.balloons()
#     else:
#         st.error("❌ Incorrect! The correct answer is " + question["answer"])
    
#     time.sleep(2)
    
#     # Select a new random question from the questions list
#     st.session_state.current_question = random.choice(questions)
#     st.rerun()        
    
# st.markdown('<div class="footer"> Made with 🖤 by <a href="https://github.com/RaoAsadMehmood" target="_blank"> Rao Asad Mehmood</a> </div>', unsafe_allow_html=True)




import streamlit as st
import random
import time

# Set page configuration
st.set_page_config(page_title="Pakistan Quiz", page_icon="🇵🇰", layout="centered")

# CSS for better styling
st.markdown("""
    <style>
    .title { color: #2E8B57; font-size: 2.5em; text-align: center; }
    .question { color: #333; font-size: 1.5em; margin: 20px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; }
    .score { font-size: 1.2em; color: #2E8B57; }
    </style>
""", unsafe_allow_html=True)

# Questions database
questions = [
    
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Peshawar", "Islamabad"],
        "answer": "Islamabad",
    },
    {
        "question": "In which year did Pakistan gain independence?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1947",
    },
    {
        "question": "Who was the first Governor-General of Pakistan?",
        "options": ["Liaquat Ali Khan", "Muhammad Ali Jinnah", "Iskander Mirza", "Khawaja Nazimuddin"],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which historical event is known as 'The Great Divide' in Pakistani history?",
        "options": ["Independence Day", "Partition of Bengal", "Separation of East Pakistan", "Creation of Bangladesh"],
        "answer": "Creation of Bangladesh",
    },
    {
        "question": "Who is known as 'Poet of the East' (Shaair-e-Mashriq) in Pakistan?",
        "options": ["Faiz Ahmad Faiz", "Allama Iqbal", "Ahmed Faraz", "Mirza Ghalib"],
        "answer": "Allama Iqbal",
    },
    {
        "question": "Which important resolution in 1940 demanded a separate homeland for Muslims of British India?",
        "options": ["Delhi Resolution", "Lahore Resolution", "Karachi Resolution", "Lucknow Pact"],
        "answer": "Lahore Resolution",
    },
    # New questions added below
    {
        "question": "What is the highest mountain peak in Pakistan?",
        "options": ["Nanga Parbat", "K2", "Tirich Mir", "Rakaposhi"],
        "answer": "K2"
    },
    {
        "question": "Which river is known as the lifeline of Pakistan?",
        "options": ["Ravi", "Chenab", "Indus", "Jhelum"],
        "answer": "Indus"
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Punjabi", "Sindhi", "Urdu", "Pashto"],
        "answer": "Urdu"
    },
    {
        "question": "Which city is known as the 'City of Lights' in Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Faisalabad"],
        "answer": "Karachi"
    },
    {
        "question": "In which year was the Pakistan Constitution of 1973 adopted?",
        "options": ["1971", "1972", "1973", "1974"],
        "answer": "1973"
    },
    {
        "question": "Which Pakistani scientist won the Nobel Prize in Physics in 1979?",
        "options": ["Abdus Salam", "Pervez Hoodbhoy", "Atta-ur-Rahman", "Abdul Qadeer Khan"],
        "answer": "Abdus Salam"
    },
    {
        "question": "What is the name of Pakistan's national flower?",
        "options": ["Rose", "Jasmine", "Sunflower", "Tulip"],
        "answer": "Jasmine"
    },
    {
        "question": "Which province of Pakistan is the largest by area?",
        "options": ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa"],
        "answer": "Balochistan"
    },
    {
        "question": "Who was the first female Prime Minister of Pakistan?",
        "options": ["Fatima Jinnah", "Benazir Bhutto", "Hina Rabbani Khar", "Maryam Nawaz"],
        "answer": "Benazir Bhutto"
    },
    {
        "question": "Which Pakistani city is famous for its salt mines?",
        "options": ["Quetta", "Khewra", "Multan", "Peshawar"],
        "answer": "Khewra"
    }
]

def initialize_session_state():
    """Initialize session state variables"""
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 0
    if "used_questions" not in st.session_state:
        st.session_state.used_questions = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = None

def get_new_question():
    """Get a new question that hasn't been used yet"""
    available_questions = [q for q in questions if q not in st.session_state.used_questions]
    if not available_questions:
        return None
    return random.choice(available_questions)

# Main application
def main():
    initialize_session_state()
    
    # Header
    st.markdown('<div class="title">Pakistan History Quiz 🇵🇰</div>', unsafe_allow_html=True)
    
    # Score display
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="score">Score: {st.session_state.score}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="score">Questions: {st.session_state.total_questions}/{len(questions)}</div>', 
                   unsafe_allow_html=True)

    # Get or set current question
    if not st.session_state.current_question or st.session_state.current_question in st.session_state.used_questions:
        new_question = get_new_question()
        if new_question:
            st.session_state.current_question = new_question
        else:
            st.success("Quiz Completed! You've answered all questions!")
            st.write(f"Final Score: {st.session_state.score}/{len(questions)}")
            if st.button("Restart Quiz"):
                st.session_state.score = 0
                st.session_state.total_questions = 0
                st.session_state.used_questions = []
                st.session_state.current_question = None
                st.rerun()
            return

    # Display question
    question = st.session_state.current_question
    st.markdown(f'<div class="question">{question["question"]}</div>', unsafe_allow_html=True)
    
    # Options and submission
    with st.form(key='quiz_form'):
        selected_option = st.radio("Choose your answer:", 
                                 question["options"], 
                                 key=f"answer_{st.session_state.total_questions}")
        submit_button = st.form_submit_button(label="Submit Answer")
        
        if submit_button:
            st.session_state.total_questions += 1
            st.session_state.used_questions.append(question)
            
            if selected_option == question["answer"]:
                st.session_state.score += 1
                st.success("✔ Correct!")
                st.balloons()
            else:
                st.error(f"❌ Incorrect! The correct answer is: {question['answer']}")
            
            time.sleep(1.5)
            st.session_state.current_question = None
            st.rerun()

    # Footer
    st.markdown(
        '<div class="footer">Made with 🖤 by <a href="https://github.com/RaoAsadMehmood" target="_blank">Rao Asad Mehmood</a></div>', 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()