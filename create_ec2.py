import boto3
import sys

MAX_COUNT=1
MIN_COUNT=1
INSTANCE_TYPE='t2.micro'
REGION='us-east-2'
AMI=''

# Create a default session
# boto3 will use exported AWS_PROFILE variable and the credentials with that profile
session = boto3.Session()

ec2 = boto3.client('ec2', region_name=REGION)
 
# create instances
conn = ec2.run_instances(InstanceType=INSTANCE_TYPE,
                         MaxCount=MAX_COUNT,
                         MinCount=MIN_COUNT,
                         ImageId=AMI)
print(conn)
