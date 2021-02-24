ETL is most time-consuming part of analytics.(80% of timr spent here)
Athena works only on s3 but not in datawarehousing data

Glue:
- discover : automtically discover and categorize your data making it immediately searchable and quesryable across data sources. Eample:crawlers
           -Data Catalog
		   --Apache Hive Metastore compatable
		   --Integrated with AWS services
		   --Automatic crawling
- Develop: Generate code to clean,enrich,and relaibly move data between various data sources.Easily customize this code or bring your own. Example:ETL
		   -Job Authoring
		   --Auto-generated ETL code
		   --python language , Apache spark Framework is underling framework.
		   --Edit,debug and share
- Deploy: Run your job on a serverless,fully managed,scale-out environmenr.No compute resources to provision or manage. Example:unlike redshift
		   -Job Execution
		   --serverless execution
		   --flexible scheduling
		   --monitoring and alerting
		   

Use case-1:
Move data across storage systems.

Data Stores(Redshift,s3,RDS,Databases running on EC2) --> Glue crawlers(creates schema) --> Glue DataCatalog(unified schema can be used across all data stores) -->Glue ETL-jobs --> Destinaton(Redshift,s3,RDS,Databases running on EC2)

you can use athena catalog but prefered is glue catalog.


USE CASE-2:
Your data(web app data,RDS,on premise data,streaming data) --> s3(coverting to parquet format ,etc, Glue-ETL can be used on top of s3) -->Glue crawlers -->Glue Data catalog --> Athena,EMR,Redshift Spectrum(analytics) -->Quiksight


Logical data lake with aws glue:
Data stores-->Glue crawlers->glue data catalog-->glue ETL-->Zepplin

Apache zepplin:
Suppose if a team of 50 developers wants to generates Etl code in parallel .every time you cant create a job,run it on demand. For interactively firing your
quiries on aws glue needs an glue endpoint.so apache zepplin you can connect to aws glue via endpoint and can start firing quiries.

Glue data catalog --> Athena, Redshift spectrum -->quicksight

- Each aws account as one AWS Glue data catalog(per account)
- use iam policies on glue data catalog schems
- versions changes can be audited for schema in glue data catalog
- Glue spark job can be created under vpc by eni's(private ip's) by which spark jobs can get/put data from datastores
- All api callas are logged in cloudtrail



- intially when glue job sets-up it may take 8-10 minutes time as it is creating/setting spark environment. And this environment can be useful for one-hour or so.
But you are billed for job-running time only.

COST:

ETL and development endpoints:
-you only pay for the time yor ETL job takes to run.
-hourly charged on DPU(dta processing units)
-1 DPU= 4vCPU,16GB memory
- A Glue ETL job requires minimum of 2 DPU's. Note: BY default glue allocates 10 DPUs to each ETL job
- A Glue Development endpoint requires a minimum of 2 DPU's. Note: By default glue allocates 5 DPUS's

Pricing:
- $0.44 per DPU-hour, billed per second,with a 10-minute minimum for each ETL job ( This means for every ETL job you will be charged for 10 minutes default minimum)
- $0.44 per DPU-hour, billed per second,with a 10-minute minimum for each  provisioned development endpoint ( development endpoint charges you if it is created whether you use or not use)
-Additionally, If you ETL from data sources such as s3,rds,redshift, you are charged standard request and data transfer rates.
-Aditionally, iF you use cloudwatch , you are charged standard rates for cloudwatch logs and cloudwatch events.


DATA Catalog storage and requests:
- you can store up to million objects for free
- $1 per 100,000 objects stored above 1M PER month
- First million access requests to the glue data catalog per month are free.(coomon requests are CreateTable,CreatePartition,GetTable,GetPartitions)
-$1 per million request above 1M in a month

Crawler:
- $0.44 per DPU-hour,billed per second,with a 10-minute minimum per crawler run.



