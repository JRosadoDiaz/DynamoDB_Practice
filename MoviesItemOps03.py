from decimal import Decimal
from pprint import pprint
import boto3

#Update data
def update_movie(title, year, rating, plot, actors, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='us-west-2',
            aws_access_key_id="user",
            aws_secret_access_key="pass" #This is running off of the desktop version, credentials are not needed
        )
    
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a", #This query is able to add the additional attribute, actors
        ExpressionAttributeValues={
            ':r': Decimal(rating), #Using the Decimal library is required for any numbers inputed to DynamoDB
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_movie("The Big New Movie", 2015, 5.5, "Everything happens all at once.", ["Larry", "Moe", "Curly"])
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)