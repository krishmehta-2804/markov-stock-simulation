import numpy as np
import matplotlib.pyplot as plt

transition_matrix = np.array([
    [0.529, 0.294, 0.177],  
    [0.308, 0.538, 0.154],  
    [0.125, 0.125, 0.75]    
])

num_weeks = 156   
initial_price = 74.18  
num_simulations = 1000  


all_prices = np.zeros((num_simulations, num_weeks + 1))


for sim in range(num_simulations):
    price = initial_price
    current_state = 0  
    weekly_prices = [price]

    for day in range(num_weeks):
        
        current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])
        
        if current_state == 0:  
            price *= np.random.normal(1.001, 0.01)  
        elif current_state == 1:  
            price *= np.random.normal(0.999, 0.02)  
        else:  
            price *= np.random.normal(1.0, 0.005)  
        
        weekly_prices.append(price)
    
    all_prices[sim] = weekly_prices  

average_prices = np.mean(all_prices, axis=0)

plt.figure(figsize=(12, 6))
plt.plot(average_prices, color='red', label="Average Stock Price (1000 simulations)")
plt.title("Average Stock Price Prediction over One Year (Markov Chain & Monte Carlo)")
plt.xlabel("Week")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()