Security and prevailages setup:
- Glue Service Role(policy) is already available with all glue related permissions
- Tp access s3 and other data-store within your vpc, vpc endpoint required
- A job or development end point can only access one vpc at a time.If you need to access data stores in different vpc's,:
  -- use vpc peering
  --use s3 as intermediatory storage location.i.e,s3 output of job 1 as input of job2.
  
- Vpc-endpoint access policy is used by glue. so if you want to allow the glue to access one s3-bucket , you can customize the policy allowing that s3-bucket.





Glue Databases:
- When you define a table in the aws glue data catalog, you add it to database
- Database is nothing but logical collection of tables.The tables that define the data(metadata) can be from many different data stors
- If you plan to access the database from amazon athena , then provide the name with only alphanumeric and underscore characters
- A table can be present only in one database
- When you delete dtabase , all tables are deleted.

Glue Tables:
- When you define a table in aws glue , you also specify the value of classification field that indicates the type and format of the data thats stored in the 
table
- If crawler creates table, these classifications are difined either by in-built classifiers or custom-classifier
- when a crawler detects the change in table metadata , a new version of the table is created in datacatalog.
- tables history is maintained in data catalog. version of schema that was used by ETL job is also kept in history.
- To improve query performance , a partitioned table might seperate monthly data into different files using name of the month as key
- When aws glue evaluates the data in amazon s3 folders to catalog a table, it dtermines whether an individual table or partitioned table to be added.
- table-name can't be changed.
- If the path is folder/* it includes all the files of folder . if path is folder/** it exclude all files from the folder. similarly 
- We can partition the data on level of sub-folders. i.e, if sub-folders are present inside root-folder, we can partiton the sub-folder using partiton-key.
Not only using sub-folder-structure in s3 but using this partitioning  key in table-creation, we can tell athena to query only on partition basis
which makes athena not to query unwanted folders or partitions , thus making qurires faste and efficient


Glue Crawlers:
- Crawlers automatically build your data catalog and keep it in sync
- Automatically discovers new data,extracts schema definitions 
 --detect schema changes and version tables
 - detect hive style partitions on s3(this is partition key which we came across when we are creating tables manually)
- Built-in classifiers for popular types;custom classifiers using grok expression(not needed for JDBC complaint data sources like s3,redshift)
- run ad hoc or on a schedule;serverless-only pay when you run
- Built-in classifiers:
  --mysql,mariadb,oracle,postgresql,microscoft sql server,aurora(used for RDS)
  --Amazon redshift(used for redshift)
  --Avro,parquet,ORC,XML,JSON&BSON,Logs[Apache(Grok),Linux(Grok),MS(Grok),Ruby,Redis],Delimited[comma,pipe,,tab,semicolon],compressions[zip,bzip,gzip,lz4,snappy]
  
- When you crawl a relational database, you must provide authorization credentials for a connection to read objects in the database engine.so we can restrcit
glue by providing limited permission database-user credentials

- When you define an s3 data store to crawl , you can choose same or different account s3
- file is downloaded by crawler if it is compressed file which consumes so much network speed.so beetter not to use crawler and direclty create table
from athena or glue.


Example use case: extracting the data from bills to know which service(sub-accounts) are using which aws-resource-types.
- dowload the file containing data from organization account bills(450MB)
- store it in s3 bucket
- create a iam-role for glue with GlueServiceRole and that s3 permissions.
- create a glue database\
- go to tables section, opt for "add table via crawler "






#################################################################

1) Crete iam-glue service based role. Attach AWS-managed glue policy. In addition, make sure the role is having permission to the particular folder
that you have given input to glue crawler/job

2)Create interface-s3-VPC-endpoint . This is useful if you want to communicate with S3 privately within aws-network.

3)create glue-database from glue-console.

4)Create table manually from glue-console

-> it is observed that miminum Get-Object permission is needed for Crawler and ETL-Job to work. List Obejct permission is not sufficient for crawler,ETL job
whereas sufficient for manually created table
->for crawler get-object permission of file is sufficient but for ETL job get-object permission of path(folder) need to be present.




