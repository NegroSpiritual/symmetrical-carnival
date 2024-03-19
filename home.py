import streamlit as st

st.set_page_config(
    page_title="Home Page",
    page_icon="👋",
)

st.write("# Welcome to the Liver Disease Web App! 👋")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    It was used to develop this project.
    **👈 Select a tool from the sidebar** to see the project in action
    
    This project was developed by:

    Lawani Benjamin
    
    Ayoola Oluwatorera 

    in partial fulfillment of the requirements of a BS.c Software Engineering under the supervision of 
    Mr Adeoti B.E.

"""
)