import streamlit as st 
from datetime import datetime

min_date = datetime(1900, 1, 1)
max_date = datetime.now()

st.title("User Information Form")

with st.form(key="user_info_form", clear_on_submit=True):
    name = st.text_input("Enter your first name")
    
    birth_date = st.date_input("Enter your birth date", min_value=min_date, max_value=max_date)
    
    if birth_date:
        age = max_date.year - birth_date.year
        
        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -= 1  # Corrected indentation (moved outside the if block)
        
        st.write(f"Your calculated age is {age} years")  # Corrected indentation (moved outside the if block)
        
        submit_button1 = st.form_submit_button(label="Submit form")
        
        if submit_button1:
            if not name or not birth_date:
                st.warning("Please fill all the form inputs")
            else:
                st.success("Form submitted successfully")
                st.success(f"Thank you, {name}, your age is {age}.")  # Corrected string formatting
                st.balloons()
                
        import pandas as pd

if submit_button1 and name and birth_date:
    df = pd.DataFrame({"Name": [name], "Birth Date": [birth_date], "Age": [age]})
    df.to_csv("user_data.csv", mode="a", index=False, header=False)
    st.success("Data saved successfully!")
