import streamlit as st
from PIL import Image


def main():
    st.set_page_config(
        page_title="Jeel's Resume Screener",
        page_icon="📝",
        layout="centered"
    )

    # Custom CSS for modern look
    st.markdown("""
    <style>
    .main-title {
        font-size: 2.8em;
        font-weight: bold;
        text-align: center;
        color: #2563eb;
        margin-bottom: 0.2em;
        margin-top: 0.5em;
    }
    .subtitle {
        font-size: 1.3em;
        text-align: center;
        color: #374151;
        margin-bottom: 2em;
    }
    .feature-list {
        display: flex;
        flex-direction: row;
        justify-content: center;
        gap: 2em;
        margin-bottom: 2em;
    }
    .feature-card {
        background: #1e293b; /* dark slate */
        border-radius: 12px;
        padding: 1.5em 1.2em;
        min-width: 220px;
        box-shadow: 0 2px 8px rgba(30,58,138,0.18);
        text-align: center;
        border: 1px solid #334155; /* darker border */
    }
    .feature-icon {
        font-size: 2em;
        margin-bottom: 0.5em;
        color: #fff; /* white for strong contrast */
    }
    .get-started-btn {
        display: flex;
        justify-content: center;
        margin-top: 2em;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header with icon and title
    st.markdown('<div class="main-title">Jeel\'s Resume Screener</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered tool for fast, accurate, and fair candidate screening</div>',
                unsafe_allow_html=True)

    # Features section
    st.markdown('<div class="feature-list">', unsafe_allow_html=True)
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <b>AI Resume Analysis</b><br>
        Extracts and summarizes key candidate information instantly.
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <b>Smart Ranking</b><br>
        Ranks candidates based on job requirements and skills match.
    </div>
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <b>Privacy First</b><br>
        Your data is processed securely and never shared.
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # How it works
    with st.expander("How does it work?", expanded=False):
        st.markdown("""
        1. **Upload resumes** (PDF format)
        2. **Upload job requirements**
        3. The AI analyzes and matches candidates
        4. Get instant, ranked results and summaries
        """)

    # Get Started button
    st.markdown('<div class="get-started-btn">', unsafe_allow_html=True)
    if st.button("🚀 Get Started", type="primary", use_container_width=True):
        st.switch_page("pages/resumescreener.py")
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
