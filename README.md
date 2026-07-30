# Flyrank Task API

A CRUD API for managing a to-do list, built with Python and FastAPI. 

## How to Install & Run
To start the server on your local machine, activate the virtual environment and run the following command:
`uvicorn main:app --reload`

## Endpoints

| Operation | HTTP Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **API Info** | GET | `/` | Returns API name and version |
| **Health Check** | GET | `/health` | Checks if the server is alive |
| **Read All** | GET | `/tasks` | Returns a list of all tasks |
| **Read One** | GET | `/tasks/{id}` | Returns a single task by ID |
| **Create** | POST | `/tasks` | Creates a new task |
| **Update** | PUT | `/tasks/{id}` | *Pending Stage 4* |
| **Delete** | DELETE | `/tasks/{id}` | *Pending Stage 4* |

## Example Request & Response

### Stage 1
#### GET
![GET CMD](/Screenshots/Stage1.png)

### Stage 2
#### GET one task by id
![GET1 CMD](/Screenshots/Stage2.png)

### Stage 3
#### POST
![POST CMD](/Screenshots/Stage3.png)

### Stage 4
#### PUT
![PUT CMD](/Screenshots/Stage4%20PUT.png)
#### DELETE
![DELETE CMD](/Screenshots/Stage4%20DELETE.png)

### Stage 5
#### SwaggerUI
See the [assignment brief (SwaggerUI)](SwaggerUI.pdf) for details.