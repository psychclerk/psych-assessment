"""
PG Psychiatry Assessment Framework
Comprehensive psychiatric symptom assessment educational app for medical students.
"""

import streamlit as st
import json
import os

# Page configuration
st.set_page_config(
    page_title="PG Psychiatry Assessment Framework",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional medical education UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    .category-header {
        font-size: 1.5rem;
        font-weight: 500;
        color: #374151;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
    }
    .faculty-pearl {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 4px solid #f59e0b;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .faculty-pearl-title {
        font-weight: 600;
        color: #92400e;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .faculty-pearl-item {
        color: #78350f;
        margin: 0.5rem 0;
        padding-left: 1rem;
    }
    .risk-alert {
        background-color: #fee2e2;
        border-left: 4px solid #dc2626;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .section-title {
        font-weight: 600;
        color: #1f2937;
        margin-top: 1rem;
    }
    .subsection-header {
        font-weight: 500;
        color: #4b5563;
        margin: 0.75rem 0 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load symptoms data
@st.cache_data
def load_symptoms_data():
    """Load symptoms data from JSON file."""
    try:
        with open('data/symptoms.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Symptoms data file not found. Please ensure 'data/symptoms.json' exists.")
        return {}
    except json.JSONDecodeError:
        st.error("Error reading symptoms data. Please check the file format.")
        return {}

# Initialize session state
def init_session_state():
    """Initialize Streamlit session state variables."""
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = None
    if 'selected_symptom' not in st.session_state:
        st.session_state.selected_symptom = None

# Main app
def main():
    init_session_state()
    
    # Load data
    symptoms_data = load_symptoms_data()
    
    if not symptoms_data:
        st.error("Unable to load symptoms data. Please contact administrator.")
        return
    
    # Get categories
    categories = list(symptoms_data.keys())
    
    # Sidebar - Category Selection
    st.sidebar.title("📚 Symptom Categories")
    
    selected_category = st.sidebar.selectbox(
        "Select a Category",
        options=["-- Select Category --"] + categories,
        index=0 if st.session_state.selected_category not in categories else categories.index(st.session_state.selected_category) + 1,
        key="category_select"
    )
    
    # Update session state
    if selected_category != "-- Select Category --":
        st.session_state.selected_category = selected_category
        
        # Get symptoms for selected category
        symptoms = list(symptoms_data[selected_category].keys())
        
        # Symptom Selection
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"### Symptoms in {selected_category}")
        
        selected_symptom = st.sidebar.selectbox(
            "Select a Symptom",
            options=["-- Select Symptom --"] + symptoms,
            index=0 if st.session_state.selected_symptom not in symptoms else symptoms.index(st.session_state.selected_symptom) + 1,
            key="symptom_select"
        )
        
        if selected_symptom != "-- Select Symptom --":
            st.session_state.selected_symptom = selected_symptom
            
            # Get symptom data
            symptom_data = symptoms_data[selected_category][selected_symptom]
            
            # Navigation buttons within category
            st.sidebar.markdown("---")
            st.sidebar.markdown("### Navigate in Category")
            
            col1, col2 = st.sidebar.columns(2)
            current_idx = symptoms.index(selected_symptom)
            
            with col1:
                if st.button("← Previous", key="prev_symptom", disabled=(current_idx == 0)):
                    st.session_state.selected_symptom = symptoms[current_idx - 1]
                    st.rerun()
            
            with col2:
                if st.button("Next →", key="next_symptom", disabled=(current_idx == len(symptoms) - 1)):
                    st.session_state.selected_symptom = symptoms[current_idx + 1]
                    st.rerun()
    
    # Main Content Area
    st.markdown('<div class="main-header">🧠 PG Psychiatry Assessment Framework</div>', unsafe_allow_html=True)
    st.markdown('*Comprehensive psychiatric symptom assessment for postgraduate medical education*')
    
    if st.session_state.selected_symptom and st.session_state.selected_category:
        st.markdown("---")
        
        # Symptom Title
        st.markdown(f'<div class="category-header">{st.session_state.selected_symptom}</div>', unsafe_allow_html=True)
        st.markdown(f"**Category:** {st.session_state.selected_category}")
        
        # Display symptom data
        assessment = symptom_data.get('assessment', {})
        differential = symptom_data.get('differential_diagnosis', {})
        management = symptom_data.get('management', {})
        pearls = symptom_data.get('faculty_pearls', [])
        
        # Assessment Section
        with st.expander("🩺 Assessment", expanded=True):
            st.markdown('<div class="section-title">Clarify Core Symptom</div>', unsafe_allow_html=True)
            st.markdown(assessment.get('clarify_core', 'Not available'))
            
            st.markdown('<div class="subsection-header">Screen for Syndrome</div>', unsafe_allow_html=True)
            st.markdown(assessment.get('screen_for_syndrome', 'Not available'))
            
            st.markdown('<div class="subsection-header">Rule Out Mimics</div>', unsafe_allow_html=True)
            st.markdown(assessment.get('rule_out_mimics', 'Not available'))
            
            st.markdown('<div class="subsection-header">Psychosocial Context</div>', unsafe_allow_html=True)
            st.markdown(assessment.get('psychosocial_context', 'Not available'))
            
            # Risk Assessment with special styling
            risk_text = assessment.get('risk_assessment', 'Not available')
            st.markdown(f"""
            <div class="risk-alert">
                <strong>⚠️ Risk Assessment</strong><br>
                {risk_text}
            </div>
            """, unsafe_allow_html=True)
        
        # Differential Diagnosis Section
        with st.expander("🔍 Differential Diagnosis"):
            st.markdown('<div class="subsection-header">Primary Psychiatric Disorders</div>', unsafe_allow_html=True)
            st.markdown(differential.get('primary_psychiatric', 'Not available'))
            
            st.markdown('<div class="subsection-header">Secondary Diagnoses / Mimics</div>', unsafe_allow_html=True)
            st.markdown(differential.get('secondary_mimics', 'Not available'))
            
            st.markdown('<div class="subsection-header">🚩 Red Flags</div>', unsafe_allow_html=True)
            st.markdown(differential.get('red_flags', 'Not available'))
        
        # Management Section
        with st.expander("💊 Management"):
            st.markdown('<div class="subsection-header">Immediate Priorities</div>', unsafe_allow_html=True)
            st.markdown(management.get('immediate_priorities', 'Not available'))
            
            st.markdown('<div class="subsection-header">Biological Interventions</div>', unsafe_allow_html=True)
            st.markdown(management.get('biological_interventions', 'Not available'))
            
            st.markdown('<div class="subsection-header">Psychological Interventions</div>', unsafe_allow_html=True)
            st.markdown(management.get('psychological_interventions', 'Not available'))
            
            st.markdown('<div class="subsection-header">Social Interventions</div>', unsafe_allow_html=True)
            st.markdown(management.get('social_interventions', 'Not available'))
            
            st.markdown('<div class="subsection-header">Follow-up & Monitoring</div>', unsafe_allow_html=True)
            st.markdown(management.get('follow_up_monitoring', 'Not available'))
        
        # Faculty Pearls Section (always visible as callout)
        st.markdown("---")
        st.markdown('<div class="faculty-pearl-title">💎 Faculty Pearls</div>', unsafe_allow_html=True)
        for pearl in pearls:
            st.markdown(f'<div class="faculty-pearl-item">• {pearl}</div>', unsafe_allow_html=True)
        
        # Quick navigation at bottom
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📖 Return to Top", key="top_button"):
                st.scroll_to(0)
    
    else:
        # Welcome message when no symptom selected
        st.markdown("---")
        st.info("👆 **Select a category from the sidebar, then choose a symptom to view detailed assessment framework.**")
        
        st.markdown("### About This Resource")
        st.markdown("""
        This interactive educational tool provides comprehensive assessment frameworks for 80+ psychiatric symptoms 
        across 11 clinical categories, designed for postgraduate medical education.
        
        **Features:**
        - Structured assessment approach for each symptom
        - Differential diagnosis with red flags
        - Evidence-based management strategies
        - Clinical pearls from psychiatry faculty
        
        **Categories Covered:**
        - Mood & Affect Presentations
        - Anxiety & Fear Presentations
        - Thought Disturbances
        - Behavioral Disturbances
        - Cognitive & Memory Presentations
        - Sleep, Appetite & Somatic Presentations
        - Substance Use & Intoxication
        - Trauma & Dissociation
        - Sexual & Gender Presentations
        - Attention, Impulse Control & Development
        - Miscellaneous Presentations
        """)
        
        st.markdown("---")
        st.caption("© 2024 PG Psychiatry Assessment Framework | Educational Use Only")

if __name__ == "__main__":
    main()
