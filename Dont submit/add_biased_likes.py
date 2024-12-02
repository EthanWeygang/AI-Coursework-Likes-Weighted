import pandas as pd
import numpy as np

file_path = './no_likes_Tweets.csv'  
df = pd.read_csv(file_path)

# Define scales for different sentiments
scale_positive = 10000
scale_neutral = 10
scale_negative = 10

# Generate likes based on sentiment
likes = []
for sentiment in df['sentiment']:
    if sentiment == 'positive':
        like = np.random.exponential(scale_positive)
    elif sentiment == 'neutral':
        like = np.random.exponential(scale_neutral)
    else:  # Assuming 'negative' sentiment
        like = np.random.exponential(scale_negative)
    likes.append(like)

# Update the 'likes' column with the new random values
df['likes'] = np.clip(likes, 0, 10000).astype(int)

# Save the updated DataFrame back to the CSV file
output_file = 'Tweets.csv'
df.to_csv(output_file, index=False)

print(f"Updated dataset saved to {output_file}")

# To generate a new dataset with likes, delete the "Tweets.csv" file and run this script once. 
# Then you'll have new data.
# This is purely for making the like data it isnt do do with the AI and wont be submitted.