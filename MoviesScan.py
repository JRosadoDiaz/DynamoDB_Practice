from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def scan_movies(year_range, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='us-west-2',
            aws_access_key_id="user",
            aws_secret_access_key="pass" #This is running off of the desktop version, credentials are not needed
        )
    
    table = dynamodb.Table('Movies')

    scan_kwargs = {
        'FilterExpression': Key('year').between(*year_range), # Specifies a condition that returns only items that satisfy the condition, all other items are discarded
        'ProjectionExpression': "#yr, title, info.rating", # Specifies the attributes you want in the scan result
        'ExpressionAttributeNames': {"#yr": "year"}
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        display_movies(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == "__main__":
    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}")
            pprint(movie['info'])

    query_range = (1950, 1959)
    print(f"Scanning for movies released from {query_range[0]} to {query_range[0]}")
    scan_movies(query_range, print_movies)


### Notes ###
# A single scan returns a maximum of 1MB to a user
# Filters are applied only after the entire table has been scanned
# The scan method returns a subset of the items each time, called a page