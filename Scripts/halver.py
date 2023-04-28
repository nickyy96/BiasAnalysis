import pandas as pd
import os
import random

root_dir = './Samples'  # Replace with the path to your root directory

file_path = os.path.join(root_dir, 'samples.csv')
df = pd.read_csv(file_path, header=0)

# Take 5000 random rows from the data frame
random_rows = df.sample(n=5000)

# Export the aggregated data to a new CSV file
random_rows.to_csv('./Samples/random.csv', index=False)