import streamlit as st
import pandas as pd
from tools.tax_calculations import Inflation, TaxBrackets


st.title("Your Tax")

# Enter income and expenditure for calculation
income = st.number_input("Enter your salary (£):")
savings = st.number_input("Enter your savings (£):")
spending = st.number_input("Enter the amount your spend on VATable goods (£):")

st.markdown("## Income Tax")
st.markdown("Calculate your government tithe")

if income != 0:
    tb = TaxBrackets(income)
    percent_inc, tax_inc = tb.percentage_tax('Income')
    st.write(f"Your income tax is £{tax_inc} per annum.")
    st.write(f"Your percentage income tax is {percent_inc:.1%}.")

st.markdown("---")
st.markdown("## National Insurance Tax")
st.markdown("Calculate your entitlement tithe")

if income != 0:
    tb = TaxBrackets(income)
    percent_nat, tax_nat = tb.percentage_tax('National Insurance')
    st.write(f"Your national insurance tax is £{tax_nat} per annum.")
    st.write(f"Your percentage national insurance tax is {percent_nat:.1%}.")

st.markdown("---")
st.markdown("## Inflation")
st.markdown("Calculate your currency expansion tithe")

trailing_months = 12

if income != 0:
    inf_inc = Inflation(income)
    value_inc = inf_inc.value_decrease(trailing_months)
    st.write(f"Over the last year your income has decreased to £{value_inc} per annum.")

if savings != 0:
    inf_sav = Inflation(savings)
    value_sav = inf_sav.value_decrease(trailing_months)
    st.write(f"Over the last year your savings have decreased to £{value_sav}.")

if income != 0 and savings !=0:
    # Fix this to work with OR (don't need percentage calc with values)
    percent_inf = 1 - (value_inc + value_sav)/(income + savings)
    st.write(f"Your percentage loss due to inflation is {percent_inf:.1%}.")

st.markdown("---")
st.markdown("## Value Added Tax")
st.markdown("Calculate your trade tithe")

if spending != 0:
    tb = TaxBrackets(spending)
    percent_vat, tax_vat = tb.percentage_tax('VAT')
    st.write(f"Your VAT tax is £{tax_vat} per annum.")
    st.write(f"Your percentage VAT tax is {percent_vat:.1%}.")