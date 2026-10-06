import streamlit as st
import ollama

# Page settings
st.set_page_config(
    page_title="AI Employee Helpdesk",
    page_icon="🛠️",
    layout="centered"
)

# Title
st.title("🛠️ AI Employee Helpdesk Assistant")

st.write(
    "Describe your IT problem in your own words. "
    "You don't need to use technical language."
)

# Employee input
problem = st.text_area(
    "What problem are you facing?",
    placeholder="Example: wifi conected bt no net in my laptop",
    height=120
)

# Get AI help
if st.button("🤖 Get AI Help"):

    if problem.strip() == "":
        st.warning("Please describe your problem first.")

    else:

        prompt = f"""
You are an IT helpdesk assistant for a company.

An employee has reported this problem:

"{problem}"

Understand the employee's meaning even if:
- There are spelling mistakes
- There is no punctuation
- The sentence is informal
- The employee uses abbreviations
- The employee does not use technical language

Give a simple and practical response.

Structure your response as:

Problem understood:
Category:
Priority:
Possible cause:

Troubleshooting steps:
1.
2.
3.
4.

When to contact IT:
Explain when the employee should escalate the issue to IT support.

Do not make dangerous changes to the computer or network.
Do not ask the employee to disable security software.
"""

        with st.spinner("🤖 AI is analyzing the problem..."):

            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.subheader("🤖 AI Helpdesk Response")

        st.write(response["message"]["content"])