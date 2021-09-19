from azure.cosmos import CosmosClient
import datetime

import config

class ObservationsDBProvider:

	def __init__(self):
		client = CosmosClient(cosmos_config.ACCOUNT_URI, credential=cosmos_config.MASTER_KEY)
		db_client = client.get_database_client(cosmos_config.DATABASE_NAME)
		self.__container_client = db_client.get_container_client(cosmos_config.CONTAINER_NAME)

	def insert(self, observation):
		observation.print()
