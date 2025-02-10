# Text-Based Blog Website

## Overview
This project is a lightweight and efficient text-based blog website built using Reflex. It provides a simple yet powerful platform for users to create, edit, and manage blog posts seamlessly. Designed with minimalism and ease of use in mind, it ensures a smooth blogging experience with database-backed storage for content persistence.

## Features
- **Simple and Intuitive UI**: A clean and distraction-free interface for writing and managing blog posts.
- **Database Integration**: Secure and reliable data storage for posts.
- **Virtual Environment Support**: Easy setup with isolated dependencies.
- **Seamless Migration**: Smooth database initialization and migration processes.
- **Fast and Lightweight**: Optimized for performance with Reflex framework.
- **Cross-Platform Compatibility**: Works on both Windows and Linux/Mac systems.
- **Docker Support**: Easily deploy and run the project in a containerized environment.

## Installation and Setup
Follow the steps below to run the project on your local machine.

### 1. Create a Virtual Environment
Create a virtual environment to manage dependencies.
```sh
py -m venv env
```

### 2. Activate Virtual Environment
- On **Windows**:
  ```sh
  env\Scripts\activate
  ```
- On **Linux/Mac**:
  ```sh
  source env/scripts/activate
  ```

### 3. Install Required Dependencies
Use `pip` to install all required dependencies.
```sh
pip install -r requirements.txt
```

### 4. Initialize Database
Create and apply database migrations.
```sh
reflex db makemigrations
reflex db migrate
```

### 5. Initialize Project
Set up the project with Reflex.
```sh
reflex init
```

### 6. Run the Application
Start the application using the following command:
```sh
reflex run
```

## Docker Setup
You can also run this project inside a Docker container.

### 1. Build the Docker Image
```sh
docker build -t text-based-blog .
```

### 2. Run the Docker Container
```sh
docker run -p 8000:8000 text-based-blog
```

### 3. Using Docker Compose (Optional)
If you have a `docker-compose.yml` file, you can run the project with:
```sh
docker-compose up -d
```
