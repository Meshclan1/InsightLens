import boto3, json, requests
from utils.shared_util import normalise_review

secrets_client = boto3.client('secretsmanager')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    secret = secrets_client.get_secret_value(SecretId="ExternalAPIKeys")
    api_keys = json.loads(secret['SecretString'])
    
    google_reviews = requests.get('https://maps.googleapis.com/...', params={'key': api_keys['google']}).json()
    trustpilot_reviews = requests.get('https://api.trustpilot.com/...', headers={'apikey': api_keys['trustpilot']}).json()
    
    reviews = normalise_review(google_reviews + trustpilot_reviews)
    
    s3.put_object(Bucket='insightlens-raw', Key='raw_reviews.json', Body=json.dumps(reviews))
    
    return {"status": "success"}
