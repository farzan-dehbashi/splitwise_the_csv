import logging

import pandas as pd
import numpy as np
df = pd.read_csv('input_csv.csv',  delimiter="\t") # read the csv file
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # drop unused columns that are being add due to a bug
df.dropna(how='all', inplace= True) # drop all nan rows

spenders = df['spender'].unique()

payers = []
for index, row in df.iterrows():
    payer = row['payer']
    for item in np.char.split(payer, sep = ',').tolist():
        payers.append(item)
payers = np.unique(np.array(payers)) # pick unique payers
print('***')
for payer in payers:
    payer_df = df[(df['payer'].str.contains(payer))] #find the rows where payer name is in the list
    payer_df['your share'] = 0.0
    payer_df['balance'] = 0.0
    balance = 0
    print('payer= '+str(payer))
    for index, row in payer_df.iterrows():
        quotient = row['payer'].count(',') + 1# number of people who share the row
        if payer == row['spender']:
            payer_df.at[index, 'your share'] = float(-1 * float(row['amount']) / quotient)
            balance = balance - (float(row['amount'])-(float(row['amount']) / quotient))


        elif payer != row['spender']:
            payer_df.at[index, 'your share'] = float(+1 * float(row['amount']) / quotient)
            balance = balance + float(row['amount']) / quotient
    payer_df.at[0, 'balance'] = balance
    payer_df.to_csv(str(payer)+'.csv')
