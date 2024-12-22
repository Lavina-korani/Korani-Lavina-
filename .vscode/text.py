import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Initialize the Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # Get the sentiment scores
    scores = analyzer.polarity_scores(text)
    
    # Determine the sentiment category
    if scores['compound'] >= 0.05:
        return "Positive"
    elif scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Welcome to the Sentiment Analysis Program!")
    while True:
        user_input = input("Enter a text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()