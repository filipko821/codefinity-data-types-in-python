each = 7
time = 60


# Calculate the number of completed transactions
completed = time // each
# Calculate the number of remaining minutes
minutes = time % each

# Print these values
print("The number of completed transactions is", completed)
print("The number of remaining minutes is", minutes)