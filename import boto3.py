import boto3

def manage_ec2_instances(action, tag_key, tag_value ):
    ec2 = boto3.client('ec2')

    # Find instances with the specified tag
    filters = [{'Name' : f"tag:{tag_key}", 'Values': [tag_value]}]
    instances = ec2.describe_instances(Filters=filters)

    instance_ids = [
        instances['Instanceid']
        for reservation in instances['Reservations']
        for instances in reservation['Instances']

    ]

    if action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        print(f"Started instances: {instance_ids}")
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"stopped instances: {instance_ids}")
    else:
        print("Invalid action. Use 'start' or 'stop'.")