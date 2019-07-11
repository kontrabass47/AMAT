#!/usr/bin/python3

from textblob import TextBlob as TextBlobAnalyzer
from textblob import Blobber
from sentiment_analyzer import SentimentAnalyzer
from sentiment_analyzer import SentimentObject

# This class uses the textblob library to performance sentiment analysis
# on a provided list of sentences.
class TextBlob(SentimentAnalyzer):

    # sentimentList - list of textblob sentiment analysis objects.
    # each object has access to sentiment.polarity and sentiment.subjectivity
    #   - polarity is a scale from -1.0 to 1.0, from negative to positive
    #   - subjectivity is a scale from 0.0 to 1.0, a measure of how opinionated
    #     the sentence is
    #def __init__(self):

    
    # Analyzes a single string for sentiment. This is a method that 
    # can be used on its own, but is also used in analyzeList as a helper
    def analyzeString(self, text):
        analyzer = TextBlobAnalyzer(text)
        obj = SentimentObject()
        if analyzer.sentiment.polarity >= 0.001:
            self.poscount += 1
            obj.classifier = "positive"
        elif analyzer.sentiment.polarity <= -0.001:
            self.negcount += 1
            obj.classifier = "negative"
        else:
            obj.classifier = "neutral"
#        print("TextBlob Result")
#        print(analyzer.sentiment)
        obj.sentence = text
        obj.aggregate = analyzer.sentiment.polarity
        return obj


    # analyzes the list of sentences passed in and populates the object's list
    # sentiment objects
    def analyzeList(self, list):
        counter = 0
        for sentence in list:
            obj = self.analyzeString(sentence)
            self.polarity += obj.aggregate
            if (obj.classifier == "negative" or obj.classifier == "positive"):
                counter += 1
            self.sentimentList.append(obj)
        self.polarity = self.polarity / counter
