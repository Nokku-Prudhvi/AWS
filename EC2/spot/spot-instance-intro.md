### Spot Instances:
- spot instances are available at 90% discount compared to ondemand
- you first decide the max spot price
- The spot price vary with regions
- If spot price is above your maximum you have 2 minutes to choose whether to stop or terminate

### Spot Block:
- You may use spot block to stop your EC2 from being terminated even if spot prices goes more than maximum.you can set spot-b;lock between 1-6 hours

### Spot instances are useful for:
- Big data and analysis
- Containerized workloads
- CI/CD and testing
- web services
- Image and media rendering
- High performance monitoring

### Not used for:
- persistent workloads
- critical jobs
- databases

### Spot Fleets:
- Spot fleet is collection of on-demand and spot instances
- Spot Fleet ateempts to launch based on spot-fleet requests 
- You can have the following startegies with spot fleets:
- 1)Capacity optimized:The spot instances comes from the pool with optmial capacity for the number of instances launching
- 2)lowsetPrice:spot instances come from the pool with lowest price . this is default strtegy
- 3)Diversified: the spot instances are distributed across pool
- 4)InstancePollToUseCount:Spot instances are distributed across the number of spot insatnce pool you specify.This parameter is valid only if used with lowestPrice strtegy.


### cli command for describe spot price
Even in the dashboard also you can visualize the spot-price for an instance type over 3 months

    aws ec2 describe-spot-price-history --instance-types m1.xlarge --start-time 2014-01-06T07:08:09 --end-time 2014-01-06T08:09:10 

https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-price-history.html


