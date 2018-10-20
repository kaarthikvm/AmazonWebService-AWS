import boto3
import os
ec2Client = boto3.client('ec2')# Set these variables for JENKINS user manually as secret key cannot be used in public forum
                           # region_name='us-east-2',
                           # aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                           # aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

def create_key_pair():
    ''' create key pair '''
    # create a file to store the key locally
    with open('ec2-keypair.pem','w') as outfile:

        # check whether key pair exits and delete it
        response = ec2Client.delete_key_pair(KeyName='ec2-keypair',DryRun=False);
        print response;


        # call the boto ec2 function to create a key pair
        key_pair = ec2Client.create_key_pair(KeyName='ec2-keypair')

        # capture the key and store it in a file
        KeyPairOut = str(key_pair['KeyMaterial'])
        print(KeyPairOut)

        outfile.write(KeyPairOut)


# create a new EC2 instance
ec2Resource=boto3.resource('ec2');
def create_instance():
    instances = ec2Resource.create_instances(
                ImageId='ami-0782e9ee97725263d', # Ubuntu 16.04 LTS 
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro',
                KeyName='ec2-keypair',
                SecurityGroups=['kaarthikSecurityPolicy'])

if __name__ == "__main__":
    create_key_pair();
    create_instance();
