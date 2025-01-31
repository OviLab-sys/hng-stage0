HNG Public API

Description

This is a simple public API developed for HNG12 that returns JSON-formatted information, including:

My registered email address on the HNG12 Slack workspace.

The current datetime in ISO 8601 format (UTC).

The GitHub URL of this project's codebase.

This API is built using Django and is deployed on Render.

Technology Stack

Programming Language: Python

Framework: Django

Deployment Platform: Render

Version Control: GitHub

CORS Handling: Configured for cross-origin requests

API Specification

Endpoint

Method: GET

URL: https://hng-stage0-e6an.onrender.com/

Response Format (200 OK)

{
  "email": "victoroduorr@gmail.com",
  "current_datetime": "2025-01-31T07:32:29.982088+00:00",
  "github_url": "https://github.com/OviLab-sys/hng-public-API"
}

Setup Instructions

Prerequisites

Ensure you have the following installed:

Python (3.11+)

pip (Python package manager)

Git

Virtual environment (venv)

Installation Steps

Clone the repository:

git clone https://github.com/OviLab-sys/hng-public-API.git
cd hng-public-API

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/

Deployment

The application is deployed on Render. To deploy your own version:

Push your code to GitHub.

Create a new Render web service.

Set environment variables if necessary.

Deploy and access your API at the given Render URL.

API Documentation

Base URL

Production: https://hng-stage0-e6an.onrender.com/

Localhost: http://127.0.0.1:8000/

Endpoints

Method

Endpoint

Description

GET

/

Returns JSON response with email, current UTC datetime, and GitHub URL

Example Usage

Using cURL:

curl -X GET https://hng-stage0-e6an.onrender.com/

Using Python requests:

import requests
response = requests.get("https://hng-stage0-e6an.onrender.com/")
print(response.json())

References

Django Documentation