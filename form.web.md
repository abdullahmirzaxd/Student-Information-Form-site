```python
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
```

    2024-09-22 01:36:56.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.923 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.923 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.923 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.931 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.931 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    2024-09-22 01:36:56.947 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
    


```python

```
