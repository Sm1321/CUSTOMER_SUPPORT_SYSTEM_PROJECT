## CUSTOMER_SUPPORT_SYSTEM
- This project is based on the RAG and LLM




```
 conda create -p env python=3.10 -y
```
```
conda activate env
```
```
uvicorn main:app --reload --port 8001
```




- Steps:-
- Run the ingestion_pipeline.py -> This code all intilization Vector DB  and will push the data into the vectior DB.
- Run the retriveal.py file -> intliaze the API and also from the Vextor Db do the retiver .
- 
