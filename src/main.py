import streamlit as st

# Page config
st.set_page_config(
    page_title="RoI Calculator",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.title("🏭 Rise Of Industry Calculator")
st.subheader(
    "Max out profits, streamline production chains, plan logistics like a tycoon"
)

# Hero section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Welcome to RoICalculator
    
    A scrappy tool to crunch numbers for Rise of Industry. This utility removes all the fun from the game 
    and lets players with OCD cope with the inability of reaching happiness in the most simple tasks.
    
    **What you can do:**
    - 📊 Calculate optimal production chains
    - 📦 Analyze resource requirements  
    - 💰 Maximize profit margins
    - 🚛 Plan efficient logistics
    - 🏭 Simulate factory setups
    - 📈 Model trade routes
    """)

with col2:
    st.info("""
    **Quick Start**
    
    1. Choose a calculator from the sidebar
    2. Input your production data
    3. Get optimized results
    4. Build your industrial empire
    """)

# Main navigation
st.markdown("---")
st.markdown("### 🛠️ Available Tools")

# Tool cards
col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Production Chain Calculator", use_container_width=True):
        st.info("Coming soon! Calculate optimal production chains and resource flows.")

with col2:
    if st.button("💰 Profit Optimizer", use_container_width=True):
        st.info("Coming soon! Maximize your profit margins across different markets.")


# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #666;'>
    <p>Built for Rise of Industry players who want to optimize their industrial empires</p>
</div>
""",
    unsafe_allow_html=True,
)
