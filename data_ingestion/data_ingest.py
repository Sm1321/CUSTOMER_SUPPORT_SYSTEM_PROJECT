from langchain_astradb import AstraDBVectorStore 
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter


load_dotenv() 



class ingest_data:
    def __init__(self):
        print("Data Ingestion class has init...")
    def data_ingestion(self):
        pass


    def _load_env_variables(self):
            """
            Load and validate required environment variables.
            """
            load_dotenv()
            
            required_vars = ["GOOGLE_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
            
            missing_vars = [var for var in required_vars if os.getenv(var) is None]
            if missing_vars:
                raise EnvironmentError(f"Missing environment variables: {missing_vars}")
            
            self.google_api_key = os.getenv("GOOGLE_API_KEY")
            self.db_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
            self.db_application_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
            self.db_keyspace = os.getenv("ASTRA_DB_KEYSPACE")


    def data_ingestion(self,status):
            vstore = AstraDBVectorStore(
                embedding = self.embedding,
                collection = "chatbotecom",
                api_endpoint = ASTRA_DB_API_ENDPOINT,
                token = ASTRA_AB_APPLICATION_TOKEN,
                namespace = ASTRA_DB_KEYSPACE,

            ) 
            storage = status

            if storage == None:
                 docs = self.data_convertor.data_transformation()
                 inserted_ids = vstore.add_documnets(docs)
                 print(inserted_ids)
            else:
                 return vstore 
            
            return vstore,inserted_ids              

    

### this is the main function

if __name__ == '__main()__':
    data_ingestion = ingest_data()
