# SICIP-Blog-Demonstration
# FA-2 — Django Blog Management System

### Task

Develop a complete **Django Blog Management System** by following the requirements below.

### 1. Project Setup

Create a project folder on the Desktop named `yourname_fa_2`. Inside it, create a Django project named **`blog_project`** and a Django app named **`blogs`**.

### 2. User Authentication

Implement the following authentication features:

* **Registration:** Username, Full Name, Email, Password
* **Login:** Username, Password
* **Logout**
* Display appropriate success/error messages for registration and login.

### 3. Blog Model

Create a model named **`BlogModel`** with the following fields:

* `title`
* `author_name`
* `content`
* `category`
* `blog_image`
* `publish_date` — automatically created

The `category` field must have these choices:

* Educational
* Technologies
* Sports

### 4. Blog CRUD

Implement complete CRUD functionality:

* **Create:** Add a new blog post
* **Read:** Blog List and Blog Details
* **Update:** Update an existing blog
* **Delete:** Delete an existing blog

### 5. Template & Navigation

Use **Template Mastering** with a common base template.

**Before Login:**

```text
Register | Login
```

**After Login:**

```text
Home | Blog List | Logout
```

### 6. Home Page

After successful login, redirect the user to the **Home Page** and display a welcome message containing the logged-in username.

Example:

```text
Welcome, Habibur!
```

### 7. Blog List

Display all blog posts in a table containing exactly these columns:

| Blog Image | Title | Author | Publish Date |
| ---------- | ----- | ------ | ------------ |

### 8. Submission Requirements

Submit the complete Django project including:

* Django project and app
* Models, Views and URLs
* Templates
* Authentication system
* CRUD functionality
* Image upload functionality
* Migrations
* `requirements.txt`
* `.gitignore`
* `README.md`

### Objective

This assessment is designed to evaluate your practical knowledge of **Django Authentication, Models, CRUD Operations, Template Inheritance, Messages, File Upload, URL Routing, and Git/GitHub project management**.
