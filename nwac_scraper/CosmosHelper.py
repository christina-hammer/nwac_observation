from azure.cosmos import CosmosClient
import datetime
from Observation import *

import config

class CosmosHelper:

	def __init__(self):
		client = CosmosClient(config.ACCOUNT_URI, credential=config.MASTER_KEY)
		db_client = client.get_database_client(config.DATABASE_ID)
		self.__container_client = db_client.get_container_client(config.CONTAINER_NAME)

	def create_item(self, observation):
		observationDict = observationToDict(observation)

		try:
			self.__container_client.upsert_item(observationDict)
		except:
			print(observation.id + " could not be upserted")




def observationToDict(observation):
		observationDict = { 'id': observation.id,
							'observationDate': observation.date,
							'region': observation.region,
							'observerType': observation.observer_type,
							'locationName': observation.location_name,
							'latitude': observation.latitude,
							'longitude': observation.longitude,
							'avalancheReported': observation.avalanche_reported,
							'signsOfInstabilityReported':observation.signs_of_instability_reported,
							'notes': observation.notes
						}

		signs_of_instability = None
		avalanches = []

		if (observation.signs_of_instability != None):
			signs_of_instability = { 'shootingCracks': observation.signs_of_instability.shooting_cracks,
									 'collapsingOrWhumpfing': observation.signs_of_instability.collapsing_or_whumpfing
								}
		
		observationDict['signsOfInstability'] = signs_of_instability

		for av in observation.avalanches:
			avalanche = { 'size': av.size,
						  'type': av.type,
						  'intentional':av.intentional,
						  'elevation':av.elevation,
						  'aspect': av.aspect,
						  'comments': av.comments,
						  'cause': av.cause
						}
			avalanches.append(avalanche)


		observationDict['avalanches'] = avalanches

		return observationDict;