import json
import boto3
import random

my_bucket = 'lazydinners'
my_key = 'allrecipes.json'


def Get_Recipeoftheday():
    
    s3 = boto3.client('s3')

    object = s3.get_object(Bucket = my_bucket, Key = my_key)
    object_data = json.loads(object['Body'].read())
        
    data = []
    data += object_data
    
    recipes = data
    
    return recipes
    
def lambda_handler(event, context):
    # Call the get_recipeoftheday function and return appropriately formatted results.
    return {'isBase64Encoded': False,'statusCode': 200,'body': json.dumps(Get_Recipeoftheday()), 'headers': {"Access-Control-Allow-Origin": "*"}}
