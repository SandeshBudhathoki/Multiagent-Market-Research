
import streamlit as st
from agents.orchestrator import run_research
st.set_page_config(
    page_title="Market Research AI",
    layout="wide"
)


# Style
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(
            circle at top,
            #132238 0%,
            #0B1120 60%
        );
    }

    .block-container {
        max-width: 950px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .title {
        text-align: center;
        color: #F8FAFC;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #94A3B8;
        font-size: 17px;
        margin-bottom: 45px;
    }

    .section-title {
        color: #F8FAFC;
        font-size: 22px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #111C30;
        border: 1px solid #263650;
        border-radius: 14px;
        padding: 20px;
    }

    .stTextInput label {
        color: #E2E8F0 !important;
        font-weight: 600;
    }

    .stTextInput input {
        background: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 9px !important;
        padding: 12px !important;
    }

    div.stButton > button,
    div.stDownloadButton > button {
        border-radius: 9px;
        padding: 10px 18px;
        font-weight: 600;
        width: 100%;
    }

    div.stButton > button[kind="primary"],
    div.stDownloadButton > button {
        background: #2563EB;
        color: white;
        border: none;
    }

    div.stButton > button[kind="primary"]:hover,
    div.stDownloadButton > button:hover {
        background: #1D4ED8;
        color: white;
    }

    div.stButton > button[kind="secondary"] {
        background: #1E293B;
        color: #E2E8F0;
        border: 1px solid #334155;
    }

    div.stButton > button[kind="secondary"]:hover {
        background: #334155;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if "query_input" not in st.session_state:
    st.session_state.query_input = ""

if "report" not in st.session_state:
    st.session_state.report = None

if "report_topic" not in st.session_state:
    st.session_state.report_topic = ""


# Clear previous search
def clear_search():
    st.session_state.query_input = ""
    st.session_state.report = None
    st.session_state.report_topic = ""


# Header
st.markdown(
    '<div class="title">Market Research AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Research companies and industries using a multi-agent AI workflow.'
    '</div>',
    unsafe_allow_html=True
)


# Research input
st.markdown(
    '<div class="section-title">Start Your Research</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    query = st.text_input(
        "Company or Industry",
        key="query_input",
        placeholder="e.g. Daraz Nepal, EV Market in Nepal"
    )

    col1, col2 = st.columns([3, 1])

    with col1:
        start_button = st.button(
            "Start Research",
            type="primary",
            use_container_width=True
        )

    with col2:
        st.button(
            "Clear",
            type="secondary",
            use_container_width=True,
            on_click=clear_search
        )


# Run research
if start_button:

    topic = query.strip()

    if not topic:
        st.warning("Please enter a company or industry.")

    elif len(topic) < 2:
        st.warning("Please enter a valid research topic.")

    elif not any(char.isalpha() for char in topic):
        st.warning("Please enter a topic containing letters.")

    else:
        st.session_state.report = None

        with st.spinner("Researching and preparing your report..."):

            try:
                report = run_research(topic)

                st.session_state.report = report
                st.session_state.report_topic = topic

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# Display research report
if st.session_state.report:

    st.markdown(
        '<div class="section-title">Research Report</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        st.caption(
            f"Research topic: {st.session_state.report_topic}"
        )

        st.markdown(st.session_state.report)

# Download report
    st.download_button(
        label="Download Report",
        data=st.session_state.report,
        file_name="market_research_report.md",
        mime="text/markdown",
        use_container_width=True
    )
