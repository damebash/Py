# %%
import streamlit as st
import math
import numpy_financial as npf

price = st.number_input('Price', step=1000, format='%d', value=0)
dp_percent = st.number_input('Down Payment Percent (%)', format='%d', value=0) / 100
rate = st.number_input('Interest Rate (%)', format='%f', value=0.0) / 100
loan_years = st.number_input('Loan Term (years)', format='%d', value=0)
tax = st.number_input('Property Tax Rate (%)', format='%d', value=0)
estimate_repairs = st.number_input('Estimated Repairs', format='%d', value=0)
montly_rate = rate / 12


st.number_input('Home Insurance Rate (%)', format='%d', value=0)
hoa = st.number_input('HOA Fee', format='%d', value=0)
rent = st.number_input('Monthly Rent', format='%d', value=0)
# st.number_input('Annual Rent Increase (%)', format='%d', value=0)
# st.number_input('Selling Cost (%)', format='%d', value=0)

down_payment = dp_percent * price
mortgage = price - down_payment
total_capital = down_payment + estimate_repairs

st.write(f'Down Payment: ${down_payment:,.2f}')
st.write(f'Mortgage: ${mortgage:,.2f}') 
st.write(f'Total Capital needed: ${total_capital:,.2f}')

monthly_mortgage = npf.pmt(montly_rate, loan_years*12, mortgage)

st.write(f'Monthly Mortgage: ${monthly_mortgage:,.2f}')
# st.write(f"Monthly Mortgage Payment: ${payment:,.2f}")

# %%
# acs