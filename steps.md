### Steps

- Start a project called `contactup`.
  `$django-admin.py startproject contactup`

- `cd contactup`
```
  ➜contactup:  ls contactup
  contactup manage.py
```

- Create a new app called contacts. `cd contactup` and `django-admin.py startapp contacts`
-
```
➜  contactup:  cd contacts
➜  contacts:  ls
    __init__.py admin.py    models.py   tests.py    views.py
```
- Create the first view `/` which will display `welcome`. Make necessary changes in `urls.py`.
- Create a model `Person` with `first_name, last_name, phone_no, address` in contacts app. db_index for first_name
- Register the app and create a new table.
- Create a new contact via shell.
- Create a new template index.html and display the newly added contacts.
- Create a new base.html with blocks.
- Create a new form which accept the details and saves to database.
- Edit the existing contact, also add the edit link in the index page.
- Delete the existing contact.
- Add new column called email.
- Add new model ExtraDetail with website, notes, relationship, birthday, person as foreign key. Syncdb.
- Add appropriate fields in the ContactForm. Save the details to two different table.
- Update the `index.html`.
- Create a url which will take a character and display all the first name starting with the character.
- Django testing.
- Django admin.
