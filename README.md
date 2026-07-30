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

```text
![Stage 3 CMD Prompt](/Screenshots/Stage3.png)