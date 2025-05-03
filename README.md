# titanic_survival
This is prediction lightgbm model for the titanic dataset.

titanic_service/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app with endpoints
│   ├── model.py             # Model training and inference
│   ├── schemas.py           # Pydantic models for request/response
│   ├── tasks.py             # Background job for async inference
│   └── utils.py             # Data preprocessing
│
├── data/                    # Titanic dataset (train.csv)
│
├── Dockerfile               # Dockerfile for containerization
├── requirements.txt         # Dependencies
├── README.md                # Instructions
└── train_model.py           # Script to train and save the model

