# Library Management System

## Features

- **Librarian Features:**
  - Add/remove a book
  - Update the quantities of books
  - Issue/deposit a book
  - Generate a penalty if the book is due for longer
- **User Features:**
  - Check and request for issue (Email should be triggered for issue request)

## Models

- **Book**
- **IssueLog**
- **IssueRequest**
- **Custom User Model** (to handle email)

## Views

### BookViewSet

- CRUD operations
- Search functionality

### IssueRequestViewSet

- CRUD operations
- Search functionality
- Custom `perform_create` method to handle issue request creation

### IssueLogViewSet

- CRUD operations
- Search functionality
- Custom `perform_create` method to handle issue log creation

### IssueLogExportView

- Get functionality to export issues/deposits for a date range

## Signals

- Post-save signal on `IssueRequest` model to trigger email for issue requests
- Post-save signal on `IssueLog` model for any additional actions or notifications

