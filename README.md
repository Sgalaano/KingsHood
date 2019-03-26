# DaHood

###  Author
nignanthomas

### Description
DaHood is a web application that allows you to be in the loop about everything happening in your neighborhood.

### User Stories
1. Sign in with the application to start using.
1. Set up a profile about me and a general location and my neighborhood name.
1. Find a list of different businesses in my neighborhood.
1. Find Contact Information for the health department and Police authorities near my neighborhood.
1. Create Posts that will be visible to everyone in my neighborhood.
1. Change My neighborhood when I decide to move out.
1. Only view details of a single neighborhood.

### How to use
To use DaHood, you must login/register. Once logged in, you will be able to see posts and businesses only for your hood.
You can add your posts and businesses in your hood.
As a user you can search for a specific business from the search bar in the navbar.
You also have the possibility to edit your profile and view the posts that you've submitted.


### Tech used
1. HTML and CSS
2. Python
3. Django
1. Postgres
1. Heroku for deployment

## Set up and Installation
### Prerequisites
You will need to install git, django, postgres and python3.6+ installed in your machine.
To install these packages, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

### Installation
1. To access this application on your command line, you need to clone it
`git clone https://github.com/nignanthomas/welcometomyhood.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations neighbor`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test neighbor`



### Known Bugs
No known bugs.

### Live link
https://dahood-nthomas.herokuapp.com/

### Licence
This project is under the [MIT](https://github.com) licence

Copyright (c) 2019 [nignanthomas](https://github.com/nignanthomas/)
