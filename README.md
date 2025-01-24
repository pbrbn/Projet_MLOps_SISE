# Iris Classification Project with Docker, Streamlit, and FastAPI  

## Overview  
This project demonstrates an end-to-end Machine Learning workflow using Docker containers. The application consists of a client interface for entering iris flower characteristics and a server backend hosting a machine learning model (RandomForestClassifier) trained on the Iris dataset.  

The system is designed using:  
- **Streamlit** for the client-side application.  
- **FastAPI** for the server-side API.  
- **Docker** to containerize both the client and server applications.  
- **Docker Compose** to orchestrate the multi-container deployment.  

---

## Project Structure  

```plaintext
project-root/
│
├── client/
│   ├── Dockerfile           # Docker configuration for the client app
│   ├── app.py               # Streamlit application to input iris characteristics
│   ├── requirements.txt     # Python dependencies for the client
│
├── server/
│   ├── Dockerfile           # Docker configuration for the server app
│   ├── app.py               # FastAPI application serving predictions
│   ├── train.py             # Script to train the RandomForestClassifier model
│   ├── model.pkl            # Serialized model file
│   ├── requirements.txt     # Python dependencies for the server
│
├── docker-compose.yml       # Docker Compose configuration for multi-container setup
```

## How it works 

### Client Application (Streamlit)  
- A user-friendly interface to input iris flower characteristics: sepal length, sepal width, petal length, and petal width.  
- Sends a POST request to the server API with the input data.  

### Server Application (FastAPI)  
- Hosts the trained `RandomForestClassifier` model.  
- Provides a REST API endpoint to predict the iris species based on the input characteristics.  

### Model Training (`train.py`)  
- The `train.py` script trains the model on the Iris dataset and saves it as `model.pkl`.  

### Docker Compose  
- Orchestrates the deployment of the client and server applications in separate Docker containers.  

---

## Setup and Usage  

### Prerequisites  
Ensure that you have the following installed on your system:  
- Docker  
- Docker Compose  

### Steps  

1. **Clone the repository**  
   ```bash  
   git clone <repository-url>  
   cd project-root/
   ```

2. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
- Open the client application in your browser: http://localhost:8501
- The server API is accessible at: http://localhost:8000/docs

4. **Interacting with the Application**
- Use the Streamlit interface to input the iris flower's features.
- The client sends a request to the FastAPI server, which responds with the predicted iris species.

## Devs Details 

### Client Application

- Framework: Streamlit
- Key Features:
 - Form to input iris flower features.
 - Communication with the server via POST requests.

### Server Application 

- Framework: FastAPI
- Key Features:
 - /predict endpoint to handle prediction requests.
 - Loads a pre-trained RandomForestClassifier model.

### Model Training

- Dataset: Iris Dataset from sklearn.datasets.
- Algorithm: RandomForestClassifier.
- Output: A serialized model (model.pkl) for inference.

## File Explanations 

- client/Dockerfile: Sets up the environment for the Streamlit app.
- server/Dockerfile: Sets up the environment for the FastAPI app and loads the model.
- train.py: Trains the RandomForestClassifier on the Iris dataset and saves the model.
- docker-compose.yml: Configures the deployment of both containers, linking the client and server.

## Sample Commands

- Rebuilding Containers :
  ```bash
  docker-compose build
  ```

- Shutting Down :
  ```bash
  docker-compose down
  ```

## Author : 

Pierre BOURBON

