from decimal import Decimal
import boto3
import json

#Imports data from Json file
def load_movies(movies, dynamodb=None):
    print('Loading movies...')

    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='us-west-2',
            aws_access_key_id="user",
            aws_secret_access_key="pass" #This is running off of the desktop version, credentials are not needed
        )
    
    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:",year,title)
        table.put_item(Item=movie)

if __name__ == '__main__':
    with open("moviedata.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)