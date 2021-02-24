Inventory Management:
- What resources currently exist in my account?
- What is the latest configuration state of my resources?
- what relationship exist between my resources?
- what configuration changes occured with in specified period of time?


Config Aggregator is used in get all accounts info at one place, relation ships,cost management in checking cost
its actually replicating all accounts config data to centralise place(master account)

sample quires: https://docs.aws.amazon.com/config/latest/developerguide/example-query.html

Cost-optimization:
Query to list all EC2 volumes that are not in use

SELECT 
    resourceId, 
    accountId,
    awsRegion, 
    resourceType, 
    configuration.volumeType,
    configuration.size, 
    resourceCreationTime,
    tags,
    configuration.encrypted, 
    configuration.availabilityZone,
    configuration.state.value 
WHERE
   resourceType = 'AWS::EC2::Volume' 
AND 
    configuration.state.value <> 'in-use'
    

Relationships:
Find EC2 instances and network interfaces related to a security group
SELECT 
    resourceId 
WHERE 
    resourceType IN ('AWS::EC2::Instance', 'AWS::EC2::NetworkInterface') 
    AND relationships.resourceId = 'sg-abcd1234'

Note:
- Maximum of 500 results is retuned via advanced-query-config-aggregator and no apgination available
- No support for nested quiries.


Finding aal ec2-resouces in all account:
SELECT accountId,COUNT(*) WHERE resourceType = 'AWS::EC2::Instance' And accountId in (1234,5678) GROUP BY accountId

config-rules:
$0.003 for config record
$0.001 for config rule evaluation

- Usecase of config rules:
- https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html

 - All best practices for all resources.
 - 
to maintain PCSIDCII


The multi-account, multi-region data aggregation and advanced query capabilities are available at no additional cost to AWS Config customers

https://aws.amazon.com/about-aws/whats-new/2020/07/aws-config-multi-account-multi-region-data-aggregation-and-advanced-query-capabilities-now-available-in-asia-pacific-hong-kong-and-middle-east-bahrain-regions/#:~:text=You%20can%20view%20the%20query,cost%20to%20AWS%20Config%20customers.
https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html