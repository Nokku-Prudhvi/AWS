import os
import boto3


def get_ec2_instances(region, project, state):
	ec2_instances=[]
	ec2=boto3.resource('ec2', region_name=region)
	
	filters = [
		
		{
		'Name': 'tag:project',
		'values': [project]
		}
		{ 'Name': 'instance_state-name',
		  'values': [state]
		}

	]

def start_ec2_instances(region, project):
	instances_to_start=get_ec2_instances(region, project, 'stopped')
	#instance_state_changed=0
	print(instances_to_start)
	instances_to_start[0].start()
	
	#for instance i instances_to_stop:
	#	instance.start()
	#	instance_state_changed+=1
	
	return "Instance started Successfully"


def stop_ec2_instances(region, project):
	instances_to_stop=get_ec2_instances(region, project, 'running')
	#instance_state_changed=0
	print(instances_to_stop)
	instances_to_stop[0].stop()
	
	#for instance i instances_to_stop:
	#	instance.stop()
	#	instance_state_changed+=1
	
	return "Instance stopped Successfully"


def lambda_handler(event, context):
	region= 'us-east-1'
	project= 'demo'
	
	instance_state_changed=0
	if(event.get('action')=='start'):
		instance_state_changed=start_ec2_instances(region, project)
	elif(event.get('action')=='stop'):
		instance_state_changed=stop_ec2_instances(region, project)

	return instance_state_changed
