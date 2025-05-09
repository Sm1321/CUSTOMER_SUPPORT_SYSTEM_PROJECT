### CUSTOMER SUPPORT SYSTEM PROJECT


##### To create a Enironment
```
 conda create -p env python=3.10 -y
```

##### To activate the environment
```
conda activate env
```

- execute this command on main.py file 
```
uvicorn main:app --reload --port 8001
```



### Steps:-
- Run the ingestion_pipeline.py -> This code all intilization Vector DB  and will push the data into the vectior DB.
- Run the retriveal.py file -> intliaze the API and also from the Vextor Db do the retiver .
- 
