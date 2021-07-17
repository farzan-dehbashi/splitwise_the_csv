import pandas as pd
import numpy as np

# payer: the person who should reimberce money
# spender: the person who have spent the money and might want some of it back
# amount: amount of the total purchase
# your share: share of payer of that purchase
# balance: the amount that a person should pay or be payed


#read and clean the csv file
df = pd.read_csv('input_csv.csv',  delimiter="\t") # read the csv file
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # drop unused columns that are being add due to a bug
df.dropna(how='all', inplace= True) # drop all nan rows

#find unique spenders
spenders = df['spender'].unique()

#find unique payers (csv files are made based on unique payers)
payers = []
for index, row in df.iterrows():
    payer = row['payer']
    for item in np.char.split(payer, sep = ',').tolist():
        payers.append(item)
payers = np.unique(np.array(payers)) # pick unique payers

# calculate the payer shares:
for payer in payers:# for each person who should pay back
    payer_df = df[(df['payer'].str.contains(payer))] #find the rows where payer name is in the list
    payer_df['your share'] = 0.0  # initiat your share row
    payer_df['balance'] = 0.0     # initiate balance row
    balance = 0

    for index, row in payer_df.iterrows():
        quotient = row['payer'].count(',') + 1 # number of people who share the row
        if payer == row['spender']:
            payer_df.at[index, 'your share'] = float(-1 * float(row['amount']) / quotient)     # add the share of payer to 'your share' row
            balance = balance - (float(row['amount'])-(float(row['amount']) / quotient))       # update the balance of payer by their share


        elif payer != row['spender']:
            payer_df.at[index, 'your share'] = float(+1 * float(row['amount']) / quotient)
            balance = balance + float(row['amount']) / quotient

    payer_df.at[0, 'balance'] = balance
    payer_df.to_csv(str(payer)+'.csv')
