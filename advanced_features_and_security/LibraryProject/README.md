# Permissions and Groups Setup

## Custom Permissions

- **can_view**: Allows viewing book.
- **can_create**: Allows creating book.
- **can_edit**: Allows editing book.
- **can_delete**: Allows deleting a book.

## User Groups and Permissions

- **Editors**: Can create and edit a book.
- **Viewers**: Can only view a book.
- **Admins**: Can view, create, edit, and delete book.

## How to Create and Assign Groups and Permissions

Run the `create_groups.py` script in the Django shell to set up groups and assign permissions. Ensure the script is executed as part of your deployment or setup process.
