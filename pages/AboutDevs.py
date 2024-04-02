import streamlit as st

# Developer information
developers = [
    {
        "name": "Benjamin Lawani",
        "role": "Machine Learning Engineer",
        "photo_url": "benjamin.jpg",
        "bio": "Final Year Software Engineering Student interested in Machine Learning and its applications"
    }
]

# Display developer information
st.title("About the Developers")
st.sidebar.header("About the Developers")

for developer in developers:
    st.write(f"## {developer['name']}")
    st.image(developer["photo_url"], caption=developer["role"], use_column_width=True)
    st.write(developer["bio"])
