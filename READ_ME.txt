To begin the application you need to fulfill several requirements:

* Download DynamoDB locally using: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
  - Extract the contents into a folder anywhere you like
  - Open the folder through Command Prompt
  - Run: java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
  ** DynamoDB will run for as long as the Command Prompt window is open
  *** ctrl+c to close manually

* The latest version of python
  - Install python package 'boto3', this is the AWS SDK for python

* You can retieve a new copy of the sample data from: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/moviedata.zip

All files can be run individually through Visual Studio, preferably in order to avoid errors but ¯\_(ツ)_/¯
