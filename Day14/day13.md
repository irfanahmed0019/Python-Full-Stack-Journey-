# Day 14 – Building a Real E-Commerce Shopping Experience

**Date:** 27 June 2026

---

## Overview

Today was one of the biggest backend-focused learning days so far.

At first, I assumed building an e-commerce website was mostly about creating pages with HTML and CSS. After implementing real shopping cart functionality, product galleries, and database relationships, I realized that most of the complexity actually exists in the backend.

Many features that look simple to users require multiple models, views, database queries, templates, JavaScript interactions, and debugging behind the scenes.

---

# Features Completed

## Product Specifications

Implemented a dedicated `Specification` model linked to each product.

Each product can now have multiple specifications such as:

- Display Size
- Resolution
- Refresh Rate
- Processor
- RAM
- Storage

The specifications are rendered dynamically on the product page using Django template loops.

---

## Automatic Savings Calculation

Added a property inside the `Product` model:

- savings

The savings amount is now calculated automatically from:

Original Price − Discounted Price

instead of manually entering it.

---

## Automatic Discount Percentage

Added another property:

- discount_percentage

The percentage discount is calculated automatically using the product prices.

This removes duplicated data and keeps pricing consistent.

---

## Multiple Product Images

Created a new database model:

- ProductImage

Each product can now contain:

- Main image
- Multiple gallery images

instead of only a single image.

---

## Dynamic Product Gallery

Replaced static gallery images with database-driven images.

Used:

```django
{% for image in product.images.all %}
```

to render all gallery images dynamically.

---

## Image Switching with JavaScript

Implemented thumbnail selection similar to Amazon.

When a thumbnail is clicked:

- JavaScript detects the click
- Reads the image URL
- Replaces the main product image

No page refresh is required.

---

## Django Admin Improvements

Implemented Django Admin Inlines.

Now Specifications and Product Images can be managed directly inside the Product admin page.

Instead of opening multiple admin pages, everything can be managed from one location.

---

## Shopping Cart Improvements

Implemented:

- Add to Cart
- Increase Quantity
- Decrease Quantity
- Automatic Total Price Calculation

The cart now updates based on quantity.

---

## Dynamic Cart Badge

Created a Django Context Processor.

The cart quantity is now visible globally inside the navigation bar.

Example:

🛒 3

instead of a static cart icon.

---

## Dynamic Cart Rendering

Replaced hardcoded cart products with database-driven data.

The cart page now loops through:

```django
{% for item in cart_items %}
```

and displays:

- Product Image
- Product Name
- Brand
- Quantity
- Price
- Stock Status

---

## Product Navigation

Users can now click product images inside the cart and return directly to the product page.

---

# Concepts Learned

Today I learned much more than writing code.

## Django Relationships

- ForeignKey
- related_name
- CASCADE
- SET_NULL

---

## Django Properties

Using:

```python
@property
```

to create calculated fields without storing duplicate values.

---

## Django Admin Inlines

Managing related models from a single admin page.

---

## Context Processors

Making shared data (cart count) available across every page.

---

## Dynamic Templates

Rendering database content using:

- for loops
- if statements
- related models

instead of static HTML.

---

## JavaScript DOM Manipulation

Using JavaScript to update the product gallery dynamically without reloading the page.

---

# Biggest Realization Today

Today completely changed how I think about web development.

To a normal user:

- Click product
- Add to cart
- Increase quantity

looks like a very simple website.

But behind those few clicks are:

- Database models
- Django views
- URL routing
- Template rendering
- JavaScript
- Foreign Keys
- Context Processors
- Database updates
- Dynamic calculations

The better the software feels to users, the more invisible the engineering becomes.

---

# Challenges Faced

- Django migration issues
- ForeignKey relationship mistakes
- Static JavaScript loading errors
- Thumbnail gallery implementation
- Template syntax errors
- URL routing mistakes
- Dynamic cart rendering
- Context Processor debugging

Each issue was solved through debugging and understanding how Django works internally.

---

# Tomorrow's Plan (Day 15)

- Django Authentication
- Amazon-style Login Flow
- User Registration
- User Login
- Logout
- Google Authentication
- User-specific Shopping Cart
- Connect Cart with Django Users

---

# GitHub Commit

```
feat: implement dynamic product gallery, shopping cart improvements and admin inlines
```

---

# Reflection

Only 14 days ago I was learning basic HTML.

Today I built features found in real e-commerce platforms:

- Dynamic product pages
- Multiple product galleries
- Shopping cart logic
- Automatic pricing
- Django admin customization
- Database relationships

This project is helping me understand how real-world web applications work—not just how they look.
