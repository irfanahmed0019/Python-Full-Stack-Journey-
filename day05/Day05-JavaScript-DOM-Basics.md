# 🚀 Day 05 - JavaScript Fundamentals & DOM Manipulation

## 📖 Overview

Today I learned the fundamentals of JavaScript and how it interacts with HTML using the DOM (Document Object Model).

Unlike HTML and CSS, which create and style web pages, JavaScript allows websites to respond to user actions and become interactive.

---

# What is JavaScript?

JavaScript is a programming language used to add behavior and interactivity to websites.

### Examples

- Button Click Events
- Popups
- Form Validation
- Counters
- Image Sliders
- Dark Mode
- Interactive Dashboards

---

# Connecting JavaScript to HTML

### External JavaScript File

```html
<script src="script.js" defer></script>
```

## Understanding the Attributes

### `script`

Used to load JavaScript into an HTML page.

### `src`

Specifies the file path of the JavaScript file.

```html
<script src="script.js"></script>
```

### `defer`

Tells the browser:

```text
Download JavaScript now
↓
Run it after HTML finishes loading
```

This prevents errors when JavaScript tries to access HTML elements before they exist.

---

# Functions

A function is a reusable block of code that performs an action.

### Example

```javascript
function showAlert() {
    alert("Welcome to JavaScript!");
}
```

## Mental Model

```text
Function
↓
Named Action
↓
Can be executed whenever needed
```

---

# onclick Event

Used to run JavaScript when a button is clicked.

### Example

```html
<button onclick="showAlert()">
    Click Me
</button>
```

## Flow

```text
Button Click
↓
onclick
↓
Function Runs
↓
Action Happens
```

---

# Alert Popup

### Example

```javascript
alert("Welcome to JavaScript!");
```

### Purpose

Display a popup message.

### Output

```text
Welcome to JavaScript!
```

---

# Understanding the DOM

DOM stands for:

**Document Object Model**

The browser converts HTML into a structure that JavaScript can access and modify.

### Example HTML

```html
<h1>Day 05 JavaScript</h1>
<button>Click Me</button>
<p>Hello</p>
```

### Browser DOM

```text
document
│
├── h1
├── button
└── p
```

---

# DOM Manipulation

DOM Manipulation means changing webpage content using JavaScript.

### Examples

- Change Text
- Change Colors
- Hide Elements
- Show Elements
- Change Images
- Update Counters

---

# document.getElementById()

Used to find an HTML element using its ID.

### HTML

```html
<p id="message">
    Hello
</p>
```

### JavaScript

```javascript
document.getElementById("message");
```

### Meaning

```text
Find the element whose ID is "message"
```

---

# innerHTML

Used to change the content inside an HTML element.

### Example

```javascript
document.getElementById("message").innerHTML =
"Welcome to JavaScript!";
```

### Before

```text
Hello
```

### After

```text
Welcome to JavaScript!
```

---

# Changing Text with JavaScript

### Example

```javascript
function showMessage() {
    document.getElementById("message").innerHTML =
    "Welcome to JavaScript!";
}
```

### Flow

```text
Click Button
↓
Find Element
↓
Replace Content
↓
Display New Text
```

---

# Hiding Elements

### Example

```javascript
document.getElementById("message").style.display =
"none";
```

### Meaning

```text
Hide the element
```

---

# Changing Colors

### Example

```javascript
document.getElementById("one").style.backgroundColor =
"red";
```

### Meaning

```text
Change the button background color
```

---

# Changing Images

### HTML

```html
<img id="photo">
```

### JavaScript

```javascript
document.getElementById("photo").src =
"image-url";
```

### Meaning

```text
Replace the image source
```

---

# Variables

Variables store data.

### Example

```javascript
let count = 0;
```

### Meaning

```text
Create a box
↓
Store value 0
```

---

# Counter Application

### Example

```javascript
let increment = 0;

function incount() {
    increment++;
    document.getElementById("count").innerHTML =
    increment;
}
```

---

# Understanding ++

```javascript
increment++;
```

Means:

```javascript
increment = increment + 1;
```

### Output

```text
0
↓
1
↓
2
↓
3
```

---

# Reading User Input

### HTML

```html
<input type="text" id="username">
```

### JavaScript

```javascript
document.getElementById("username").value;
```

### Meaning

```text
Get what the user typed
```

### Example

User Types:

```text
Irfan
```

JavaScript Reads:

```text
Irfan
```

---

# Username Greeting Project

### HTML

```html
<input type="text" id="username">
<button onclick="hello()">Submit</button>
```

### JavaScript

```javascript
function hello() {
    alert(
        "Hello " +
        document.getElementById("username").value
    );
}
```

### Example Output

```text
Hello Irfan
```

---

# Key Concepts Learned Today

- ✅ JavaScript Basics
- ✅ Functions
- ✅ onclick Events
- ✅ alert()
- ✅ DOM
- ✅ document
- ✅ getElementById()
- ✅ innerHTML
- ✅ style.display
- ✅ style.backgroundColor
- ✅ src
- ✅ Variables
- ✅ ++ Operator
- ✅ User Input
- ✅ value
- ✅ Counter Logic

---

# Biggest Lesson

```text
HTML
↓
Creates the Structure

CSS
↓
Styles the Structure

JavaScript
↓
Changes the Structure
```

---

# Mental Model

Almost every modern website feature follows this pattern:

```text
Find Element
↓
Modify Element
↓
User Sees Result
```

This is the foundation of frontend web development and DOM manipulation.

---

# 🧠 Day 05 Summary

JavaScript makes websites interactive.

The core workflow is:

```text
User Action
↓
JavaScript Function
↓
DOM Manipulation
↓
Updated Web Page
```

Today I learned how to:

- Connect JavaScript to HTML
- Create and use functions
- Handle button click events
- Show alerts
- Access HTML elements using IDs
- Change text dynamically
- Hide and style elements
- Change images
- Store data using variables
- Build a counter
- Read user input
- Create interactive web pages
