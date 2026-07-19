import streamlit as st

 st.set_page_config(page_title="Harvester Technician App")

 st.title("Harvester Technician Performance Tracking App")

 st.success("App deployed successfully!")

 st.write("Welcome to the Harvester Technician Dashboard")

 visit_type = st.selectbox(
  "Select Visit Type",
    [
        "Dealership Visit",
        "Customer Complaint",
        "Pre-Season Readiness",
        "Retrofitment",
        "Installation",
        "PDI",
        "Others"
    ]
)

 st.write("Selected:",visit_type)
create app.py
st.write("Selected:", visit_type)
