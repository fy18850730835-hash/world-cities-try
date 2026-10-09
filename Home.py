import streamlit as st

# Page configuration
st.set_page_config(
    page_title="World Cities Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS styling
st.markdown(
    """
    <style>
    .hero-container {
        text-align: center;
        padding: 3rem 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.95;
        margin-bottom: 0;
    }
    .feature-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    .feature-box {
        background: #f0f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .feature-box h3 {
        color: #667eea;
        margin-top: 0;
    }
    .cta-button {
        display: inline-block;
        padding: 0.75rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        margin-top: 1rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hero section
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🌍 World Cities Explorer</div>
        <div class="hero-subtitle">Discover and Analyze Cities Around the Globe</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Welcome text
st.markdown(
    """
    ## Welcome to World Cities Explorer! 👋
    
    This interactive application helps you explore world cities with powerful filtering, 
    visualization, and analytics capabilities. Whether you're researching urban populations, 
    comparing capital cities, or analyzing geographic trends, this tool has everything you need.
    """
)

st.divider()

# Features section
st.markdown("## ✨ What You Can Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### 🗺️ Interactive Maps
        
        View cities plotted on an interactive map and explore their geographic distribution.
        """
    )

with col2:
    st.markdown(
        """
        ### 📊 Population Analytics
        
        Analyze population trends and compare city sizes across countries with charts and data.
        """
    )

with col3:
    st.markdown(
        """
        ### 🔍 Smart Filtering
        
        Filter cities by population, capital status, and country to find exactly what you need.
        """
    )

st.divider()

# Call-to-action section
st.markdown("## 🚀 Get Started")

st.write(
    "Click the button below to explore the cities explorer with filters, maps, and detailed analytics."
)

# Navigation button to app.py
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("📍 Go to City Explorer", use_container_width=True, type="primary"):
        st.switch_page("pages/app.py")

st.divider()

# Footer
st.markdown(
    """
    <div style="text-align: center; color: #888; font-size: 0.9rem; margin-top: 3rem;">
        <p>World Cities Explorer • Built with Streamlit</p>
        <p>Explore. Analyze. Discover.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
