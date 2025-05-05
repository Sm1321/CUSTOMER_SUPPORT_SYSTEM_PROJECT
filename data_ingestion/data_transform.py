import pandas as pd
from langchain_core.documents import Document

# Class
class data_converter:
    def __init__(self):
        print("Data Convertor has been init...")
        self.product_data = pd.read_csv(r"C:\MY_Folder\MY_Courses\1.GEN_AI_LIVE_Classes\ipynb_files\CUSTOMER_SUPPORT_SYSTEM\data\flipkart_product_review.csv")
        print(self.product_data.head())

    def data_transformation(self):
        requried_columns = self.product_data.columns
        requried_columns = list(requried_columns[1:])
        # print(requried_columns)
        #Itertaing to the data by this below
        product_list = []
        for index,row in self.product_data.iterrows():
            object = {
                "product_name":row['product_title'],
                "product_rating":row['rating'],
                "product_summary":row['summary'],
                
                "product_review":row['review']
            } 
            product_list.append(object)
        # print("************************Below is My Product List*********************")    
        # print(product_list[0])   
        # Iterating to the product list
        docs = []
        for entry in product_list:
            metadata = {"product_name":entry['product_name'],
                        "product_rating":entry['product_rating'],
                        "product_summary":entry['product_summary'],
                        }
            doc = Document(page_content = entry['product_review'],metadata = metadata)
            docs.append(doc)
        print(docs[0])
        #return docs  
        

if __name__ == '__main__':
    data_con = data_converter()
    print("The Columns Names:-\n")
    data_con.data_transformation()
