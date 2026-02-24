import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load stock data from Excel file
file_path = 'random_stock.xlsx'
stock_data = pd.read_excel(file_path)

# Define thresholds for Bullish and Bearish market states
bullish_threshold = 1.0  
bearish_threshold = -1.0  

def determine_state(change_percentage):
    if change_percentage > bullish_threshold:
        return 'Bullish'
    elif change_percentage < bearish_threshold:
        return 'Bearish'
    else:
        return 'Stagnant'

stock_data['Market State'] = stock_data['Change(%)'].apply(determine_state)
states = ['Bullish', 'Bearish', 'Stagnant']
transition_counts = {state: {s: 0 for s in states} for state in states}

# Count the transitions between states
for i in range(1, len(stock_data)):
    previous_state = stock_data.iloc[i-1]['Market State']
    current_state = stock_data.iloc[i]['Market State']
    transition_counts[previous_state][current_state] += 1

print("Transition Matrix (Counts):")
for state in transition_counts:
    print(f"{state}: {transition_counts[state]}")

for state in transition_counts:
    total_transitions = sum(transition_counts[state].values())
    if total_transitions > 0:
        for next_state in transition_counts[state]:
            transition_counts[state][next_state] /= total_transitions

# Display the transition probabilities
print("\nTransition Matrix (Probabilities):")
for state in transition_counts:
    print(f"{state}: {transition_counts[state]}")
