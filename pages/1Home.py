# pages/2_👨‍💻_About.py
import streamlit as st

def load_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #1f77b4;
            margin-bottom: 2rem;
        }
        .section-header {
            font-size: 2rem;
            font-weight: bold;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
            margin: 2rem 0 1rem 0;
        }
        .skill-badge {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 0.3rem 0.8rem;
            margin: 0.2rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        .project-card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #3498db;
        }
        .metric-card {
            background: linear-gradient(135deg, #167eea 0%, #194ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

def render_home():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## Welcome to my portfolio!")
        st.write("""
        I'm Vebri Satriadi, a passionate Data Engineer with 4+ years of experience in designing, 
        building, and optimizing data pipelines and architectures. 
        I enjoy solving complex data challenges and leveraging cutting-edge 
        tools and platforms to create scalable and efficient solutions.
        """)
        
        st.markdown("### What I've been up to")
        st.write("""
        I've been working on a variety of projects, including:
        - **Data Engineering**: End-to-end data pipeline development, ETL/ELT processes, and data modeling.
        - **Cloud Platforms**: Extensive experience with Google Cloud Platform (GCP) and Amazon Web Services (AWS).
        - **Containerization and Orchestration**: Proficient in Docker and Kubernetes for deploying and scaling data solutions.
        - **Optimization**: Performance tuning for data workflows and system resources.
        """)    
    
    with col2:
        st.markdown("### 🎯 Current Focus")
        st.info("Deep diving into MLOps and DataOps practices to bridge the gap between data engineering and machine learning.")
        
        st.markdown("### 📍 Location")
        st.write("Jakarta Selatan, Indonesia")
        
        st.markdown("### 🌐 Languages")
        st.write("- **Bahasa Indonesia** (Native)")
        st.write("- **English** (Professional)")

    st.markdown("---") 
    st.markdown("### Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card metric-card-1"><h3>4+</h3><p>Years Experience</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card metric-card-2"><h3>20+</h3><p>Projects Completed</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card metric-card-3"><h3>20+</h3><p>Technologies Used</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card metric-card-4"><h3>100TB+</h3><p>Data Processed</p></div>', unsafe_allow_html=True)

render_home()