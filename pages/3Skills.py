# pages/3_🛠️_Skills.py (Versi Final)
import streamlit as st
import plotly.graph_objects as go
from config import SKILLS_DATA, RADAR_CHART_DATA

def render_skills():
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    st.markdown("### Core Competencies")
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=list(RADAR_CHART_DATA.values()),
        theta=list(RADAR_CHART_DATA.keys()),
        fill='toself',
        name='Skill Level',
        line_color='#3498db'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100]), bgcolor="#f8f9fa"),
        showlegend=False, height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Technology Stack")
    
    for category, skills in SKILLS_DATA.items():
        with st.expander(f"**{category}**"):
            badges_html = " ".join([f'<span class="skill-badge-blue">{skill}</span>' for skill in skills])
            st.markdown(badges_html, unsafe_allow_html=True)

render_skills()