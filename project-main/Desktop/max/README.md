# Student Management REST API

A simple Flask API for retrieving and adding student records.

## Setup

PowerShell:

```powershell
.\myenv2\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python app.py
```

The API runs at `http://127.0.0.1:5000`.

## Endpoints

- `GET /students` returns all students.
- `GET /students/<id>` returns one student or `404`.
- `POST /students` adds a student and returns `201`.

POST body:

```json
{
  "name": "Mia Patel",
  "email": "mia.patel@example.com",
  "course": "Data Science"
}
```

## Postman

Import `Student Management API.postman_collection.json` into Postman. Start the Flask server, then run the three requests in the collection. The collection includes response assertions for status codes and response shapes.

## Tests

```powershell
python -m pytest -q
```

Data is stored in memory and resets whenever the server restarts.
