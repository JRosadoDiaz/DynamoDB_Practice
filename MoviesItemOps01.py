from pprint import pprint
import boto3

#Creating new data
def put_movie(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='us-west-2',
            aws_access_key_id="user",
            aws_secret_access_key="pass" #This is running off of the desktop version, credentials are not needed
        )
    
    table = dynamodb.Table('Movies')
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_movie("The Big New Movie", 2015, "Nothing happens at all.", 0) #Returns the http response from the database in Json format giving details on the addition
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)