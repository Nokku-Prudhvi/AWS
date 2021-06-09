import os
import boto3


def get_ec2_instances(region, project, state):
	ec2_instances=[]
	ec2=boto3.resource('ec2')
	instances=ec2.instances.filter(
	Filters = [
		
		{
		'Name': 'tag:project',
		'Values': [project]
		},
		{ 'Name': 'instance-state-name',
		  'Values': [state]
		}

	]
	)
	print(instances)
	for i in instances:
		print(i)
	return list(instances)
	

def start_ec2_instances(region, project):
	instances_to_start=get_ec2_instances(region, project, 'stopped')
	print(instances_to_start)
	instances_to_start[0].start()
	return "Instance started Successfully"


def stop_ec2_instances(region, project):
	instances_to_stop=get_ec2_instances(region, project, 'running')
	print(instances_to_stop)
	instances_to_stop[0].stop()
	return "Instance stopped Successfully"


def lambda_handler(event, context):
	region= 'ap-south-1'
	project= 'demo'
	
	instance_state_changed=0
	if(event.get('action')=='start'):
		instance_state_changed=start_ec2_instances(region, project)
	elif(event.get('action')=='stop'):
		instance_state_changed=stop_ec2_instances(region, project)

	return instance_state_changed
