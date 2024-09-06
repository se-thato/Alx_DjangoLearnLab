# API Endpoints

## Book Endpoints

### List Books
- **URL**: `/books/`
- **Method**: GET
- **Description**: Retrieve a list of all books.
- **Permissions**: Read-only for unauthenticated users.

### Create Book
- **URL**: `/books/`
- **Method**: POST
- **Description**: Create a new book.
- **Permissions**: Authenticated users only.

### Retrieve Book
- **URL**: `/books/<int:pk>/`
- **Method**: GET
- **Description**: Retrieve a specific book by ID.
- **Permissions**: Read-only for unauthenticated users.

### Update Book
- **URL**: `/books/<int:pk>/`
- **Method**: PUT/PATCH
- **Description**: Update a specific book by ID.
- **Permissions**: Authenticated users only.

### Delete Book
- **URL**: `/books/<int:pk>/`
- **Method**: DELETE
- **Description**: Delete a specific book by ID.
- **Permissions**: Authenticated users only.
