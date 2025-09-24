import streamlit as st
import pandas as pd
from datetime import datetime

# --- App Configuration and Title ---
st.set_page_config(page_title="Gender-Based Violence Reporting App", layout="centered")

# --- UI elements and styling ---
st.markdown("""
<style>
    /* General body and container styling */
    .main .block-container {
        padding-top: 2rem;
    }
    .main .st-emotion-cache-1629p29 {
        background-color: #ffe6f2; /* Light pink background */
        border-radius: 1rem;
        padding: 30px;
        box-shadow: 0 4px 12px rgba(219, 112, 147, 0.2); /* Pink shadow */
    }
    
    body {
        font-family: 'Inter', sans-serif;
    }
    
    /* Headers and titles */
    h1 {
        color: #d81b60; /* Deep pink color */
        text-align: center;
        font-weight: bold;
    }
    .subheader {
        color: #555;
        text-align: center;
    }
    h2, h3, h4, h5, h6 {
        color: #d81b60;
        font-weight: bold;
    }
    
    /* Button styling */
    div.stButton > button {
        background-color: #d81b60; /* Pink background */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s, transform 0.3s;
    }
    div.stButton > button:hover {
        background-color: #e91e63; /* Lighter pink on hover */
        transform: translateY(-2px); /* Lift effect on hover */
    }
    
    /* Expander styling */
    div.st-expander {
        background-color: #fff0f5; /* Very light pink */
        border-radius: 10px;
        border: 1px solid #d81b60;
    }
    
    /* Selectbox styling */
    div.stSelectbox > div {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Gender-Based Violence Reporting App", anchor=False)
st.markdown("<h2 class='subheader'>Report an Incident Securely</h2>", unsafe_allow_html=True)

# --- Incident Reporting Form ---
st.header("Report an Incident")
st.markdown("Please provide details of the incident below. All information is confidential.")

with st.form("report_form", clear_on_submit=True):
    # Personal Information Section (Optional, but good practice for a real app)
    with st.expander("Your Information (Optional)", expanded=False):
        name = st.text_input("Your Name (or anonymous)")
        contact_info = st.text_input("Email or Phone Number (for follow-up)")

    # Incident Details Section
    incident_type = st.selectbox(
        "Type of Incident",
        ("Physical Violence", "Sexual Violence", "Psychological/Emotional Abuse", "Economic Abuse", "Online Harassment", "Other")
    )

    date_of_incident = st.date_input("Date of Incident", max_value=datetime.now())
    time_of_incident = st.time_input("Time of Incident")
    
    location_details = st.text_area("Location Details (e.g., city, neighborhood, or specific address)")

    description = st.text_area(
        "Incident Description",
        "Please provide a detailed, factual account of what happened.",
        height=200
    )

    # Submission Button
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        # This is a placeholder for demonstration purposes.
       
        report_data = {
            "name": name if name else "Anonymous",
            "contact_info": contact_info,
            "incident_type": incident_type,
            "date": date_of_incident,
            "time": time_of_incident.strftime("%H:%M"),
            "location": location_details,
            "description": description,
            "timestamp": datetime.now()
        }

        st.success("Thank you for your report. It has been submitted securely.")
        st.info("Please note: For immediate help, contact your local emergency services or a national helpline.")

# --- Placeholder for a dashboard of reports ---
st.markdown("---")
st.subheader("Submitted Reports (Placeholder)")
st.warning("This section is for demonstration. It does not store reports persistently.")

# A placeholder list to show how reports would be displayed.
placeholder_reports = [
    {"ID": "RPT-001", "Type": "Physical Violence", "Date": "2024-01-15"},
    {"ID": "RPT-002", "Type": "Psychological Abuse", "Date": "2024-02-28"},
    {"ID": "RPT-003", "Type": "Sexual Violence", "Date": "2024-03-10"},
]

df_placeholder = pd.DataFrame(placeholder_reports)
st.dataframe(df_placeholder)
