import streamlit as st

# Developer information
developers = [
    {
        "name": "Benjamin Lawani",
        "role": "Machine Learning Engineer",
        "photo_url": "benjamin.jpg",
        "bio": "Final Year Software Engineering Student interested in Machine Learning and its applications"
    },
    {
        "name": "Ayoola Oluwatorera",
        "role": "Software Engineer",
        "photo_url": "torera.jpg",
        "bio": "Software Engineering Student who is interested in Java and mobile development."
    }
]

# Display developer information
st.title("About the Developers")
st.sidebar.header("About the Developers")

for developer in developers:
    st.write(f"## {developer['name']}")
    st.image(developer["photo_url"], caption=developer["role"], use_column_width=True)
    st.write(developer["bio"])

st.write("\n")

st.write("""*THIS PROJECT WAS SUBMITTED TO THE DEPARTMENT OF SOFTWARE ENGINEERING, SCHOOL OF COMPUTING AND ENGINEERING SCIENCES,  BABCOCK UNIVERSITY, ILISHAN-REMO, OGUN.*

*IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF A BACHELOR OF SCIENCE(BSC) DEGREE IN SOFTWARE ENGINEERING.*

*UNDER THE SUPERVISION OF*

*Mr ADEOTI B. E*

*March, 2024*""")