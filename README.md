# E-Commerce-Website-Django

This is an e-commerce website built with Django. It provides functionalities for managing user accounts, products, and orders.

## Features

- User registration and authentication(verification email sent to user while registering)
- User profile management
- Product management (create, retrieve, update, delete)
- Product variations (e.g., size, color)
- Product reviews and ratings
- Shopping cart
- Order placement via PayPal
- Product search
- Order confirmation email sent to the user

## Models

- `Account`: Custom user model that uses email for authentication.
- `Product`: Model for storing product data. Each product is associated with a category and can have multiple variations.
- `Variation`: Model for storing product variation data. Each variation is associated with a product.
- `ReviewRating`: Model for storing product review and rating data. Each review is associated with a product and a user.
- `Order`: Model for storing order data. Each order is associated with a user and contains multiple order products.
- `OrderProduct`: Model for storing order product data. Each order product is associated with an order and a product.

## Setup

To get started, clone the repository and then install the required dependencies:

```bash
pip install -r requirements.txt
```
Next, apply the migrations:

```bash
python manage.py migrate
```
Finally, start the development server:

```bash
python manage.py runserver
```
The site will be available at http://127.0.0.1:8000.
