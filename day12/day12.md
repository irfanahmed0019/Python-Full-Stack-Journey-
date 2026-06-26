# Day 11 - Django Template Inheritance & Static Files

## Overview

Today I started learning Django Templates and how professional Django projects avoid duplicating HTML using template inheritance.

Instead of copying the same header, footer, and layout across every page, Django provides a cleaner and more maintainable approach.

---

# Topics Covered

- Django Template Inheritance
- Base Template (`base.html`)
- `{% extends %}`
- `{% block content %}`
- `{% endblock %}`
- `{% load static %}`
- `{% static %}`
- Static Files
- External JavaScript
- Project Structure

---

# Understanding Template Inheritance

Instead of writing this for every page:

```
<!DOCTYPE html>
<html>
<head>
...
</head>
<body>

Header

Page Content

Footer

</body>
</html>
```

Django allows creating a single **base template**.

```
base.html
│
├── Header
├── Navigation
├── Footer
└── Shared Layout
```

Every page simply extends it.

```
home.html

↓

{% extends "base.html" %}
```

This removes duplicated code and makes maintenance much easier.

---

# Block Tags

## Content Block

```django
{% block content %}

Page Content

{% endblock %}
```

The content inside this block is inserted into `base.html`.

---

## Styles Block

```django
{% block styles %}
{% endblock %}
```

Allows each page to load its own CSS.

Example:

```django
<link rel="stylesheet" href="{% static 'css/home.css' %}">
```

---

## Scripts Block

```django
{% block scripts %}
{% endblock %}
```

Allows each page to load only the JavaScript it needs.

Example:

```django
<script src="{% static 'js/home.js' %}"></script>
```

---

# Django Static Files

At the top of the template:

```django
{% load static %}
```

Loading CSS

```django
<link rel="stylesheet" href="{% static 'css/base.css' %}">
```

Loading JavaScript

```django
<script src="{% static 'js/home.js' %}"></script>
```

Loading Images

```django
<img src="{% static 'images/logo.png' %}">
```

---

# Project Structure

```
ecommerce/
│
├── manage.py
├── db.sqlite3
│
├── ecommerce/
│
├── store/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── product.html
│   └── ...
│
└── static/
    ├── css/
    │   └── base.css
    │
    ├── js/
    │   ├── home.js
    │   └── product.js
    │
    └── images/
```

---

# Base Template Structure

```
base.html

HEAD
│
├── Tailwind CDN
├── Google Fonts
├── Tailwind Configuration
├── Base CSS
└── {% block styles %}

BODY
│
├── Header
├── Navigation
├── {% block content %}
├── Footer
└── {% block scripts %}
```

---

# Why Use Template Inheritance?

Without inheritance:

```
Home
Header
Footer

Product
Header
Footer

Cart
Header
Footer
```

The same code is repeated on every page.

With inheritance:

```
base.html
│
├── Header
├── Footer
└── Shared Layout

↓

Home

↓

Product

↓

Cart
```

Changing the header or footer in one place updates every page.

---

# Key Takeaways

- Learned how Django Templates work.
- Understood the purpose of `base.html`.
- Used `{% extends %}` to inherit layouts.
- Used `{% block %}` to insert page-specific content.
- Learned how Django manages static files.
- Moved JavaScript into separate files.
- Built a reusable project structure.

---

# Next Steps

- Convert all remaining pages to use `base.html`.
- Create Django Models.
- Connect the project to the database.
- Display products dynamically from the database.
