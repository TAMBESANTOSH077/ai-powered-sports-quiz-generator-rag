import streamlit as st
from src.database import initialize_database
from src.generator import generate_quiz

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="🏆 AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide",
)

# -----------------------
# Initialize Database
# -----------------------
initialize_database()

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#2563eb;
}

.sub-title{
    text-align:center;
    color:#94a3b8;
    font-size:18px;
    margin-bottom:25px;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    background:#2563eb;
    color:white;
}

.stButton>button:hover{
    background:#1d4ed8;
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# Header
# -----------------------

st.markdown(
    '<div class="main-title">🏆 AI Sports Quiz Generator</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-title">Generate intelligent sports quizzes using ChromaDB + DuckDuckGo + Gemini AI</div>',
    unsafe_allow_html=True,
)

st.write("")

# -----------------------
# Selection
# -----------------------

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    sport = st.selectbox(
        "🏅 Select Sport",
        [
            "Cricket",
            "Football",
            "Badminton",
            "Basketball",
            "Tennis",
            "Hockey",
        ],
    )

with col2:
    difficulty = st.selectbox(
        "🎯 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard",
        ],
    )

with col3:
    st.write("")
    st.write("")
    generate = st.button("🚀 Generate")

st.divider()

# -----------------------
# Technology Cards
# -----------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        label="📂 Knowledge Base",
        value="ChromaDB",
    )

with c2:
    st.metric(
        label="🌐 Live Search",
        value="DuckDuckGo",
    )

with c3:
    st.metric(
        label="🤖 AI Model",
        value="Gemini 2.5 Flash",
    )

st.divider()

# -----------------------
# Session State
# -----------------------

if "quiz" not in st.session_state:
    st.session_state.quiz = ""

if "context" not in st.session_state:
    st.session_state.context = ""

# -----------------------
# Generate
# -----------------------

if generate:

    with st.spinner("Generating AI Quiz..."):

        quiz, context = generate_quiz(
            sport,
            difficulty,
        )

        st.session_state.quiz = quiz
        st.session_state.context = context

# -----------------------
# Output
# -----------------------

if st.session_state.quiz:

    st.success("✅ Quiz Generated Successfully!")

    st.subheader("📝 Generated Quiz")

    st.code(
        st.session_state.quiz,
        language="text",
    )

    st.download_button(
        "📥 Download Quiz",
        st.session_state.quiz,
        file_name="sports_quiz.txt",
    )

    with st.expander("📚 RAG Context Used"):

        st.text(st.session_state.context)

# -----------------------
# Footer
# -----------------------

st.divider()

st.markdown(
    """
<div class="footer">
Built with ❤️ using Python • Streamlit • ChromaDB • DuckDuckGo • Gemini AI
</div>
""",
    unsafe_allow_html=True,
)