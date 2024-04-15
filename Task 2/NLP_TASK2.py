import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Load the CSV dataset
data = pd.read_csv("Task 2/covid_19_data.csv")  

# Check for missing values
# Assuming the column containing the text data is "Country/Region"
data = data.dropna(subset=["Country/Region"]) 

# Define functions for tokenization and stemming
def tokenize(text):
    return word_tokenize(text.lower())  # Convert to lowercase

def stem(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

# Apply tokenization and stemming
# Assuming the column containing the text data is "Country/Region"
data["Country/Region"] = data["Country/Region"].apply(str)  # Convert 'Country/Region' column to string
data["Country/Region"] = data["Country/Region"].apply(tokenize)  
data["Country/Region"] = data["Country/Region"].apply(stem)

# Print the modified DataFrame
print(data)