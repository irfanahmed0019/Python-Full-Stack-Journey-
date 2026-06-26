# 📅 Day 13 – Django Multi-Page Routing & Template Architecture

## 🎯 Goal

Today, I transformed my Django project from a collection of individual HTML pages into a structured multi-page web application using Django's template system, URL routing, and reusable layouts.

---

# 🧠 Topics Covered

- Django Template Inheritance
- `base.html`
- `{% extends %}`
- `{% block %}`
- `{% load static %}`
- Django URL Routing
- `{% url %}`
- Views
- Static Files
- Navigation Between Pages
- Page Anchors (`#section`)
- Project Structure
- HTML Cleanup

---

# 📂 Final Project Structure

```
ecommerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── store/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── product.html
│   ├── cart.html
│   ├── review.html
│   ├── shipping.html
│   ├── payment.html
│   └── confirmed.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py
└── db.sqlite3
```

---

# 🔹 Understanding Template Inheritance

Instead of copying the same HTML into every page, Django allows us to create a reusable layout.

Example:

```
base.html

Header
Navbar

{% block content %}

Footer
```

Every page extends this layout.

Example:

```django
{% extends "base.html" %}
```

This means Django inserts the page content into the `content` block automatically.

Advantages:

- No duplicated code
- Easy maintenance
- Professional project structure
- One edit updates every page

---

# 🔹 Understanding Blocks

Example:

```django
{% block styles %}
{% endblock %}
```

Purpose:

Allows each page to load its own CSS.

Example:

```django
{% block styles %}
<link rel="stylesheet" href="{% static 'css/home.css' %}">
{% endblock %}
```

---

Content Block

```django
{% block content %}
...
{% endblock %}
```

Every page places its unique content here.

---

Scripts

```django
{% block scripts %}
<script src="{% static 'js/home.js' %}"></script>
{% endblock %}
```

Each page can load different JavaScript.

---

# 🔹 Static Files

Instead of writing CSS inside HTML, Django serves files from the `static` folder.

Structure:

```
static/

css/
js/
images/
```

Loading static files:

```django
{% load static %}
```

Example:

```django
<link rel="stylesheet"
href="{% static 'css/home.css' %}">
```

JavaScript

```django
<script src="{% static 'js/home.js' %}"></script>
```

Benefits:

- Better organization
- Easier maintenance
- Reusable assets

---

# 🔹 Django URL Routing

Created multiple views.

Example:

```python
def home(request):
    return render(request,"home.html")
```

Connected them inside

```
store/urls.py
```

Example:

```python
path("", views.home, name="home")
```

Using `name` allows Django to generate URLs dynamically.

---

# 🔹 Using `{% url %}`

Instead of writing

```
href="product.html"
```

we use

```django
href="{% url 'product' %}"
```

Advantages

- Dynamic
- Easy to maintain
- URLs can change without editing HTML

---

# 🔹 Navigation Flow

The complete project flow now works.

```
Home
   ↓
Product
   ↓
Cart
   ↓
Review
   ↓
Shipping
   ↓
Payment
   ↓
Order Confirmed
```

Each page is connected using Django routing.

---

# 🔹 Home Page Sections

Created section IDs.

Example

```html
<section id="hero">
```

```html
<section id="categories">
```

```html
<section id="latest-arrivals">
```

```html
<section id="contact">
```

Navigation now scrolls to sections.

Example

```django
<a href="{% url 'home' %}#categories">
```

This first opens the Home page and then jumps directly to the Categories section.

---

# 🔹 Why We Don't Route `base.html`

`base.html` is not an actual page.

It only contains

- Header
- Navbar
- Footer
- Empty content block

Every page extends it.

```
base.html
      +
home.html
      =
Final Page
```

Therefore, users should never navigate directly to `base.html`.

---

# 🔹 Cleaning the Project

Removed unnecessary duplicate HTML.

Moved:

- Header
- Navbar
- Footer

into

```
base.html
```

Every page now only contains its own content.

---

# 🔹 Problems Faced Today

## Project Structure Mistake

Accidentally moved the Django project into the virtual environment.

Recovered by moving:

- ecommerce/
- store/
- static/
- templates/

back into the project root.

---

## Git Push Issue

GitHub rejected the push because the remote repository already contained commits.

Learned:

```
git clone
```

and proper repository structure.

---

## Invalid HTML

Discovered that

```html
<a>
<button>
```

should not be nested.

Replaced with properly styled anchor tags.

---

## Django Template Routing

Initially tested pages using Live Server.

Realized Django templates only work through

```
python manage.py runserver
```

instead of

```
127.0.0.1:5500
```

---

# 💡 Key Concepts Learned

- Django project architecture
- Reusable templates
- Template inheritance
- Static files
- Dynamic URL generation
- Navigation between pages
- Section anchors
- Project organization
- Debugging routing issues
- HTML cleanup

---

# 📚 What I Learned

Today was less about writing code and more about understanding how a professional Django project is structured.

Instead of duplicating HTML, I learned to build reusable layouts using `base.html`.

I also understood how Django connects:

```
Browser
    ↓
URL
    ↓
urls.py
    ↓
views.py
    ↓
render()
    ↓
Template
```

This helped me understand the complete request-response cycle.

---

# 🚀 Outcome

✅ Created a reusable Django template structure

✅ Connected all pages using Django routing

✅ Organized CSS and JavaScript using the static folder

✅ Built a complete e-commerce navigation flow

✅ Improved project architecture

✅ Gained a much deeper understanding of Django template inheritance and URL routing.

---

# 🔥 Day 13 Summary

Today's work shifted my project from a collection of static HTML pages into a structured Django application.

The biggest lesson was understanding **why** Django uses template inheritance, reusable layouts, and URL routing instead of duplicated HTML.

I also learned that building maintainable software is just as important as making it work.
