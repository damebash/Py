# %%
import streamlit as st
import math
import numpy_financial as npf

st.title('Rental Property Calculator')
st.write('This calculator is used to estimate the cash flow of a rental property. It is not meant to be used for investment purposes. Please consult a professional before making any investment decisions.')
st.write('--------')

st.columns(2)
col1, col2 = st.columns(2)

with col1:

    price = st.number_input('Price of property:', step=1000, format='%d', value=0)
    dp_percent = st.number_input('Down Payment Percent (%):', format='%d', value=0) / 100
    rate = st.number_input('Interest Rate (%):', format='%f', value=0.0) / 100
    loan_years = st.number_input('Length of loan (years):', format='%d', value=0)
    
    down_payment = dp_percent * price
    st.write(f'Down Payment: ${down_payment:,.2f}')

    mortgage = price - down_payment
    montly_rate = rate / 12

    monthly_mortgage = abs(npf.pmt(montly_rate, loan_years*12, mortgage))

    st.write(f'Monthly Mortgage: ${monthly_mortgage:,.2f}')

with col2:
    tax = st.number_input('Property Tax Rate (%):', format='%d', value=0)
    estimate_repairs = st.number_input('Estimated Repairs ($):', format='%d', value=0)
    st.number_input('Home Insurance Rate (%)', format='%d', value=0)
    hoa = st.number_input('HOA Fee', format='%d', value=0)

    total_capital = down_payment + estimate_repairs


    st.write(f'Total Capital needed: ${total_capital:,.2f}')




# st.number_input('Annual Rent Increase (%)', format='%d', value=0)
# st.number_input('Selling Cost (%)', format='%d', value=0)



# st.write(f'Mortgage: ${mortgage:,.2f}') 



rent = st.number_input('Monthly Rent', format='%d', value=0)

yearly_gross_rent = rent * 12

st.write('--------')

st.subheader('Expenses')

trash = st.number_input('Trash ($)', format='%d', value=50)
maintenance = st.number_input('Maintenance (%)', format='%d', value=5) / 100
vacancy = st.number_input('Vacancy (%)', format='%d', value=5) / 100
management = st.number_input('Management (%)', format='%d', value=10) / 100

yearly_expenses = trash * 12 + yearly_gross_rent * maintenance + yearly_gross_rent * vacancy + yearly_gross_rent * management
monthly_expenses = yearly_expenses / 12

st.write(f'Yearly Expenses: ${yearly_expenses:,.2f}')
st.write(f'Monthly Expenses: ${monthly_expenses:,.2f}')

cash_flow = yearly_gross_rent - yearly_expenses

st.write(f'Yearly Cash Flow: ${cash_flow:,.2f}')