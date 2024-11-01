# 🐾 Spy Cat Agency Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-3.x-green)
![Django REST Framework](https://img.shields.io/badge/DRF-3.x-lightgrey)

## 📖 Overview
The **Spy Cat Agency Application** is designed to manage spy cats, missions, and targets efficiently. Built with **Django** and **Django REST Framework**, it provides a robust RESTful API for performing CRUD (Create, Read, Update, Delete) operations on the core models of the application.

## 🚀 Features
- **Manage Spy Cats**: Keep track of all your spy cats and their details.
- **Mission Control**: Create, assign, and track missions effectively.
- **Target Management**: Handle targets and their statuses with ease.
- **RESTful API**: Seamlessly interact with the application via API endpoints.

## 🛠️ Requirements
- **Python**: Ensure you have Python 3.x installed on your machine.
- **Django**: This project uses Django as the web framework.
- **Django REST Framework**: Essential for building the API endpoints.
- **Requests**: Required to handle external API calls for breed validation.

## 📚 Setup Instructions

### Clone the Repository
```
git clone <repository-url>
cd spy_cat_agency
```
Install Dependencies:
Manually install the necessary packages

```
pip install django djangorestframework requests
```

Apply Migrations:
Set up the necessary database tables
```
python manage.py migrate
```
Run the Development Server:
Start the Django development server
```
python manage.py runserver
```

API Endpoints:
After starting Django development server explore the API endpoints using Postman
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/39434734-ded9a1e8-e43a-439d-b736-357398b67d5b?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D39434734-ded9a1e8-e43a-439d-b736-357398b67d5b%26entityType%3Dcollection%26workspaceId%3D80060c85-07cc-4e69-a0bb-465a89881d72)
