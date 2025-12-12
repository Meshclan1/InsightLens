import boto3, json

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    table = dynamodb.Table('InsightLensInsights')
    scan = table.scan()
    
    aggregated = {'positive':0, 'neutral':0, 'negative':0}
    for item in scan['Items']:
        aggregated[item['sentiment'].lower()] += 1
    
    s3.put_object(Bucket='insightlens-aggregated', Key='weekly_summary.json', Body=json.dumps(aggregated))
    return {"status": "aggregation complete"}
