import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'random_stock.xlsx'
stock_data = pd.read_excel(file_path)

def classify_market_state(change_percentage):
    if change_percentage > 1:
        return 'Bullish'
    elif change_percentage < -1:
        return 'Bearish'
    else:
        return 'Stagnant'

stock_data['Market State'] = stock_data['Change(%)'].apply(classify_market_state)
transition_probabilities = {
    'Bullish': {'Bullish': 0.53, 'Bearish': 0.29, 'Stagnant': 0.18},
    'Bearish': {'Bullish': 0.31, 'Bearish': 0.54, 'Stagnant': 0.15},
    'Stagnant': {'Bullish': 0.12, 'Bearish': 0.75, 'Stagnant': 0.13}
}

initial_state_probs = {'Bullish': 1.0, 'Bearish': 0.0, 'Stagnant': 0.0}
current_state_probs = initial_state_probs.copy()
probabilities_over_time = {'Bullish': [], 'Bearish': [], 'Stagnant': []}

for week in range(len(stock_data)):
    probabilities_over_time['Bullish'].append(current_state_probs['Bullish'])
    probabilities_over_time['Bearish'].append(current_state_probs['Bearish'])
    probabilities_over_time['Stagnant'].append(current_state_probs['Stagnant'])

    next_week_probs = {
        state: sum(current_state_probs[prev_state] * transition_probabilities[prev_state][state]
                   for prev_state in transition_probabilities)
        for state in transition_probabilities
    }
    current_state_probs = next_week_probs

plt.figure(figsize=(8, 6))
plt.plot(range(len(stock_data)), probabilities_over_time['Bullish'], label='Bullish', color='blue')
plt.plot(range(len(stock_data)), probabilities_over_time['Bearish'], label='Bearish', color='red')
plt.plot(range(len(stock_data)), probabilities_over_time['Stagnant'], label='Stagnant', color='black')

# Add a vertical line at the "burn-in" week
burn_in_week = 15
plt.axvline(x=burn_in_week, color='green', linestyle='--', label='Burn-In Period')

plt.xlim(0, len(stock_data) - 1)
plt.ylim(0, 1)
plt.xlabel("Week")
plt.ylabel("Probability of Market State")
plt.legend()
plt.tight_layout()
plt.show()
