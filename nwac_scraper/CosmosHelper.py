from azure.cosmos import CosmosClient
import datetime

import config

class CosmosHelper:

	def __init__(self):
		client = CosmosClient(config.ACCOUNT_URI, credential=config.MASTER_KEY)
		db_client = client.get_database_client(config.DATABASE_ID)
		self.__container_client = db_client.get_container_client(config.CONTAINER_NAME)

	def create_item(self, observation):
		print(observation.to_string())
		
