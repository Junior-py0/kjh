import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Calculate sum and product when the button is clicked
if st.button("Calculate"):
    sum_result = num1 + num2
    product_result = num1 * num2

    # Display results
    st.write(f"The sum of {num1} and {num2} is: **{sum_result}**")
    st.write(f"The product of {num1} and {num2} is: **{product_result}**")
