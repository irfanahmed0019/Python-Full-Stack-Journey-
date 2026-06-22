# Day 09 - Understanding Dynamic Websites with JavaScript

## 🚀 Overview

Today was one of the most important days in my Full Stack Development journey.

Instead of building a new project from scratch, I used my existing **ARCHERS website** as a learning laboratory.

The original website was already completed and safely backed up on GitHub, so I started intentionally breaking parts of it to understand how modern websites work behind the scenes.

This helped me move from simply editing code to understanding the relationship between:

```text
Data → JavaScript → DOM → UI
```

---

# 🎯 Objective

Understand how websites can create and update content dynamically without manually editing HTML every time.

---

# 🧠 Key Concepts Learned

## 1. Arrays

Arrays store multiple values.

Example:

```javascript
const events = [
    "Event 1",
    "Event 2",
    "Event 3"
];
```

Think of an array as a container that holds multiple items.

---

## 2. Objects

Objects store related information together.

Example:

```javascript
const event = {
    title: "Mini Militia Tournament",
    description: "Gaming competition"
};
```

Objects use:

```text
key : value
```

pairs.

---

## 3. Arrays of Objects

This is commonly used in web development.

```javascript
const events = [
    {
        title: "Mini Militia Tournament",
        description: "Gaming Event"
    },
    {
        title: "Design With AI",
        description: "Workshop"
    }
];
```

This structure allows websites to store multiple records efficiently.

---

## 4. JavaScript Loops

### forEach()

Used to loop through every item in an array.

```javascript
events.forEach(event => {
    console.log(event.title);
});
```

Flow:

```text
events
 ↓
Event 1
 ↓
Event 2
 ↓
Event 3
```

The code inside the loop runs once for every item.

---

## 5. Understanding `events` vs `event`

This was one of my biggest questions today.

```javascript
events.forEach(event => {
});
```

### events

Entire array

```javascript
events
```

Contains:

```text
Event 1
Event 2
Event 3
```

---

### event

Single item currently being processed

```javascript
event
```

Example:

```javascript
event.title
```

returns:

```text
Mini Militia Tournament
```

Important:

The name `event` is just a variable name.

This would also work:

```javascript
events.forEach(item => {
    console.log(item.title);
});
```

or even:

```javascript
events.forEach(k => {
    console.log(k.title);
});
```

---

## 6. DOM (Document Object Model)

The browser converts HTML into a structure called the DOM.

Example:

```html
<div id="events-container"></div>
```

JavaScript can find and modify elements inside the DOM.

---

## 7. Selecting HTML Elements

```javascript
document.getElementById("events-container")
```

Meaning:

```text
Find the HTML element
whose id is "events-container"
```

---

## 8. innerHTML

Used to insert HTML using JavaScript.

Example:

```javascript
container.innerHTML = "<h1>Hello</h1>";
```

Result:

```html
<h1>Hello</h1>
```

appears on the page.

---

## 9. Template Literals

Template literals use backticks.

```javascript
`
Hello
`
```

Unlike normal strings, they allow:

- Multiple lines
- Variable insertion

---

## 10. `${}`

Used to insert JavaScript values into HTML.

Example:

```javascript
`${event.title}`
```

If:

```javascript
event.title = "Mini Militia Tournament"
```

Result:

```html
Mini Militia Tournament
```

---

## 11. Dynamic HTML Generation

Instead of manually writing:

```html
<h2>Event 1</h2>

<h2>Event 2</h2>

<h2>Event 3</h2>
```

JavaScript can generate everything automatically.

Example:

```javascript
events.forEach(event => {

    container.innerHTML += `
        <h2>${event.title}</h2>
    `;

});
```

Flow:

```text
Data
 ↓
JavaScript
 ↓
HTML
 ↓
UI
```

---

## 12. Conditional Rendering

Today I also learned how to display content only when it exists.

Example:

```javascript
${event.image ? `<img src="${event.image}">` : ""}
```

Meaning:

```text
If image exists
    Show image

Else
    Show nothing
```

This prevents broken image links.

---

## 13. Tailwind CSS Classes

Example:

```html
class="w-full"
```

Equivalent CSS:

```css
width: 100%;
```

Examples:

```text
w-full      → width:100%
p-8         → padding
border      → border
bg-white    → white background
text-black  → black text
```

---

# 🔨 Practical Exercise Performed

I used my ARCHERS website as a sandbox environment.

Original website:

```text
Hardcoded Event Cards
```

Example:

```html
<h3>MINI MILITIA TOURNAMENT</h3>
```

Everything was manually written.

---

## Step 1

Created an event array.

```javascript
const events = [
    {
        title:"MINI MILITIA TOURNAMENT",
        description:"Gaming Event"
    }
];
```

---

## Step 2

Created an empty container.

```html
<div id="events-container"></div>
```

---

## Step 3

Used JavaScript to generate HTML dynamically.

```javascript
events.forEach(event => {

    container.innerHTML += `
        <div>
            <h2>${event.title}</h2>
            <p>${event.description}</p>
        </div>
    `;

});
```

---

## Step 4

Added new events using:

```javascript
events.push({
    title:"TYPING SPEED CHALLENGE",
    description:"Test your speed"
});
```

Without touching HTML, a new card appeared automatically.

This was the biggest breakthrough of the day.

---

## Step 5

Added images dynamically.

```javascript
<img src="${event.image}">
```

Then improved it using conditional rendering:

```javascript
${event.image ? `<img src="${event.image}" class="w-full">` : ""}
```

---

# 🐛 Bugs Encountered

## Bug 1

Wrong method name

```javascript
getElementbyId
```

Fixed:

```javascript
getElementById
```

---

## Bug 2

Wrong variable

```javascript
conatiner
```

Fixed:

```javascript
container
```

---

## Bug 3

Used:

```javascript
events.title
```

instead of:

```javascript
event.title
```

Learned the difference between array and item.

---

## Bug 4

Broken images caused by:

```javascript
event.image
```

not existing for every event.

Solved using conditional rendering.

---

# 💡 Biggest Lesson

A website does not need to store every piece of content directly inside HTML.

Modern websites often work like this:

```text
Database
 ↓
API
 ↓
JSON
 ↓
JavaScript
 ↓
DOM
 ↓
UI
```

Today I recreated a simplified version of this workflow using plain JavaScript.

---

# 🎯 Key Takeaway

Before today, I viewed websites as:

```text
HTML
CSS
JavaScript
```

After today, I understand them more like:

```text
Data
 ↓
Logic
 ↓
DOM
 ↓
User Interface
```

Understanding this concept is the foundation behind:

- React
- Vue
- Angular
- Flask Templates
- Django Templates
- Modern Web Applications

---

## Day 09 Status

✅ Arrays

✅ Objects

✅ forEach()

✅ DOM Manipulation

✅ Template Literals

✅ Dynamic HTML Generation

✅ Conditional Rendering

✅ Tailwind Classes

✅ Debugging Real Project Code

✅ Understanding Data → UI Flow

---

### GitHub Repository

Python Full Stack Journey

Day 09 Completed ✅
