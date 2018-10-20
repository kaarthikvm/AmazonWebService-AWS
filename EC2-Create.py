#!/usr/bin/python

import boto3
import os
ec2 = boto3.client('ec2',region_name='us-east-2')#,
                           #aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                           #aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

def create_key_pair():
    ''' create key pair '''
    # create a file to store the key locally
    with open('ec2-keypair.pem','w') as outfile:

        # check whether key pair exits and delete it
        response = ec2.delete_key_pair(KeyName='ec2-keypair',DryRun=False);
        print response;


        # call the boto ec2 function to create a key pair
        key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

        # capture the key and store it in a file
        KeyPairOut = str(key_pair['KeyMaterial'])
        print(KeyPairOut)

        outfile.write(KeyPairOut)


# create a new EC2 instance
def create_instance():
    instances = ec2.create_instances(
                ImageId='ami-0b59bfac6be064b78',
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro',
                KeyName='ec2-keypair')

if __name__ == "__main__":
    create_key_pair();
    #create_instance();
