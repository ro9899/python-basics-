# Day 27 - Statistics & Probability in Python

import statistics as stats
import random

# --------------------
# Basic Statistics
# --------------------
data = [10, 20, 30, 40, 50, 60, 70]

mean_val = stats.mean(data)
median_val = stats.median(data)
mode_val = stats.mode(data)
stdev_val = stats.stdev(data)
variance_val = stats.variance(data)

print("Data:", data)
print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
print("Standard Deviation:", stdev_val)
print("Variance:", variance_val)

# --------------------
# Probability with Random
# --------------------
print("\nRandom Numbers:")

# Random float between 0 and 1
print("Random float [0,1):", random.random())

# Random integer between 1 and 10
print("Random int [1,10]:", random.randint(1, 10))

# Choose random element from a list
choices = ["Apple", "Banana", "Cherry", "Date"]
print("Random Choice:", random.choice(choices))

# Shuffle a list randomly
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print("Shuffled Deck:", deck)

# --------------------
# Simulating Probability
# --------------------
# Example: Tossing a coin 10 times
coin = ["Heads", "Tails"]
results = [random.choice(coin) for _ in range(10)]
print("\nCoin Toss Results:", results)

# Example: Rolling a dice 5 times
dice_results = [random.randint(1, 6) for _ in range(5)]
print("Dice Rolls:", dice_results)













