import boto3

dynamodb = boto3.resource('dynamodb')
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    reviews = event['reviews']
    table = dynamodb.Table('InsightLensInsights')
    
    for r in reviews:
        sentiment = comprehend.detect_sentiment(Text=r['text'], LanguageCode='en')['Sentiment']
        key_phrases = comprehend.detect_key_phrases(Text=r['text'], LanguageCode='en')['KeyPhrases']
        
        table.put_item(Item={
            'review_id': r['id'],
            'sentiment': sentiment,
            'key_phrases': key_phrases
        })
    
    return {"status": "analysis complete"}
