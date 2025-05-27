import requests 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

# Get all products
url = "https://fakestoreapi.com/products"
response = requests.get(url)

# Convert to JSON
products = response.json() # List of dictionaries

# Example: print first product
print(products[0])

def generate_fake_reviews(product):
    title = product["title"].lower()
    category = product["category"].lower()
    
    reviews_pool = []
    
    if "shirt" in title:
        reviews_pool = ["This shirt is comfortable!", "The shirt is of good quality.", 
                        "The shirt is too small.", "Fabric is too coarse", "It fits like a glove"]
    elif "jeans" in title:
        reviews_pool = ["These jeans are very comfortable.", "The jeans are of good quality.", "The jeans are too tight.", 
                        "The jeans are too loose.", "The jeans are too expensive."]
    elif "jewelery" in category:
        reviews_pool = ["The jewelry is beautiful.", "The jewelry is of good quality.", "The jewelry is too expensive.", 
                        "Not as shiny as expected", "It has such beautiful craftmanship"]
    else:
        reviews_pool = ["The product is good.", "The product is of good quality.", "The product is not worth the price.", 
                        "It works as expected", "Surprisingly good quality"]

    return random.sample(reviews_pool, random.randint(3, 5))

# empty dictionary for sentiment analysis
product_reviews = {}

# store reviews in dictionary
for product in products:
    product_reviews[product["id"]] = generate_fake_reviews(product)
    
# Sentiment analysis and average score
analyzer = SentimentIntensityAnalyzer()
product_sentiments = {}

for id, reviews in product_reviews.items():
    scores = [analyzer.polarity_scores(reviews)["compound"] for reviews in reviews]
    avg_score = sum(scores) / len(scores)
    product_sentiments[id] = avg_score
    
# coverting sentiment score to stars
def sentiment_to_stars(score):
    return round(((score + 1) / 2) * 5, 1)

# make dataframe 
results = []

# add data to dataframe
for product in products:
    id = product['id']
    title = product['title']
    price = product['price']
    category = product['category']
    sentiment_score = product_sentiments[id]
    star_rating = sentiment_to_stars(sentiment_score)
    results.append([id, title, price, category, sentiment_score, star_rating])

df = pd.DataFrame(results, columns = ["Product ID", "Title", "Price", "Category", "Sentiment Score", "Star Rating"])

# sort products by star rating 
df = df.sort_values(by = "Star Rating", ascending = False)

# visualize star rating
sns.barplot(data=df, x = "Star Rating", y = "Title", orient = "h")
plt.title("Estimated Star Rating of Products")
plt.xlim(1, 5)
plt.tight_layout()
plt.show()

# save to csv
#df.to_csv("product_sentiment_ratings.csv", index=False)


