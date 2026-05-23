import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="Healthcare RAG Assistant",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Healthcare RAG Assistant")
st.write("Ask healthcare-related questions based on the local knowledge base.")

st.warning(
    "This tool is for educational purposes only. It does not provide medical advice."
)

question = st.text_area(
    "Enter your question",
    placeholder="Example: What lifestyle habits help manage high blood pressure?",
    height=120
)

if st.button("Ask Assistant"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Searching healthcare knowledge base..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("Answer")
                    st.write(data["answer"])

                    st.subheader("Sources")
                    if data["sources"]:
                        for source in data["sources"]:
                            st.write(f"- {source}")
                    else:
                        st.write("No sources returned.")

                    st.subheader("System Info")
                    st.write(f"Route: `{data['route']}`")
                    st.write(f"Latency: `{data['latency_ms']} ms`")

                else:
                    st.error(f"API Error: {response.status_code}")
                    st.code(response.text)

            except requests.exceptions.ConnectionError:
                st.error("FastAPI server is not running. Start it first.")
            except Exception as e:
                st.error("Something went wrong.")
                st.code(str(e))