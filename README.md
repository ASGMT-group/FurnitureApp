# Furniture App

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview
The Furniture App is a comprehensive web application designed to provide users with a seamless experience in browsing, purchasing, and managing their furniture purchases. Built using the Django web framework, this project offers a robust set of features that cater to the needs of both customers and administrators.

The primary goal of this project is to create an intuitive and user-friendly platform for individuals and businesses to explore, select, and purchase a wide range of furniture items. The app also includes features for managing orders, inventory, and user accounts, making it a versatile solution for furniture retail and e-commerce.

## Technologies Used
- Python 3.9
- Django 3.2
- Django Forms
- Django Contrib Auth
- SQLite (default database)
- JavaScript
- HTML/CSS
- Bootstrap

## Features
1. **User Registration and Authentication**:
   - Users can register for the app, login, and manage their accounts.
   - Email verification and password reset functionality are included.
2. **Product Catalog**:
   - Customers can browse through a comprehensive catalog of furniture products.
   - Product details, images, and pricing information are displayed.
   - Administrators can manage the product catalog, including adding, updating, and deleting items.
3. **Shopping Cart and Checkout**:
   - Customers can add items to their cart, view the cart contents, and proceed to checkout.
   - The checkout process includes order summary, payment options, and order confirmation.
4. **User Reviews and Ratings**:
   - Customers can leave reviews and ratings for the furniture products they have purchased.
   - Administrators can moderate user reviews and manage the feedback system.
5. **Responsive Design**:
   - The app is designed to be mobile-friendly and accessible across various devices.

## Installation and Setup
1. Clone the repository:
```
git clone https://github.com/your-username/furniture-app.git
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Apply database migrations:
```
python manage.py migrate
```
5. Create a superuser account:
```
python manage.py createsuperuser
```
6. Run the development server:
```
python manage.py runserver
```
The application should now be accessible at `http://localhost:8000`.

## Usage
1. Register a new user account by navigating to the registration page and filling out the form.
2. Log in to the application using your registered email and password.
3. Browse the furniture catalog and add items to your cart.
4. Proceed to the checkout page to complete your order.
5. Manage your user profile, order history, and leave reviews for the furniture you've purchased.
6. Administrators can log in to the admin panel to manage the product catalog, inventory, orders, and user reviews.

## Project Structure
The Furniture App project follows a standard Django project structure, which includes the following key components:

```
FurnitureAppPro/
├── baseapp/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── users/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── FurnitureAppPro/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

The `furniture_app` directory contains the core functionality of the application, including models, views, and URL configurations. The `core` directory holds the project-level settings and URL configurations. The `static` and `templates` directories store the application's static assets and HTML templates, respectively.

## Contributing
Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.
