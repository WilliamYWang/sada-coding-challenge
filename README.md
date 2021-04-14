# Challenge: Longest-compound words

https://github.com/WilliamYWang/sada-coding-challenge

## Run
1. cd highest-profit
2. ./run.sh

or

1. cd highest-profit
2. python highest_profit.py data.csv

## Input
* We only need data.csv for input

## Output
* Produces data2.json as output

## Design
* Reads in the csv as a dictionary
* Checks to see whether each row's 'Profit (in millions)' column is a string
* If the row's 'Profit (in millions)' column is a numerical value then add the row to a new dictionary called 'data'
* Dumps this 'data' dictionary into a JSON file
* Sorted this 'data' dictionary based on the 'Profit (in millions)' column
