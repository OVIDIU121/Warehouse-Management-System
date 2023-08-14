# Warehouse Management Web Application

This repository has been created as part of my final project for the University of Roehampton.
This repository contains the source code for a web-based warehouse management application, designed to help users efficiently manage warehouse operations. 
The application aims to provide a user-friendly interface, secure authentication, and seamless interaction with a back-end database.

## Table of Contents
- [Introduction](#introduction)
- [Project Specifications](#project-specifications)
- [Development Platform](#development-platform)
- [Getting Started](#getting-started)
- [Features](#features)


## Introduction
The Warehouse Management Web Application is developed with the goal of streamlining warehouse management processes.
It provides users with the ability to manage inventory, track shipments, and oversee various aspects of warehouse operations through an intuitive web interface.

## Project Specifications
The project focuses on the following specifications:
- **Web Application:** The primary objective is to deliver a user-friendly web-based application that simplifies warehouse management tasks and offers a polished user experience.
- **Secure Authentication:** Users can create accounts, securely log in, and manage sessions, ensuring sensitive information is protected.
- **Back-end Database:** The application is backed by a scalable and efficient database that efficiently stores warehouse data.

## Development Platform
The Warehouse Management Web Application is built based on the following requirements:
- asgiref==3.6.0
- autopep8==2.0.2
- beautifulsoup4==4.12.2
- Django==4.2
- django-bootstrap-v5==1.0.11
- django-filter==23.1
- djangorestframework==3.14.0
- Markdown==3.4.3
- psycopg2-binary==2.9.6
- pycodestyle==2.10.0
- pytz==2023.3
- soupsieve==2.4.1
- sqlparse==0.4.4
- tomli==2.0.1
- tzdata==2023.3
- whitenoise==6.4.0


## Getting Started
To set up and run the Warehouse Management Web Application locally, follow these steps:
1. Clone this repository to your local machine.
2. Install Python 3.7+ and PostgreSQL 12.0+ if not already installed.
3. Set up a virtual environment using your preferred tool (e.g., virtualenv).
4. Activate the virtual environment.
5. Navigate to the project's backend directory and install backend dependencies using `pip install -r requirements.txt`.
6. Create a PostgreSQL database and configure the database settings in the backend's settings file.
7. Apply migrations to set up the database schema: `python manage.py migrate`.
8. Navigate to the project's frontend directory and install frontend dependencies using your preferred package manager.
9. Build the frontend assets using the appropriate build command for your frontend framework.
10. Start the development server for both the backend and frontend.

## Features
- User-friendly web interface for managing warehouse operations.
- Secure user authentication and session management.
- Efficient storage and retrieval of warehouse data from the database.
- Interactive dashboard to visualize inventory and shipment status.

## Web Application structure
- based on the deployment of the application on AWS
![image](https://github.com/OVIDIU121/Warehouse-Management-System/assets/94175010/563b57c8-aa24-4a35-a90f-d2aa1d35af5a)



For any questions or support, please contact me.
