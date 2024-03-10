import streamlit as st
import pandas as pd

# Personal Information (replace with your details)
name = "Sreeram Nithin"
title = "Business Analyst"
description = "I'm a Hons Data Science Grad working as a Business Analyst and I'm very passionate about Machine Learning, Data Science, Data Analytics and AI"
profile_pic = "C:\\Users\\Nithin\\Downloads\\WhatsApp Image 2024-03-10 at 2.02.52 PM.jpeg"

# Social Media Links (replace with your links)
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/nithin-sreeram-a191a4212/",
    "GitHub": "https://github.com/SreeramNithin",
    "Medium": "https://medium.com/@nithin.sreeram2002",
    # Add more social media links as needed
}

# Logos for social media
linkedin_logo = "C:\\Users\\Nithin\\Downloads\\linkedin_logo.jpg"
github_logo = "C:\\Users\\Nithin\\Downloads\\github_logo.png"
medium_logo = "C:\\Users\\Nithin\\Downloads\\medium_logo1.png"

# Project Information (replace with details of your projects)
projects_info = [
    {
        "title": "Fifa Players Wage Predictor",
        "description": "To combine my passion for data science and love for football as my final year project I made this",
        # "link": "https://www.example.com/project1",  # Optional link to project
        # "image": "path/to/project1_image.jpg",  # Optional image for project 1
    },
    {
        # Add more projects with the same structure
    },
]

# Experience Information (optional, replace with details of your experience)
experiences = pd.DataFrame({
    "Company": ["Lognormal Analytics", "UNP"],
    "Title": ["Business Analyst", "Teaching Assistant"],
    "Dates": ["Start Date 1 - End Date 1", "Start Date 2 - End Date 2"],
    "Description": [
        "Description of experience 1",
        "Description of experience 2",
    ],
})

# Blog Information (optional, replace with blog post summaries)
blog_posts = [
    {
        "title": "Blog",
        "summary": "I post articles and writeups on AI, Data Science, Analytics etc based on my everyday learnings at work and everywhere else.",
        "link": "https://medium.com/@nithin.sreeram2002",  # Optional link to blog post
    },
    {
       "title":"Google Gemini",
       "summary": "How data enthusiasts can use Google Gemini",
       "link":"https://medium.com/@nithin.sreeram2002/google-gemini-everything-you-need-to-know-about-it-as-a-data-professional-a07f096e8389"
    },
]

# Skills Information (replace with your skills)
skills = [
    "Python Programming",
    "Power Bi",
    "Microsoft Excel",
    # Add more skills
]

# Define functions for different sections of the portfolio
def about_me():
    st.header("About Me")
    try:
        st.image(profile_pic, width=150)
    except FileNotFoundError:
        st.error("Profile picture not found. Please check the file path.")
    st.subheader(name)
    st.subheader(title)
    st.write(description, unsafe_allow_html=True)  # Allow basic HTML formatting
    
    # Display LinkedIn, GitHub, and Medium links side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(linkedin_logo, width=50)
        st.markdown(f"[LinkedIn]({social_media['LinkedIn']})", unsafe_allow_html=True)
    with col2:
        st.image(github_logo, width=50)
        st.markdown(f"[GitHub]({social_media['GitHub']})", unsafe_allow_html=True)
    with col3:
        st.image(medium_logo, width=50)
        st.markdown(f"[Medium]({social_media['Medium']})", unsafe_allow_html=True)

def display_projects():
    st.header("Projects")
    for project in projects_info:
        st.subheader(project["title"])
        st.write(project["description"])
        if project.get("link"):
            st.markdown(f"[View Project]({project['link']})")

def experience():
    st.header("Experience")
    st.dataframe(experiences)

def blog():
    st.header("Blog")
    for post in blog_posts:
        st.subheader(post["title"])
        st.write(post["summary"])
        if post.get("link"):
            st.markdown(f"[Read More]({post['link']})")

def display_skills():
    st.header("Skills")
    for skill in skills:
        st.write(f"- {skill}")

def resume():
    st.header("Resume")
    resume_file_path = r"C:\Users\Nithin\Downloads\Sreeram_Nithin.Resume (2).pdf"
    with open(resume_file_path, "rb") as f:
        resume_bytes = f.read()
        st.download_button(
            label="Download Resume",
            data=resume_bytes,
            file_name="Sreeram_Nithin_Resume.pdf",
            mime="application/pdf"
        )

# Set page configuration
st.set_page_config(
    page_title="Portfolio - Sreeram Nithin",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Create the navigation buttons in a horizontal layout
col1, col2, col3, col4, col5, col6 = st.columns(6)

about_me_button = col1.button("About Me")
projects_button = col2.button("Projects")
experience_button = col3.button("Experience")
blog_button = col4.button("Blog")
skills_button = col5.button("Skills")
resume_button = col6.button("Resume")

if about_me_button:
    about_me()
elif projects_button:
    display_projects()
elif experience_button:
    experience()
elif blog_button:
    blog()
elif skills_button:
    display_skills()
elif resume_button:
    resume()
else:
    about_me()  # Default to the "About Me" section
