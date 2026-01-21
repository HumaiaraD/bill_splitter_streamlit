import streamlit as st

st.title("Bill Splitting Calculator")
bill_amount = float(st.number_input("Enter the total bill amount: $", min_value=0.0, step=0.01))
tip_percentage = float(st.number_input("Enter the tip percentage: ", min_value=0.0, step=0.01))
tip_amount = (tip_percentage / 100) * bill_amount
per_person = int(st.number_input("Enter the number of people splitting the bill: ", min_value=1, step=1))

def reset_fields():
    st.session_state.bill_amount = 0.0
    st.session_state.tip_percentage = 0.0
    st.session_state.per_person = 1

total = bill_amount + tip_amount
amount_per_person = total / per_person
st.write(f"Total (including tip): ${total}")
st.write(f"Each person pays: ${amount_per_person}")

if st.button("Reset", on_click=reset_fields):
    pass
if st.button("Celebrate!"):
    st.balloons()
