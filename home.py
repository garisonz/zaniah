import streamlit as st

# Page config (wide for better hero layout)
st.set_page_config(page_title="Zaniah", layout="wide")

# Custom CSS for layout tightening, hero styling, and hiding default Streamlit elements
st.markdown("""
<style>


    /* Reduce padding around the main content */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 90rem;  /* Limits max width for readability on large screens */
    }

    /* Make the hero row tall enough for proper centering */
    .stColumns > div > div > div {
        min-height: 80vh;
    }

    /* Hero section styling */
    .hero {
        display: flex;
        flex-direction: column;
        justify-content: center;  /* Vertical centering */
        height: 100%;  /* Fill the column height */
        padding: 2rem 0;
    }

    .hero-title {
        font-size: 4rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #010101;  
    }

    .hero-subtitle {
        font-size: 1.5rem;
        margin-bottom: 2rem;
        color: #4b5563;  
        max-width: 80%;
    }

    .hero-buttons a {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        margin-right: 1rem;
        text-decoration: none;
        border-radius: 0.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .hero-primary {
        background-color: #010101;    /* Blue primary */
        color: white;
    }

    .hero-primary:hover {
        background-color: #010101;
        transform: translateY(-2px);
    }

    .hero-secondary {
        background-color: transparent;
    }


    /* Image column - make image fill nicely and center vertically */
    .hero-image {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .hero-image img {
        max-height: 80vh;
        max-width: 100%;
        width: auto;
        object-fit: contain;
        border-radius: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Columns with better ratio and explicit vertical centering
left, right = st.columns([0.6, 0.4], vertical_alignment="center", gap="large")

with left:
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Zaniah</div>
        <div class="hero-subtitle">
            Make informed decisions with a unified view of U.S. equities and macroeconomic signals.
        </div>
        <div class="hero-buttons">
            <a class="hero-primary" href="#stock-analysis" target="_self">Explore the Dashboard</a>
            <a class="hero-secondary" href="#about" target="_self">View Methodology</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="hero-image">', unsafe_allow_html=True)
    st.image("assets/hero_image.png", width='content')  # Let CSS handle sizing
    st.markdown('</div>', unsafe_allow_html=True)