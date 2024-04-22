import re
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Download NLTK stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Read the contents of the file
with open("random_paragraphs.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Remove non-alphanumeric characters and split into words
words = re.findall(r'\b\w+\b', text.lower())

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display word frequency count to console
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
