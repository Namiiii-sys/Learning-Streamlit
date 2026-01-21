import streamlit as st

st.set_page_config(page_title="CSS Playground", layout="wide")

# ---------- LOAD CSS ----------
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
       background: linear-gradient(135deg, #880808, #EE4B2B);
    }


    /* Custom title */
    .custom-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* Card styling */
    .card {
        background: white;
        color: black;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton>button {
        background-color: #6366f1;
        color: white;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #4f46e5;
        transform: scale(1.03);
    }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background-color: #f9fafb;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    /* Hide footer */
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- UI ----------
st.markdown('<div class="custom-title">CSS Playground</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Mess with styles, break things, learn.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Users", "1,024")
col2.metric("Revenue", "$12.4k")
col3.metric("Growth", "18%")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">This is a custom card.<br>Change padding, color, radius.</div>', unsafe_allow_html=True)
    st.button("Primary Action")

with col2:
    st.markdown('<div class="card">Try gradients, shadows, fonts here.</div>', unsafe_allow_html=True)
    st.text_input("Styled Input")

st.markdown("<br>", unsafe_allow_html=True)

with st.expander("Raw Data (Styled)"):
    st.dataframe(
        {"A": [1, 2, 3], "B": [4, 5, 6]},
        use_container_width=True
    )
