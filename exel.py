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
st.write(f'Monthly Cash Flow: ${cash_flow/12:,.2f}')

cap_rate = cash_flow / price

st.write(f'Cap Rate: {cap_rate:.2%}')

# %%
# Add the following import at the top
from tabulate import tabulate  # Helps print tables in a nice format

# Add the following code at the bottom
st.write('--------')

st.subheader('Yearly Return on Investment for the first 10 years')

# Initialize lists to hold yearly data
years = []
rois = []

# Create amortization table and calculate ROI for each year
for i in range(1, 11):
    # Calculate principal paid in year i
    principal_paid = abs(npf.ppmt(montly_rate, i*12, loan_years*12, mortgage)) * 12
    
    # Adjust total capital
    total_capital -= principal_paid
    
    # Adjust cash flow by adding the increase in equity (principal paid)
    adjusted_cash_flow = cash_flow + principal_paid
    
    # Calculate ROI
    roi = adjusted_cash_flow / total_capital
    
    # Add data to lists
    years.append(i)
    rois.append(f'{roi:.2%}')
    
# Create a table with ROI data
roi_table = tabulate(zip(years, rois), headers=['Year', 'ROI'], tablefmt='pipe')

st.write(roi_table)