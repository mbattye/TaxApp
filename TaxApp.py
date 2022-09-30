import streamlit as st
import pandas as pd
from tools.tax_calculations import TaxBrackets

st.set_page_config(
    page_title="TaxApp",
    page_icon="💰",
)

# sidebar 
# st.sidebar.title("Where do you want to go?")

st.title("Tax App")
st.markdown("## Taxes. Sorted.")
st.write('Taxes are inherently complicated, implicitly assumed yet not explicitly taught.')
st.write('We want to build tools to change that. Giving knowledge and power to the tax payer, not the rule maker.')
st.write('See what you are paying to keep the country running.')

# data = [['Karan',25,'Male','SDE'],['Danielle',23,'Female','Marketing Intern'],['Mike',20,'Male','SEO Expert']]
# df = pd.DataFrame(data, columns=['EmployeeName', 'Age','Gender','Designation'])

# if st.checkbox('Show Available data'):
#     df

# Download report
# st.download_button('Download report', data)