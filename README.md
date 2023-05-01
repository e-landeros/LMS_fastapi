# A Learning Management System in FastAPI

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

## GO TO
``` 
localhost:8000/docs
```
# Alembic Commands. Make database migrations and upgrade or downgrade database
```bash
alembic revision --autogenerate -m "message"
alembic upgrade head
alembic downgrade base
```

## Features
- postgreSQL database
- Alembic migrations
- Pydantic
- SQLAlchemy models
- FastAPI
- REST API
- CRUD operations


## Purpose
This project is a learning management system that allows users to create courses and enroll in courses. It is a REST API that uses FastAPI and PostgreSQL.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Status
Project is: _in progress_

