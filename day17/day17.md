# Day 17 – Django Full Stack Development Journey

**Date:** June 30, 2026

---

# Mission

Today was one of the biggest architecture days of the project. Instead of building new pages, I focused on making the application dynamic, fixing major backend issues, improving authentication, automating product management, and preparing the project for my CodeAlpha internship.

---

# Topics Covered

## Authentication System

### Email Authentication

Implemented complete authentication flow.

- Login
- Signup
- Continue Login
- Forgot Password UI
- Reset Password UI
- Logout
- User Dashboard

Learned:

- authenticate()
- login()
- logout()
- create_user()
- Login decorators
- Session handling

---

## Google Authentication

Integrated Google OAuth using Django Allauth.

Learned:

- Google Cloud Console
- OAuth Client ID
- Redirect URIs
- Django Allauth
- Social Login
- Callback URLs

Debugged:

- Unauthorized callback (401)
- Redirect URI mismatch
- Authentication configuration
- Google provider settings
- Site configuration

Successfully logged into the application using Google.

---

# Checkout System

Completed the complete checkout workflow.

```
Cart
      ↓
Review
      ↓
Shipping
      ↓
Payment
      ↓
Order Confirmation
```

---

## Shipping Address

Implemented shipping address management.

Stored

- Full Name
- Email
- Street
- City
- State
- Pincode

Learned

- get_or_create()
- Updating existing addresses
- Saving user-specific addresses

---

## Payment System

Implemented payment module.

Current methods

- Card
- Cash on Delivery

Database stores

- Payment Method
- Payment Status
- Payment Date

---

## Order System

Implemented complete order creation.

When payment is completed

- Create Payment
- Retrieve Shipping Address
- Read Cart Items
- Create Order
- Create Order Items
- Empty Cart
- Redirect to Confirmation Page

Learned relationship between

```
Order

↓

OrderItem

↓

Product
```

---

# Cart System

Improved shopping cart.

Features

- Add Product
- Increase Quantity
- Decrease Quantity
- Delete Item
- Dynamic Total
- Tax Calculation
- Shipping Calculation
- Grand Total

---

# Product Management

Extended Product Model.

Added

- Category
- Brand
- Stock
- Rating
- Featured Products
- Discount Percentage
- Savings Calculation

Implemented

```
@property
```

for

- Savings
- Discount Percentage

---

# Product Specifications

Created reusable specifications.

Example

```
Display
↓

6.7 inch AMOLED

RAM
↓

16 GB

Battery
↓

5000 mAh
```

---

# Product Gallery

Implemented multiple images per product.

Created

```
ProductImage
```

model.

Used

```
related_name="images"
```

to access gallery images dynamically.

---

# Category System

Created reusable category architecture.

Instead of

```
electronics.html

accessories.html

home-office.html
```

Used

```
category.html
```

for every category.

Implemented

```
/category/electronics/

/category/accessories/

/category/home-office/
```

using one template.

---

# Dynamic Routing

Created

```
category/<slug>/
```

route.

Learned

```
get_object_or_404()

Foreign Keys

Dynamic URL Routing

Context Passing
```

---

# Dynamic Templates

Replaced static HTML with Django template loops.

```
{% for product in products %}

...

{% endfor %}
```

Benefits

- Unlimited products
- Cleaner code
- Database driven
- Easy maintenance

---

# Product Navigation

Every product card now opens its own page.

```
product/<id>/
```

using

```
{% url 'product' product.id %}
```

---

# Admin Panel

Improved Django Admin.

Added

- Search
- Filters
- Featured Products
- Category Management
- Product Specifications
- Product Images

Learned

```
ModelAdmin

TabularInline

list_display

search_fields

list_filter
```

---

# Seed Script

Instead of manually creating products,

Created Python seed script.

Automatically generated

- Products
- Categories
- Pricing
- Stock
- Ratings

Saved hours of manual work.

---

# Product Images Automation

Integrated Pexels API.

Workflow

```
Product

↓

Search API

↓

Download Image

↓

Save

↓

Assign to Product
```

Automated product image population.

---

# Database Design

Current Models

```
Category

Product

Specification

ProductImage

CartItem

ShippingAddress

Payment

Order

OrderItem
```

Strengthened understanding of

- One-to-Many
- Foreign Keys
- Related Names
- Database Relationships

---

# Debugging Experience

Resolved numerous real-world Django issues.

Including

- Google OAuth configuration
- Callback authorization errors
- Duplicate model registration
- Admin registration conflicts
- URL reverse errors
- Template loop mistakes
- Category routing issues
- Migration failures
- Unique constraint errors
- Shipping form field mismatch
- Database IntegrityError
- Dynamic URL context issues
- Product routing problems

---

# Concepts Learned

- Django Authentication
- Google OAuth
- Django Allauth
- Django ORM
- Foreign Keys
- Related Names
- Dynamic Templates
- Template Context
- URL Routing
- Template Inheritance
- Admin Customization
- Model Properties
- QuerySets
- Seed Scripts
- REST-like Routing
- API Integration
- Media Handling
- Database Migrations
- Debugging Django Applications

---

# Project Progress

## Completed

- Responsive Homepage
- Product Detail Page
- Categories
- Dynamic Category Pages
- Shopping Cart
- Review Page
- Shipping
- Payment
- Order Confirmation
- Authentication
- Google Login
- User Dashboard
- Orders
- Addresses
- Payment History
- Login Security
- Product Specifications
- Product Gallery
- Dynamic Product Routing
- Django Admin
- Seed Script
- Automated Product Images

---

# Challenges Faced

- Google OAuth configuration
- Redirect URI mismatch
- Category migration issues
- Dynamic routing errors
- Admin duplicate registration
- Database migration conflicts
- Shipping form validation
- Integrity constraints
- Dynamic template rendering

---

# Git Commit

```bash
feat: complete authentication, Google OAuth, checkout workflow, dynamic category system, product management, admin improvements, seed scripts, and automated product image integration
```

---

# Reflection

Today was focused on transforming the project into a much more complete full-stack application. I implemented authentication, integrated Google OAuth, completed the checkout workflow, automated product creation and image management, improved the Django admin, and converted static pages into reusable dynamic templates. Along the way, I resolved several real-world issues involving migrations, routing, authentication, and database constraints. These debugging sessions strengthened my understanding of Django's architecture and prepared the project as a strong foundation for the CodeAlpha internship.
