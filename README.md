# E-Commerce-Website-Django

This project is a comprehensive e-commerce website built with Django from [Udermy Course](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/learn/lecture/36526812?start=585#reviews)

## Features

- User Registration and Authentication: Users can register for an account using their email address. A verification email is sent upon registration to ensure the validity of the email address.
- User Profile Management: Users can manage their profile information, providing a personalized shopping experience.
- Product Management: Admins can create, retrieve, update, and delete products. This includes managing product variations such as size and color.
- Product Reviews and Ratings: Users can leave reviews and ratings for products, providing valuable feedback for both the seller and other customers.
- Shopping Cart: Users can add products to a shopping cart, allowing them to manage their desired purchases.
- Order Placement via PayPal: Users can place orders using PayPal, providing a secure and convenient payment method.
- Product Search: Users can search for products, making it easy to find exactly what they're looking for.
- Order Confirmation Email: Upon placing an order, users receive a confirmation email, providing them with a record of their purchase.

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
