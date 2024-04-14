import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Simple Streamlit App')

# A text input field
user_input = st.text_input("Enter your name", "")

# A button
button_clicked = st.button("Click Me")

np.random.seed(0)
dates = pd.date_range('2022-01-01', periods=100)
sales_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 1000, size=len(dates))
})

# Display user input when the button is clicked
if button_clicked:
    st.write("Hello,", user_input)
    st.title('Sales Data Visualization')

    # Display the sample data in a table
    st.subheader('Sample Data')

    # Plot the sales data
    st.subheader('Sales Over Time')
    st.line_chart(sales_data.set_index('Date'))

    st.title('Sales Data Visualization')

    # Display the sample data in a table
    st.subheader('Sample Data')

    # Plot the sales data using a bar chart
    st.subheader('Sales Over Time (Bar Chart)')
    st.bar_chart(sales_data.set_index('Date'))



# Generate sample data


# Preview the data
print(sales_data.head())