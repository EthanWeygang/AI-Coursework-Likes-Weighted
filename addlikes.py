import pandas as pd
import numpy as np

file_path = './Tweets.csv'  
df = pd.read_csv(file_path)

scale = 10  
likes = np.random.exponential(scale, size=len(df))

df['likes'] = np.clip(likes, 0, 100).astype(int)

output_file = 'updated_dataset.csv'
df.to_csv(output_file, index=False)

print(f"Updated dataset saved to {output_file}")
