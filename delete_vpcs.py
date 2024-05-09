import boto3
import csv

import boto3.session

def delete_vpc(vpc_id, session):
   ec2 = session.client('ec2')
   response = ec2.delete_vpc(VpcId=vpc_id)
   return response

def main():
    with open('vpcs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            account_profile, region, vpc_id = row
            aws_profile = account_profile.strip()
            session = boto3.Session(profile_name=aws_profile, region_name=region)
            print(f"Deleting vpc {vpc_id} using aws profile {aws_profile} in region {region}")
            delete_vpc(vpc_id, session)
            print(f"VPC {vpc_id} deleted successfully")

if __name__ == "__main__":
    main()