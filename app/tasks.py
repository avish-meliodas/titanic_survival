from uuid import uuid4
from fastapi import FastAPI, BackgroundTasks
from app.model_pred import prediction

results = {}

def run_model(data, job_id):
    response = prediction(data)
    results[job_id] = response 

def async_predict(data, background_tasks: BackgroundTasks):
    
    job_id = str(uuid4())
    results[job_id] = None
    
    # result = prediction(data)
    background_tasks.add_task(run_model, data, job_id)
    # results[job_id] = result

    return job_id

def get_results(job_id):
    
    return results.get(job_id)
