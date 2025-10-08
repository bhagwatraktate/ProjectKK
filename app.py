import json
import boto3

def lamda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instance(
    ImageId='XYZ',
    InstanceType='',
    KeyName='linux',
    MaxCount=1,
    MinCount=1
  )
  
