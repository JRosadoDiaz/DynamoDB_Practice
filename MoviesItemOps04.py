from decimal import Decimal
from pprint import pprint
import boto3

#Update an Atomic Counter
def increase_rating(title, year, rating_increase, dynamodb=None):
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
        UpdateExpression="set info.rating = info.rating + :val",
        ExpressionAttributeValues={
            ':val': Decimal(rating_increase)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = increase_rating("The Big New Movie", 2015, 1)
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)