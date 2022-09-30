# Calculations

import pandas as pd

class TaxBrackets:
    def __init__(self, value):
        # self.value = input("\nWhat is your value?\n")
        self.value = value

    # Tax bracket dictionaries
    value_brackets_dict = {0.20:12571, 0.40:50270, 0.45:150000}
    nat_brackets_dict = {0.1325:12576, 0.0325:50268}
    vat_dict = {0.167:0}    # UK VAT is 20% but the customer pays 16.7% of the total cost towards that task

    def percentage_tax(self, type):
        total_tax = 0
        value = int(self.value)
        if type.lower() == 'income':
            current_brackets_dict = self.value_brackets_dict
        elif type.lower() == 'national insurance':
            current_brackets_dict = self.nat_brackets_dict
        elif type.lower() == 'vat':
            current_brackets_dict = self.vat_dict

        for key, val in current_brackets_dict.items():
            if value > val:
                total_tax += (value-val)*key
                # print(total_tax)
            
        return round(total_tax/value, 2), round(total_tax, 2)

class Inflation:
    def __init__(self, value):
        self.value = value
    
    inflation_df = pd.read_csv("./data/series-280922.csv")

    def value_decrease(self, trailing_months):
        percent_list = []
        for month in reversed(range(1,trailing_months+1)):
            percent_list.append(self.inflation_df.iloc[-month,1])
        percent_list = [float(x)/12.0 for x in percent_list]
        for perc in percent_list:
            self.value = self.value * (1-perc/100)
        return round(self.value, 2)