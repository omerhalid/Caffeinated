# Caffeinated

Caffeinated is a Django web application that provides a platform for coffee lovers to find cafes with amenities like good coffee, WiFi, and power outlets. It's an ideal resource for freelancers, students, and anyone who enjoys working or relaxing in a cafe environment.

## Features

- Browse a list of cafes with detailed information.
- Add new cafe entries through a user-friendly form.
- Interactive, responsive design for a seamless browsing experience.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running:

Clone the repository:

```bash

git clone https://github.com/yourusername/caffeinated.git
cd caffeinated
```

Set up the database:

```bash

python manage.py migrate

Create a superuser:
```

```bash

python manage.py createsuperuser

Start the development server:
```

```bash

python manage.py runserver

Now, the server should be running on http://127.0.0.1:8000/
```

### Deployment

Add additional notes about how to deploy this on a live system.
Built With

    Django - The web framework used
    Bootstrap - The front-end library used for responsive design

