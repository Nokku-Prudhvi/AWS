Athena:
- Interactive query service to analyse data in s3 using SQL.
  --Query instanstly
  --Pay per query(save 30-90% on per query costs through compression)
  --open(ANSI SQL interface,JDBC/ODBC drivers)
  --Easy(integrated with Quicksight)
  
- It wont store any data.
- Presto is used for SQL quiries
  -- In-memory distributed query engine
  -- ANSI-SQL compatible with extensions
- Hive is used for DDL functionality
  -- Complex data types
  -- Multitude of formats
  -- supports data partitioning
  
COST:  
- $5 per TB scanned from s3
- DDL Quiries and failed quiries are free
- Saveby using compression(gzip),columar formats(parquet),partitioning

Log Analysis Pipeline:
Raw Logs -> Structured -> Staging Table -> Spark -> Final Table ->Presto ->SQL
simalar as above:
Raw Logs -> Structured -> Staging S3    -> Glue  -> Final S3    ->Athena ->SQL

Log Analysis Life Cycle:

Aws service logs
Web Application Logs   --> s3  --->Glue Crawler-->Glue ETL -->Update table partition on Glue data catalog,Create Partion on S3 -->AThena 
Server Logs

- Format on athena available are CSV,JSON or columnar formats like Apache parquet and Apache ORC,ApacheWb Logs(regex expression),Text file with custom delimiters
- Directly you can create table in athena also.

- Athena uses IAM policies to restrict access to athena operations.Encryption option is useful for encrypt query results

Athena object model:
- Athena uses an approach known as schema-on-read.which means a schema is projected on to your data at the time you execute query.This eliminates
need for data loading and tranformations.
- maximum query string lengh is 256KB
- Hive supports multiple data formats through the use of serializer-deserializer?(SerDe) libraries.You can also define complex schemas using regular expressions.
- Table names must be globally unique


Athena Lab:
- "CREATE EXTERNAL TABLE" is used for creating tables in glue data-catalog. so whatever database objects you create using DDL statements in athena are automatically 
regestered in glue datacatalog.
- every format has corresponding SerDe libraries to be used.
- History contains previous query results,run-time,data scanned,encryption type.
- 
//refer lab-2 resource
//refer lab3 parquet resorce

ATHENA DDL COMMANDS:
- ALTER DATABASE SET DBPROPERTIES
- ALTER TABLE ADD PARTITION
- ALTER TABLE DROP PARTITION
- ALTER TABLE RENAME PARTITION
- ALTER TABLE SET LOCATION
- ALTER TABLE SET TBLPROPERTIES
----------------
- CREATE DATABASE
- CREATE TABLE
---------------
- DESCRIBE TABLE
---------------
- DROP DATABASE
- DROP TABLE
---------------
- MSCK REPAIR TABLE
---------------
- SHOW COLUMNS
- SHOW CREATE TABLE
- SHOW DATABASES
- SHOW PARTITIONS
- SHOW TABLES
- SHOW TBLPROPERTIES
--------------
Datatypes , DDL statements:
DATABASE:

CREATE (DATABASE|SCHEMA) [IF NOT EXISTS] database_name
   [COMMENT 'database_comment']
   [LOCATION 's3_loc']
   [WITH DBPROPERTIES('property_name'='property_value') [, ...] ]

Tables:
CREATE [EXTERNAL] TABLE [IF NOT EXISTS]
   [db.name.]table_name [(col_name data_type [COMMENT col_comment] [, ...] )]
   [COMMENT table_comment]
   [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
   [ROW FORMAT row_format]
   [STORED AS file_format] [WITH SERDEPROPERTIES (...)] ]
   [LOCATION 's3_loc']
   [TBLPROPERTIES (['has_encrypted_data='true|false',] ['classification'='aws_glue_classification',] property_name=property_value [, ...]  )]

-To run ETL jobs,AWS glue requires that you create a table with the classification property to indicate the data type for Aws glue as csv,paraquet,orc,avro,json.
-you can specify this classification property('classification'='csv') using glue console also.

SerDe:
- To create tables and query data from files in the formats in Athena , specify a SerDe so that athena knows which format is used and how to parse the data.
- Athena doesnot support custom SerDe
- You specify SerDe type by listing explicitly in ROW FORMAT part of your CREATE TABLE statement in Athena. Athena Uses SerDe types by default for certain
types of format if you omit to mention.
- In general, it uses LazySimpleSerde

-LazySimpleSerDe - CSV,TSV,Custom Delimited Files
- Hive Json or OpenX Json SerDe for JSON files.
- Avro SerDe for Apache AVRO files
- ORC SerDe,ZLIB Compression for ORC files
- Parquet SerDe,Snappy Compression for Parquet files
- Grok SerDe for Logstash log files
- Regex Serde for Apache Webserver log files
- CloudTrial Serde for Cloudtail logs


Athena Query AWS Service Logs:
- CLoudtrail
- cloudfront
- CLB,ALB Logs
- VPC Flow logs



Athena Limitations:
- Athena Query timeout 30 minutes
- concurrency limits - 20 concurrent DDL quiries(used for creating tables and adding partitions), 20 soft limit of concurrent SELECT quiries
- Athena does not support but Presto Version 0.172 supports are defined below:
  -- CREATE TABLE AS SELECT statements
  -- INSERT INTO statements
  -- Athena supports only:
	 - snappy(default compression format for files in Parquet format)
	 - ZLIB (default compression format for files in ORC format)
	 - GZIP
	 - LZO
  -- 




