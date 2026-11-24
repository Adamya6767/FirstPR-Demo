import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="FirstPR | AI Open-Source Guide", page_icon="🚀", layout="wide")

# --- Custom CSS for a Modern Look (FORCED LIGHT THEME) ---
st.markdown("""
    <style>
    /* Force background */
    .stApp { background-color: #f4f7f6 !important; }
    
    .main-title { color: #1f3c88 !important; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    
    /* Card styling with forced dark text */
    .issue-card {
        background-color: white !important; 
        padding: 25px; 
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        margin-bottom: 25px;
        border-left: 5px solid #1f3c88;
        color: #333333 !important; /* Force dark text */
    }
    
    /* Force all text inside the card to be dark */
    .issue-card h3, .issue-card p, .issue-card span, .issue-card div, .issue-card b, .issue-card i {
        color: #333333 !important;
    }
    
    .score-badge-high { background-color: #28a745 !important; color: white !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 14px; }
    .score-badge-med { background-color: #ffc107 !important; color: black !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 14px; }
    
    /* File tags */
    .file-tag { background-color: #e9ecef !important; padding: 4px 10px; border-radius: 6px; font-family: monospace; color: #d63384 !important; display: inline-block; margin: 2px; }
    
    /* Roadmap steps */
    .roadmap-step { border-left: 3px solid #1f3c88; padding-left: 15px; margin-bottom: 10px; color: #333333 !important;}
    .roadmap-step code { background-color: #eee !important; color: #d63384 !important; padding: 2px 5px; border-radius: 3px; }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 class='main-title'>🚀 FirstPR</h1>", unsafe_allow_html=True)
st.markdown("### Your AI-Powered Open-Source Contribution Guide")
st.write("Stop searching. Start contributing. We match your skills to the perfect 'good first issue' and explain exactly how to solve it.")

st.divider()

# --- Input Form ---
with st.container():
    st.subheader("1. Build Your Developer Profile")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        skills = st.text_input("Primary Language / Skills", value="Python")
    with col2:
        experience = st.selectbox("Experience Level", ["Absolute Beginner", "Intermediate", "Advanced"])
    with col3:
        time_available = st.selectbox("Time Available", ["1-2 hours", "3-5 hours", "A full weekend"])

    analyze_button = st.button("🔍 Find My Perfect Issue", use_container_width=True, type="primary")

st.divider()

# --- Results Section ---
if analyze_button:
    if not skills:
        st.error("Please enter at least one skill to continue.")
    else:
        # Simulate AI Processing
        with st.spinner("Connecting to GitHub API & scanning repositories..."):
            time.sleep(1)
        with st.spinner("Evaluating issue suitability based on your profile..."):
            time.sleep(1.5)
        with st.spinner("Generating AI contribution roadmap..."):
            time.sleep(1.5)

        st.success("✨ Match Found! Here is your personalized contribution guide.")

        # --- Result 1: High Match ---
        with st.container():
            st.markdown('<div class="issue-card">', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.markdown("### Issue: Add Input Validation to Signup Form", unsafe_allow_html=True)
                st.markdown("**Repo:** `example-org/fastapi-community` | **Labels:** `good first issue`, `help wanted`", unsafe_allow_html=True)
            with col_b:
                st.markdown('<span class="score-badge-high">95% Match</span>', unsafe_allow_html=True)
            
            st.write("---")
            
            st.markdown("#### 🧠 AI Explanation (Plain English)")
            st.info("The signup form currently accepts any text for the email address. If a user types something without an '@' symbol, the database crashes. This task asks you to add a simple Python check to make sure the email looks real before saving it.")
            
            st.markdown("#### 📂 Candidate Files to Inspect")
            st.markdown("<span class='file-tag'>app/api/routes/auth.py</span> <span class='file-tag'>app/schemas/user.py</span> <span class='file-tag'>tests/test_auth.py</span>", unsafe_allow_html=True)
            
            st.markdown("#### 🗺️ Step-by-Step Contribution Roadmap")
            st.markdown("""
            <div class='roadmap-step'><b>1. Fork & Clone:</b> Fork the repo and clone it locally.</div>
            <div class='roadmap-step'><b>2. Setup:</b> Run <code>pip install -r requirements.txt</code>.</div>
            <div class='roadmap-step'><b>3. Code:</b> Open <code>app/schemas/user.py</code> and add a validator to the <code>email</code> field using Pydantic's <code>EmailStr</code>.</div>
            <div class='roadmap-step'><b>4. Test:</b> Go to <code>tests/test_auth.py</code> and write a test that sends an invalid email and expects a 422 error.</div>
            <div class='roadmap-step'><b>5. Submit:</b> Push your code and open a Pull Request!</div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 💡 Concepts to Learn")
            st.markdown("- `Pydantic Data Validation` \n- `HTTP 422 Error Handling`", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Result 2: Medium Match ---
        with st.container():
            st.markdown('<div class="issue-card">', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.markdown("### Issue: Fix Typo in Documentation", unsafe_allow_html=True)
                st.markdown("**Repo:** `example-org/data-tools` | **Labels:** `documentation`", unsafe_allow_html=True)
            with col_b:
                st.markdown('<span class="score-badge-med">80% Match</span>', unsafe_allow_html=True)
            
            st.write("---")
            
            st.markdown("#### 🧠 AI Explanation (Plain English)")
            st.info("The README file has a spelling mistake in the installation section. It says 'instal' instead of 'install'. This is a great way to make your very first open-source contribution without touching any complex code.")
            
            st.markdown("#### 📂 Candidate Files to Inspect")
            st.markdown("<span class='file-tag'>README.md (Line 12)</span>", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👆 Fill out your profile above and click the button to see your AI-matched open-source issues.")
