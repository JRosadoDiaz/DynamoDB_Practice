import boto3

def create_movie_table(dynamodb=None):
    print("Creating table...")

    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000", #Default port for desktop version
            region_name='us-west-2',
            aws_access_key_id="user",
            aws_secret_access_key="pass" #This is running off of the desktop version, credentials are not needed
        )

    table = dynamodb.create_table(
        TableName="Movies",
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH' #partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE' #sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10, #Provisioned Throughput = monitoring read and write capabilities
            'WriteCapacityUnits': 10 #This is running off the desktop version which ignores Provisioned Throughput
        }
    )
    return table

if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)