from azure.cosmos import exceptions, CosmosClient, PartitionKey
import family

def get_item(cidr):
    item={"id":"ransom"+cidr[0:6],"cidr":cidr,"Alias":"Alias"}
    return item

# Initialize the Cosmos client
endpoint = ""
key = ''

# <create_cosmos_client>
client = CosmosClient(endpoint, key)
# </create_cosmos_client>

# Create a database
# <create_database_if_not_exists>
database_name = 'firstCosmosDatabase'
database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>

# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
container_name = 'firstCosmosContainer3'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)
# </create_container_if_not_exists>

family_items_to_create = [get_item("10.0.0.0/20"),get_item("10.0.16.0/20")]
 # <create_item>
for family_item in family_items_to_create:
    print(family_item)
    container.create_item(body=family_item)
# </create_item>

# Add items to the container
#family_items_to_create = [family.get_andersen_family_item(), family.get_johnson_family_item(), family.get_smith_family_item(), family.get_wakefield_family_item()]
"""
 # <create_item>
for family_item in family_items_to_create:
    print(family_item)
    container.create_item(body=family_item)
# </create_item>

# Read items (key value lookups by partition key and id, aka point reads)
# <read_item>
for family in family_items_to_create:
    #item_response = container.read_item(item=family['id'], partition_key=family['lastName'])
    item_response = container.read_item(item="Andersen_f1b3c49d-1550-45fc-9e3c-cbcf702ede78", partition_key=family['lastName'])
    print(item_response)
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Read item with id {0}. Operation consumed {1} request units'.format(item_response['id'], (request_charge)))
# </read_item>


# Query these items using the SQL query syntax. 
# Specifying the partition key value in the query allows Cosmos DB to retrieve data only from the relevant partitions, which improves performance
# <query_items>
query = "SELECT * FROM c WHERE c.lastName IN ('Wakefield', 'Andersen')"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))
# </query_items>
"""
