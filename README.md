# Titanic Survival using LightGBM
In this project we built a LightGBM model to predict if a passenger survives on titanic.
The famous Titanic Dataset is used for this project.

## Software and Tools
1. [GithubAccount]
2. [VSCodeIDE]
3. [GitCLI]
4. [Docker]
5. [FastAPI]
6. [LightGBM]

Through FastAPI we will create 2 endpoints as Synchrounous and Asynchrounous APIs.

## Requirements
- Python 3.9 (we will sue Python 3.13)
- Docker

## How to build and run
- Using Docker (Recommended)
1. **Build the Docker image**

```bash
docker build . -t titanic_survival
```
This will build a docker image named ```titanic_survival``` , which we need to run

2. **RUN THE IMAGE**
```bash
docker run -p 5000:8000 titanic_survival
```
This will get the container running. We will talk to our container through port ```5000``` from our localhost which is mapped to port ```8000``` of the ```titanic_survial``` container.

APIs are accesscible at ```http://127.0.0.1/5000``` 

- Run locally (for development)
1. **Clone the repo from github**

```bash
git clone https://github.com/avish-meliodas/titanic_survival.git
```
Make sure you have git CLI installed. This will copy the repository into your local system, into your current directory.

2. **Acticate the virtual environment**
```bash
source venv/bin/activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
To install all required libraries. If you want to add a new library, make sure to add it into the ```requirements.txt``` file.

4. **Train the model**
If you want to re-train the model to generate new model.pkl files, please refer to ```titanic.ipynb``` notebook which contains all EDA part and `model.pkl' files generation.

5. **Run FastAPI**
```bash
uvicorn app.main:app --reload
```
This should get the default port `8000` for FastAPI started.

## How to use APIs

1. **POST /titanic_sync**
Synchronous endpoint for immediate prediction.
Request:
```bash
POST /titanic_sync
Content-Type: application/json

{
  "PassengerId": "string",
  "Pclass": "string",
  "Name": "string",
  "Sex": "string",
  "Age": 0,
  "SibSp": 0,
  "Parch": 0,
  "Ticket": "string",
  "Fare": 0,
  "Cabin": "string",
  "Embarked": "string"
}
```
Response:
```bash
{
  "survived": 0,
  "probability": 0.187
}
```

2. **POST /titanic_async**
Asynchronous endpoint for immediate prediction.
Request:
```bash
POST /titanic_sync
Content-Type: application/json

{
  "PassengerId": "string",
  "Pclass": "string",
  "Name": "string",
  "Sex": "string",
  "Age": 0,
  "SibSp": 0,
  "Parch": 0,
  "Ticket": "string",
  "Fare": 0,
  "Cabin": "string",
  "Embarked": "string"
}
```
Response:
```bash
{
  "job_id": "6efdb6d3-2264-484a-9ba7-7c354909c071"
}
```

3. **GET /titanic_async/{job_id}**
Submits a prediction request that runs in the background.
Response:
```bash
{
  "survived": 0,
  "probability": 0.187
}
```
If the job is still processing:
```bash
{
  "status": "processing"
}
```
