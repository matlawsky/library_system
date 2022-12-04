# Library system

## Access
Access based on the roles which are worker and reader.
Worker is given special, privileged access by administrator.

## Features
- CRUD for books / Worker
- Registering of new user / Reader
- Book reservation/ordering / Reader
- Rating the book and commenting / Reader
- Mark the books as read / Reader
- Returning the book - scheduling the library visit / Reader
- Returning the book - registering return in the system / Worker
- Search books in catalog / Reader and Worker(additional info visible) 
- Overdue fee calculator / Reader and Worker

## Storage and data simulations
To simulate real library I use a google books API to search te books
If chosen book based on recommendations is already in the system the data is pulled from database (PostgreSQL), and if such book is not in a storge book data is requested from google books API
Then randomly assing a number from 0 to 3 which determines how many copies of the books there is
After that another random assingment takes place if the first number is between 1-3, random number between 1-3 gets picked which is a number of this book copies that are physically available at the library, 
for other books another assignment takes place that is random users gets book assigned to his/her account and date between 1 and 6 months gets also assigned and based on that fee is also assigned if there is an overdue

## Models
Reader != Worker != User but Reader and Worker are Users

Reader: 
ID - integer
Name - string
Surname - string
birth-date - date
Books in posession - List of integers

Book:
bookId - integer
title - string
author - string

CopyBook:
ID - integer
BookID - integer
availableAt - date

Comment:
ID - integer
UserID - integer
BookID - integer
content - string

Rating:
ID - integer
BookID - integer
UserID - integer
Grade - float

## Frontend
I decided I don't need to put a lot of elements, design should be simple
and not deconcentrating, Here focus should be put on utilities rather than looks
So whole frontend with small exceptions is covered by Bootstrap and the wireframe 
of the site is a derivative of Bootstrap examples
