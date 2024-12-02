import pandas as pd
import numpy as np

file_path = './Apple.csv'  
df = pd.read_csv(file_path)

scale = 500
likes = np.random.exponential(scale, size=len(df))

df['likes'] = np.clip(likes, 0, 10000).astype(int)

output_file = 'Tweets.csv'
df.to_csv(output_file, index=False)

print(f"Updated dataset saved to {output_file}")

# To generate a new dataset with likes, delete the "Tweets.csv" file and run this script once. 
# Then you'll have new data.
# This is purely for making the like data it isnt do do with the AI and wont be submitted.