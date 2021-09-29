
## Milestone 3 Project

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1 style="text-align:center">Python and Data Centric Developement Milestone 3 Project</h1> 
<h2 style="text-align:center">Create a Service Department Database :robot: :engineer: </h2>


Here is the deployed version on the site : 
**[Service Database](https://github.com/marks530/ms3_project)**

# **Table of Contents**

- [**Project Introduction**](#project-introduction)
- [**Project Goals**](#project-goals)
- [**User Goals**](#user-goals)
- [**User Stories**](#user-stories)
- [**Site Owner Goals**](#site-owner-goals)
- [**Database**]
- [**UX**](#ux)
- [**Design Choices**](#design-choices)
- [**Wireframes**](#wireframes)
- [**Features**](#features)
	- [Features left to implement](#features-left-to-implement)       
- [**Technologies Used**](#technologies-used)
- [**Testing**](#testing)	
- [**Bugs**](#bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
	- [Content](#content)
	- [Acknowledgements](#acknowledgements)
- [**Footnote**](#footnote)    
## Project Introduction
The web application created for the project Python and Data Centric Developement Milestone 3 is designed for engineering companies who have a sales and service team. From my previous experience working as a service engineer I realise the value of having a record of every service call and the actions taken to resolve each problem. A database that recorded the service history each piece of equipment with the customer infomation would be a huge asset to these companies



## Project Goals

The goal of the project is to provide a web based application to access a database with Create, Read, Update and Delete functionality.
I have followed Code Inititute criteria to create the application


* Data handling: Build a database in MongoDB using the Flask Python web application framework
* Database structure: Design a structure that matches requirements in this case a non-relational database
* User functionality: Create Read Update and Delete records through the web interface
* Use of technologies: Use HTML and custom CSS for the website's front-end
* Structure: Incorporate a main navigation menu and organised layout
* Documentation: Write a README.md file
* Version control: Use Git & GitHub for version control
* Attribution: Maintain clear separation between code written by you and code from external sources
* Deployment: Deploy the web application to cloud based host (Heroku)
* Make sure to not include any passwords or secret keys in the project repository

Apart from satisfing the Milestone criteria I have endevoured to create a database that could be used in a commercial environment such as 
a service department in companies that sell and service production equipment. The design and content of the database would depend on the particular requirements
of the individual companies but I believe the basic structure if the project database would be suitable for many of them.
The database created will be a historical record of all the work carried out by the service engineers and all of the repairs made by them.
As such the database will become valuable asset for the company and perhaps in time take on a value of its own


## User Goals

The users of the applicatiion would be administration staff, sales staff, service engineers and the Service Manager of the department who would be the administrator of the database.
The service engineers will be the main users of the application who want to create a report of their daily service calls with customer information and machine details.
They will be able to search the database for all the previous service calls on each piece of the equipment and perhaps find a solution to the problem
in the "action taken" section. 
The admistrative staff who may be sales support or human resources can check the work of the service engineers keep an eye on the outstanding calls using the urgent flag. Information on any parts used would also be of interest. These individuals would not be able to alter any records but would have read-only access.
The sales staff would be able to get an update on any problems a customer may having before a visit to that customer.
The Service Manager who is the Admin user and ultimately the administator of the database will be able to monitor the operation of the service department and 
view any outstanding service calls. The "parts used" section of the database is of special interest to check parts stock and which parts to order.


## User Stories

The Service Manager as administrator of the application will be responsible for introducing new users to the application and creating their user accounts and passwords. Each time a new user requires access to the web app the manager creates a new account and issue the credentials to the new user.
He is the only user with full access to the databable and have the ability to delete accounts and records.

The service engineer will be the main user of the application. He/she will be able to

* Create a service report each time an on-site service call is made 
* Add specific detail of successful repairs to help other engineers and for future reference
* Before making an on-site service call check the history of previous calls parts used and action taken
* Check the service history of similar machines by searching using "machine_type
* Check to see parts used on the machine type

The office staff and HR staff will also have limited access to the database to carry out the following tasks

* Check and keep track of service calls made by engineers
* Monitor the use of spare parts and parts stock
* Check for service calls not yet resolved

The sales staff will also have limited access to the database to check the following

* Monitor outstandiing service calls before visiting a customer
* Monitor the reliability of each machine type for future sales
* Check the operation and performance of the service department


## Site Owner Goals

The site owner will have invested in the web application to increase the productivity of the service department. They can view the statistics of 
equipment problems and make judgements on the reliability of manufacturers and equipments types. They can also get an overview of the activities of the 
service department

## Database
As mentioned in the Project Goals section, it was required to: 

>"Build a MongoDB-backed Flask project for a web application that allows Users to store and manipulate data records on a cloud-based host"  

The database can be customised for each company that uses it with controlled acces for different groups

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas) was a ideal for this purpose as it is a non-relational document-oriented database program.

This database contains two collections

* **Users**: contains the Username and a Password ([Hashed](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) 

* **serviceReports**: containing all the data with the following fields Customer Name, Engineer Name, Date, Machine Type, Fault Deacription, Action Taken
and Parts Used. The last field shows unresolved service calls and marks them urgent



## UX


The design of the web application was to create a repository of information on the operation of a service department in any company. The challenge was to generate a stucture that embraced all of the important elements that needed to be recorded and would continue to provide assistance to users into the future.
From my experience in the business I selected the following headers

* Customer Name - in the this case the end user and buyer of equipment
* Engineer Name - as the main user and gaining the greatest benefit
* Machine Type - Machine Type or equipment type, a single customer may have many differect types
* Fault Description - allows the engineer to enter details of the problem
* Action Taken - space to allow the service engineer give detailed information on actions taken to solve the problem
* Parts Used - very important for stock control and costs


The control and the functioning of the site is managed on the base.html page 

* As the main page the servicereports.html page shows all the service calls for all engineers
* The add_record.html page is where the engineers enters all the required information on the service call
* The add_user.html page where only the administator can add a new user
* The edit_record.html page - only the engineer who created the record can edit it
* The profile.html shows who is logged in at any given time
* The login.html page allows registered users to login 
* The register.html page allows only the administroator to create new users and delete old users


The goal of this milestone project was to create a web application using **Python**, the **Flask** libraries (a Python web framework) and a (NoSQL) non-relational document based Database (**Mongo DB**) to construct the functioning app, as well as incorporate the *CRUD* operations (Create, Read, Update and Delete). 

**CRUD** refers to [persistence storage](https://en.wikipedia.org/wiki/Persistence_(computer_science)) 

**(1) Create** - add new, unique data to the database.
**(2) Read** - Fetch data from the database.
**(3) Update** - change and edit pre-existing database data.
**(4) Delete** - completely remove data from database

## Design Choice     

The site layout contains a navigation bar, a banner image, a welcome message and event details section, a carousel with multiple images of the golf course, an information section and a footer.
This is a simple layout which can be developed to suit many different courses throughout the country and indeed abroad
In the center of the page is the "Score Entry" button which is the call to action for the page. This takes the user to the score entry page 

This page contains the business area of the site. The layout directs the user to log in and enter their score via the score entry area to appear in the score card table. The structure and layout of the score entry area is based on the Maths game used in the JavaScript course. The increment and decrement were a perfect fit for the score entry structure. The JavaScript content takes some elements from the game but is largely modified. Extra functions to get the players name, fetch the par values and present them in the score entry box, log the scores in the score card, total the numbers of strokes and add the total score to the score card 
The leaderboard page contains a table with a column for the players names and a column for the total scores for each individual. The structure is based on the local storage property that allows access to a storage object saved across browser sessions. This accessed by functions created in both the JavaScript files on the site. The site is configured for a maximum of 9 players but can easily be extended

 
## Wireframes

I have in included three desktop wireframes, one for iphone and one for ipad
Desktop Wireframes:

![alt text]
![alt text]

![alt text]

iPad Wireframe:

![alt text]

iPhone Wireframe:
![alt text]

## Features

**Site Structure by HTML pages**

**Base.html**:
- This page is the base/layout html page used for Jinja Templates, which is common on all of the HTML pages. Each of the following HTML's use the base.html as their 'base' and are then appropriately adapted but maintain the links e.g. to the CSS stylesheet. The Jinja templating engine is used here, for example `{% extends "base.html" %}` followed by `{% block content %}` `{% endblock %}`. It's the general page layout, yet Users don't necessarily access this page itself, rather the other pages use it as the building block. 

**Servicereports/Home page**
- As the main page the servicereports.html page shows all the service calls for all engineers in a card style layout from the Materialize components section. As a child template it inherits its structure from the base.html page.
I decided to have the page open with all the contents of the database on display. The user can choose to collapse the display if desired.
The search panel sits at the top of the page below the navbar and the user can enter the search criteria which are "Customer Name" and "Machine Type".
The resultant search will then display all the elements that match. 


**Login page** 
- As a child template the login page inherits its structure from the base.html page. The Login page is a straight forward card displaying a login in form. If a User has already registered and has their details are saved on the Mongo DB, they can then Log In with their Username and Password combination. If they are new to the site, they can avail of the links to the Register Page at the bottom of the form. Any errors will display a flashed error message (e.g. **'Incorrect Username and/or Password'**) and leave the user on the same page. The flashed message contains both the username and password as a possible error to deter individuals from 
trying to get one right first. 

**Register New User Page**
- The service manager who is the administrator of the site is the only user with access the Register New User (add_user.html) page. He will register a new user and give them their credintials which consist of a username and password and saved on the Database plus a *‘Confirm Password’* input. This must match the chosen Password or a Flashed Error Message will appear. Other errors (including a choosing a Username already in existence) will prompt further Error Messages or tell them that the fields inputs are too long or too short.

**Profile Page**

- Once the User has successfully Logged In, their chosen Username is displayed on a Jumbotron, in a *Welcome "username"* . The Navbar options have changed to give the User access to the site and its functionalities. Only users who are service engineers have the ability to modify or delete their own records. They will see edit and delete buttons in their own card records. Sales and office staff only have the option to view and search the database.

**Add Record Page**

- Primarily for use by the service engineer this is the location where they can create new records delete them and mark them as urgent or not.
The first item in the list is a dropdown selector with the engineers name listed and all of the other fields which are required fields

**Manage Users Page**

- This is the location where the administrator can edit any user either delete the user completely or change the password associated with the user.
If the administrator chooses to delete a user he/she will be prompted with a confirmation message to confirm or cancel the action.



## Technologies Used

 -   [HTML5](https://www.w3schools.com/html/)
 -   [CSS](https://www.w3schools.com/css/default.asp)
 -   [Javascript](https://www.javascript.com/)
 -   [Python]
 -   [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 -   [MongoDB](https://www.mongodb.com/)
 -   [Heroku](Heroku: Cloud Application Platform https://www.heroku.com)



## Testing

Completed testing of all the html code at the following address 
 -   [W3 Validator](https://validator.w3.org/nu/#textarea) 
and the css.style file using the css checkbox on the same page 
On each page I evaluated the navbar, from Desktop to Mobile, watching the behaviour of the dropdown menu on each of the different screens. I also ensured the hamburger dropdown menu was working correctly and in position once it was visible on screen.


Javascript code was checked on 
  -  [jshint](https://jshint.com/)
 

## Bugs

While not exactly a bug I had considered adding an extra page to look up the passwords in case somebody had forgotten theirs, but was unable to find a way to do that and after some searching I found this article and it provided a solution. The Manage Passwords page which I had created was based on the Manage Users page showing the username and their password which I had retrieved from the database. The problem was that the hashed password was retrieved from the database. The key point being that a hashed function is a one way function that cannot work in reverse. It explains why when you forget your password for a particular site they always get you to create a new one.

-  [Stackoverflow](https://stackoverflow.com/questions/40902230/how-to-unhash-the-password-which-is-hashed-by-generate-password-hash/40902311#40902311?newreg=ec5b09c9145b402795b3d553bd44b52e)
From Wikipedia:
[MD5] is a mathematical algorithm that maps data of arbitrary size to a bit string of a fixed size (a hash function) which is designed to also be a one-way function, that is, a function which is infeasible to invert.

Leaving aside potential vulnerabilities, there's no way to get the original data that produced the hash. And that's the idea. If some bad guy get access to your database, he won't be able to know your users' passwords.



[StackOverflow](https://stackoverflow.com/questions/48919200/github-pages-only-showing-readme-file) whilst trying to deploy I could only see my ReadMe on Github Pages

## Deployment

Create Github repo 

add links here to deployed site 

  - [deployed site](https://marks530.github.io/Second-Milestone-Project-MS2/index.html)


**CLI commands** 

```
git add -A
git commit -m 
git push 
git status

``` 

## Credits 

- I found [w3schools](https://www.w3schools.com//) to be extremely helpful

- [css-tricks](https://css-tricks.com//) was another site I found to be useful

- [Bootstrap 4](https://getbootstrap.com/docs/4.1/components/) documents proved to be 

- [Javascript docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)



The Data Centric Design Mini-Project forms the basis for the project so the site and application are based largely on it. So credit to Tim Nelson for that

## Content



**Code Snippet Example - continue**

```javascript

function saveScores() {
    let scores = localStorage.getItem(LOCAL_STORAGE_GAME_SCORES);
    if (!scores)
        scores = JSON.stringify({}); //JSON.stringify convert Javascript objet to a JSON object
    let scoresObject = JSON.parse(scores); //JSON.parse convert JSON objet to a Javascript object
    let name = document.getElementById('name').value;
    scoresObject[name] = getArrayTotal();
    localStorage.setItem(LOCAL_STORAGE_GAME_SCORES, JSON.stringify(scoresObject))
}

```


## Footnote

I found this project challenging and very time consuming. I spent the vast bulk of the time writing and testing my JavaScript code and that was at the expense of the look and feel of the site. I intend to work on the project in the coming weeks while it is still fresh in my mind.
Nevertheless I found the whole project both fascinating and in the end had a real sense of achievement 
















###Errors

Inevitably some typing errors will occur and trying to identify them can be difficult and time comsuming. However,
using the Traceback in the Jinja Error page proved to be very useful in tracing the exact location of the
syntax error
Example:
File "/workspace/ms3_project/templates/login.html", line 40, in template
    <a href="{{ url_for('register' }}" class="light-blue darken-4 text-shadow">Register Account</a>
jinja2.exceptions.TemplateSyntaxError: unexpected '}', expected ')'

jinja2.exceptions.TemplateSyntaxError
jinja2.exceptions.TemplateSyntaxError: unexpected '}', expected ')'