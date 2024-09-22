#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

name = st.text_input("Enter your Name ")
fname = st.text_input("Enter your  Father's Name")
add = st.text_area("Enter your Address ")
semester = st.selectbox("Enter your Semester ",(1,2,3,4,5,6,7,8))  #dropdown

button = st.button("Done")
if button:
    st.markdown(f"""
    
    Name = {name}
    Father's Name = {fname}
    Address = {add}
    Semester = {semester}
    
    """)


# In[ ]:




