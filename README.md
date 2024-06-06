#Medicine Information Web App 
## Project Description
 Welcome to the Medicine Information Web App! This Django-based application allows users to browse through a comprehensive list of medicines and view detailed information about each one. Additionally, it includes an admin panel where administrators can manage the medicine database efficiently. 

## Features
-**Browse Medicines: ** Easily search and browse through a wide range of medicines.
 - **Detailed Information: ** View detailed information for each medicine, including generic name, manufacturer, and description.
 - **Admin Panel: ** Manage the medicine database with ease using the built-in admin panel.

### Managing Medicines 
In the admin panel, administrators can:
 - Add new medicines 
- Edit existing medicine details 
- Delete medicines from the database

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
-python latest version (Install python from the website)
-Django (``pip install django `` run this command in comand prompt)
-pip ( package installer)

### Installation

Follow these steps to get a development environment running.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MizanurRahman1234/Medicine-website/tree/master
    ```


3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for accessing the admin site):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Your app should now be running at `http://127.0.0.1:8000/`.

## Usage

### Accessing the Application

- **User View:** Navigate to `http://127.0.0.1:8000/` to start browsing medicines and viewing their details.
- **Admin Panel:** To access the admin panel, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.


