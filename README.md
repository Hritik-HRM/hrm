# Flask Project: Day 1 Tasks

## Task 1: Display Multiplication Table of 2
**Objective:**  
Learn basic Flask routing and how to display static content.

**Description:**  
Modify function `table` using flask route decorator such that it returns the multiplication table for the number 2 (from 2 x 1 to 2 x 10) when accessed via `http://localhost:5000/table`.

---

## Task 2: Dynamic Multiplication Tables

**Objective:**  
Understand how to pass route parameters and dynamically generate content in Flask.

**Description:**  
Modify the `table` function to generate multiplication tables dynamically based on a number passed in the URL. For example, accessing `http://localhost:5000/table/2` will display the table of 2, while `http://localhost:5000/table/9` will display the table of 9.

---


## Task 3: Correcting Template Path Error  

**Objective:**  
Learn to handle and resolve template file path issues in Flask.

**Description:**  
Run `app.py` and visit `http://localhost:5000/table/3`. You should encounter a "Template Not Found" error. Identify the missing template file and correct its path so the page renders properly.  
HINT: Search on internet and change default template folder to current folder because the required template is at current folder

After that run again and visit again you will see "UndefinedError"  
Fix this error by giving required variable to render_template 

---


## Task 4: Implement Template Inheritance

**Objective:**  
Understand and implement Flask’s template inheritance for cleaner, more maintainable templates.

**Description:**  
Refactor four HTML files in the `templates` folder by implementing **Template Inheritance**. There is a common layout file `x_layout.html` with a jinja block named `mainbody`. Use this layout in each of the two HTML files (named as `x_home.html` and `x_login.html`) by extending `x_layout.html` and placing the specific content within the `mainbody` jinja block.

---
