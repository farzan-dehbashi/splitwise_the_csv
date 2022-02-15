# Splitwise the CSV
This is a python script to imitate splitvise app using pandas library. It splits the expenses and calculates the shares of each person involved in a trip.

## More details
calc.py is a script that reads input_csv.csv file and calculate the share of each individual. The input file columns are the following:

* spender: is the name who has paid for that purchase
* amount: is the total value of the purchase
* description: is the description of the purchase
* payer: list of people who enjoyed the purchase including/excluding the spender

### How to use:
```angular2html
python3 calc.py
```
