
## Milestone 3 Project

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1 style="text-align:center">Python and Data Centric Developement Milestone 3 Project</h1> 
<h2 style="text-align:center">Create a Service Department Database :robot:</h2>


Here is the deployed version on the site:
**[Service Database](http://ms3-project-heroku.herokuapp.com)**

Administrator Credentials:
- Username: **admin**   
- Password: **IPS123** 

For the purposes of testing I have given all the users the same password **IPS123**

# **Table of Contents**

- [**Project Introduction**](#project-introduction)
- [**Project Goals**](#project-goals)
- [**User Goals**](#user-goals)
- [**User Stories**](#user-stories)
- [**Site Owner Goals**](#site-owner-goals)
- [**Database**](#database)
- [**UX**](#ux)
- [**Design Choices**](#design-choices)
- [**Wireframes**](#wireframes)
- [**Features**](#features)     
- [**Technologies Used**](#technologies-used)
- [**Testing**](#testing)	
- [**Errors**](#errors)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
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
He is the only user with full access manage users of the databable and have the ability to delete accounts.
The service engineer is the only user with ability to edit and/or delete their own records.
Any user can create a record but any record created can only be allocated to a service engineer.

The service engineer will be the main user of the application. He/she will be able to

* Create a service report each time an on-site service call is made 
* Add specific detail of successful repairs to help other engineers and for future reference
* Before making an on-site service call check the history of previous calls parts used and action taken
* Check the service history of similar machines by searching using "machine_type
* Check to see parts used on the machine type
* Only the service engineer can edit or remove his/her own report.
* The administrator can also do this but only by logging in as an engineer.

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

* **Users**: contains the Username and a Password ([Hashed](https://werkzeug.palletsprojects.com/en/1.0.x/utils/))

* **serviceReports**: containing all the data with the following fields Customer Name, Engineer Name, Date, Machine Type, Fault Deacription, Action Taken
and Parts Used. The last field shows unresolved service calls and marks them urgent



## UX


The design of the web application was to create a repository of information on the operation of a service department in any company. As the application was created and developed to be used by a company and its employees and not open to the general public it is not envisaged that there will be huge numbers of users. That said the fact that the application is for a commercial enterprise it would certainly be in use every day and that while the number of users would be relatively low, the  number of entries will grow steadly. Off-site access is also required. The MongoDB database seemed like a good solution with its features like End-to-End Encryption, Sync Data Seamlessly, Global Data Distribution, Real-Time Alerts.
For the database itself, the challenge was to generate a stucture that embraced all of the important elements that needed to be recorded in the business and would continue to provide assistance to users into the future.
From my experience in this type of business I selected the following headers

* Customer Name - in the this case the end user and buyer of equipment
* Engineer Name - as the main user and gaining the greatest benefit
* Machine Type - Machine Type or equipment type, a single customer may have many differect types
* Fault Description - allows the engineer to enter details of the problem
* Action Taken - space to allow the service engineer give detailed information on actions taken to solve the problem
* Parts Used - very important for stock control and costs
* Urgent or not

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

## Design Choices     

The design and layout of the site is a plain and simple approach. The information is presented in a card format taken from the Materialize website and the Mini Project on the CI course.
The records are displayed in large style card that is easy to read and the user can scroll to browse all the entries. This area is also collaspable.
The manage users page with its list of users and their employee type is also presented in a card format.

On the manage users page and the register new user page there is duplication of the task to create a new user. On the manage users page where only the administrator has access the add user function displays an immediate response and the administrator can see immediately the list of users. On the register new user page similarly a new user is created by the administrator but is taken to the login page.
I have decided to leave the page on the site in case in the future the administrator may decide to allow new users to create their own registration details.

I spent a lot of time trying to list only the engineers names in the select list on the add report page and eventually solved the problem
The difference was changing the code in the the app.py file from 
```
usernames = (mongo.db.users.find().sort("username", 1))
``` 
to
```
usernames = list(mongo.db.users.find().sort("username", 1)))
```
This small change, adding "list" to the statement allowed me access all fields in the users collection of the database and finally this loop produced the correct result

``` {%for username in usernames %}
      {% if username.employee_type == "engineer" %}
          <option value="{{ username.username }}">{{ username.username }}</option> 
      {% endif %}
    {% endfor %}) 
```



I have removed the link from the bottom of the login page to the register page to restrict access to the that page to the administrator or service manager
 
## Wireframes

I have in included three desktop wireframes, one for iphone and one for ipad
Desktop Wireframes:

### Desktop Wireframe Add Report

![Desktop Wireframe](static/images/Add_report.png)

### Desktop Wireframe Service Reports

![Desktop Wireframe](static/images/Service_Reports_page.png)

### iPad Wireframe  Manage Users

![Ipad wireframe](static/images/Manage_Users_Ipad.png)






## Features

**Site Structure by HTML pages**

**Base.html**:
- This page is the base/layout html page used for Jinja Templates, which is common on all of the HTML pages. Each of the following HTML's use the base.html as their 'base' and are then appropriately adapted but maintain the links e.g. to the CSS stylesheet. The Jinja templating engine is used here, for example `{% extends "base.html" %}` followed by `{% block content %}` `{% endblock %}`. It's the general page layout, yet Users don't necessarily access this page itself, rather the other pages use it as the building block. 

**Servicereports/Home page**
- As the main page the servicereports.html page shows all the service calls for all engineers in a card style layout from the Materialize components section. As a child template it inherits its structure from the base.html page.
The page opens with all the contents of the database collasped. The user can choose to open the display if desired by clicking in the panel.
The search panel sits at the top of the page below the navbar and the user can enter the search criteria which are "Customer Name" and "Machine Type".
The resultant search will then display all the elements that match. 


**Login page** 
- As a child template the login page inherits its structure from the base.html page. The Login page is a straight forward card displaying a login in form. If a User has already registered and has their details are saved on the Mongo DB, they can then Log In with their Username and Password combination. If they are new to the site, they can avail of the links to the Register Page at the bottom of the form. Any errors will display a flashed error message (e.g. **'Incorrect Username and/or Password'**) and leave the user on the same page. The flashed message contains both the username and password as a possible error to deter individuals from 
trying to get one right first. 

**Register New User Page**
- The service manager who is the administrator of the site is the only user with access the Register New User (add_user.html) page. He will register a new user and give them their credintials which consist of a username and password and saved on the Database plus a *???Confirm Password???* input. This must match the chosen Password or a Flashed Error Message will appear. Other errors (including a choosing a Username already in existence) will prompt further Error Messages or tell them that the fields inputs are too long or too short.

**Profile Page**

- Once the User has successfully Logged In, their chosen Username is displayed on a Jumbotron, in a *Welcome "username"* . The Navbar options have changed to give the User access to the site and its functionalities. Only users who are service engineers have the ability to modify or delete their own records. They will see edit and delete buttons in their own card records. Sales and office staff only have the option to view and search the database.

**Add Record Page**

- Primarily for use by the service engineer this is the location where they can create new records delete them and mark them as urgent or not.
The first item in the list is a dropdown selector with the engineers names listed and all of the other fields which are required fields

**Manage Users Page**

- This is the location where the administrator can edit any user either delete the user completely or change the password associated with the user. He/she can also see at a glance the employee type
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

 I have divided the testing of the application in to three sections
 The first consists of checking the operation of all of the options available to the user and verifying that they are behaving as intended and the second section is checking the code for errors and good coding practices and of course validation. The third section is testing the application in different browsers and different screen sizes and finally on Windows machines and Macs.
 For the purposes of testing the application I have given all the users the same password "IPS123"

 ### Testing of the User Options


The following checks were carried out:

* Test the CRUD operations: create users and reports, view(read) users and reports, update users and reports and delete users and reports.
* Register a new user with username password and employee type and verify the exact same values were prenent in the database
* After registration verify the user is taken back to the login page
* Login as the administrator and check on the profile page to see who is logged in
* Login as the administrator and check the navbar for links to all the html pages on the site
* Login as the a standard user and check the navbar for links to the html pages on the site
* Login as existing user and check for correct flashed message
* Login as an engineer and check the navbar for correct links to the html pages on the site
* Test the login page for existing user and check that correct flash messages are received
* Test the login page for unknown user and check that correct flash messages are received
* Check the login page for min and max lengths and patterns on all fields
* Check that Engineers Name in New Report limited to engineers only
* Create a new report and check for validation of min and max length on all fields
* Verify in the add report page that empty fields are not permitted
* Verify that new report is reflected in the correct collection in the database
* Check the profile page responds with the correct logged in user and flashed message
* Login as the administrator and check the navbar for links to all the html pages on the site
* Verify that the manage users page shows lists all the users and their role correctly
* Check the operation of the base.html and that it is showing the correct links for each user
* Test link at bottom of register new user page to return user to login page
* Test link at bottom of login page to return user to register page



### Testing after deployment to Heroku


* After deployment on Heroku I tried logging in as different users on different computers 

As Flask is a framework, there is a requirement to validate the HTML code using the URL to avoid false error flags due to jinja2 so  when passing the code through the W3C validator, instead of using "Validate by Direct Input", it is necessary to 
"Validate by URI" which means copying the address bar from the Heroku host. As I found out that means a lot more git pushes because in order to test the URL the changes they have to be pushed to git to be reflected on the Heroku host. Even if you are not sure if you have solved the problem it cannot be validated unless the changes have been pushed to git.



Completed testing of all the html code at the following address 
 -   [W3 Validator](https://validator.w3.org/nu/#textarea) 
and the css.style file using the css checkbox on the same page
The validation process was carried out on the URL or the "Validate by URI" tab on the W3C Validation Service 

The results of HTML validation process are as follows

#### Service Reports Page Validation

After restoring some missing div elements the validation process returned the following message

 ![Section Error Message](static/images/All_Reports_Validation.jpeg)

This message (a warning message) is returned for all pages and I realised the warning must be on the base.html page, the section for displaying the flash messages

```
<section>
      <!-- flash messages -->
      {% with messages = get_flashed_messages() %}
          {% if messages %}
              {% for message in messages %}
                  <div class="row flashes">
                      <h4 class="red accent-1 center-align">{{ message }}</h4>
                  </div>
              {% endfor %}
          {% endif %}
      {% endwith %}
</section>

```

To solve the problem I would have to add a heading to the section but as there is no requirement for this in application I chose to ignore the warning.

#### Manage Users Page Validation

![Manage Users Page Validation report](static/images/Manage_Users_Validation.jpeg)

This validation report revealed a class attribute error which was fixed by removing the large attribute. It could have also been solved by adding a hyphen between btn and large.

#### Register/Add User Validation

![Register Page Page Validation report](static/images/Register_Page_Validation.jpeg)

This validation report found an error in the textarea element which was fixed by removing the type attribute. I had been getting an unwanted box in the confirm password window
but now that I try to recreate the error message I cannot do so. I will leave the message in place as a remainder. I have changed the code back to using the correct element "input"
```
<!-- confirm password --> 
    <div class="row">
        <div class="input-field col s12">
			<i class="material-icons prefix">password</i>
            <textarea id="confirm_password" name="confirm_password" minlength="5" 
             maxlength="15" class="validate" required></textarea>
            <label for="confirm_password">Password</label>
        </div>
    </div>
```

![Register Page Second Validation report](static/images/Second_Validation_Register_Page.jpeg)

The second error on the register user page shows the error "Element "option" without attribute label must not be empty. After a running several adjustments without success I discovered 
a solution on [Stackoverflow](https://stackoverflow.com/questions/22237658/html5-validation-error-with-select-required-attribute/31800584)
Change from this option setting from the Materialize website for the Select option

```
<option value="" disabled selected>Choose your option</option>
```
to this option I found on the link named above

```
<option value="">Select</option>
```

#### Profile, New Report and Login pages

Apart from the same errors for the same pieces of code these pages did not generate any new errors.


On each page I evaluated the navbar, from Desktop to Mobile, watching the behaviour of the dropdown menu on each of the different screens. I also ensured the hamburger dropdown menu was working correctly and in position once it was visible on screen.

Jquery code was checked on 
  -  [jshint](https://jshint.com/)

I tested the Jquery code on JSHint and got the following report with two warnings and an unused variable

> ES6 refers to version 6 of the ECMA Script programming language. ... It is a major enhancement to the JavaScript language, and adds many more features intended to make large-scale software development easier. ECMAScript, or ES6, was published in June 2015. It was subsequently renamed to ECMAScript 2015

>Two warnings
18	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
19	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

This message remainded me that I had added this code at some stage in the development but had not used it. I have removed this code block.

>One unused variable
45	toggleModal


### Python Checking PEP8

For this purpose i used the Python code checker at [Python Code Check](http://pep8online.com/)

The result containing a sample of the error is below

![Python Code Check Result](static/images/PEP8_online_code_check.jpeg)

The errors consisted of the following
* trailing whitespace errors at the end of line
* unexpected spaces around keywords
* lines to long
* too many blanks lines
* continuation line with the same indent as the next logical line

The last error type proved quite difficult to deal with as I started getting some errors in the application when I made some changes.
As a consequence I have left some of the lines too long (> than 79 characters) to avoid any errors in the code.
I will rectify this when I have more time.



Found that this piece of css code keeps the footer at the base of each page

'''main {
    flex: 1 0 auto;
}'''

I have tested the application on my Mac with Chrome Safari and Firefox and everything worked as it should on the different screens sizes. I also used the application with an iPad and it 
functioned correctly in landscape an portrait mode. I also tested the application on a Windows laptop using Chrome and Edge browsers and everything looked fine. On all the browsers at the different screen sizes the app was responsive.

## Errors

There may be some confusion around the use of function names and page headers in the application. The words **records** and **reports** are effectively interchangeable. 
I will have to correct this at a later stage.

Despite all the browsers showing the correct layout the iphone size there is a problem on the actual iphone 6. The navbar header "Database" falls out of the navbar and into the space below.
I will have to correct this at a later stage.

I had some diffuculty with the Urgent setting. When the setting is set to off the value stored in the database is set to none. I will have to fix this at a later stage.

While not exactly a bug I had considered adding an extra page to look up the passwords in case somebody had forgotten theirs, but was unable to find a way to do that and after some searching I found this article and it provided a solution. The Manage Passwords page which I had created was based on the Manage Users page showing the username and their password which I had retrieved from the database. The problem was that the hashed password was retrieved from the database. The key point being that a hashed function is a one way function that cannot work in reverse. It explains why when you forget your password for a particular site they always get you to create a new one.

-  [Stackoverflow](https://stackoverflow.com/questions/40902230/how-to-unhash-the-password-which-is-hashed-by-generate-password-hash/40902311#40902311?newreg=ec5b09c9145b402795b3d553bd44b52e)
From Wikipedia:
[MD5] is a mathematical algorithm that maps data of arbitrary size to a bit string of a fixed size (a hash function) which is designed to also be a one-way function, that is, a function which is infeasible to invert.

Leaving aside potential vulnerabilities, there's no way to get the original data that produced the hash. And that's the idea. If some bad guy get access to your database, he won't be able to know your users' passwords.



![StackOverflow](https://stackoverflow.com/questions/48919200/github-pages-only-showing-readme-file) whilst trying to deploy I could only see my ReadMe on Github Pages

## Deployment to Github

Create Github repo 

add links here to deployed site 

  - [deployed site](https://github.com/marks530/ms3_project)


**CLI commands** 

```
git add -A
git commit -m 
git push 
git status

``` 
## Deployment to Heroku
The project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud [Heroku](https://dashboard.heroku.com/apps) in a range of programming languages. Python was the language used for this project.

The following process was undertaken to successfully deploy the project on the Heroku:
[**The Deployed Heroku site can be found here**](http://ms3-project-heroku.herokuapp.com/)

- Heroku requires the following two files
    - A **requirements.txt** file is needed to run the installed dependencies, so to create and commit this file, the following command was used: 
    `$  pip3 freeze --local > requirements.txt`.
    - A **Procfile** is needed to direct the Heroku app to the file that it needs to run. Use the echo command the output the string
    `$  echo web: python app.py > Procfile`
    Remove the blank line to avoid problems running on Heroku.

The application was created and name simply "ms3-project-heroku" on my Heroku profile. 
Set up automatic deployment to GitHub using the "Connect to GitHub" method as the Deployment method.
But before setting *Enable Automatic Deployment* click on the Settings tab and  select *Reveal Config Vars* to securely tell Heroku which variables are required
I then had to configure some of the settings, I set the `IP: 0.0.0.0` and `PORT: 5000`. This is mirrored on my app.py.
After creating my env.py file which was added to .gitignore file, I added the `MONGO URI`, `MONGO_DBNAME` and `SECRET KEY` in to the *reveal config vars* area.

- Finally, select *Enable Automatic Deployment*  to deploy my code from GitHub to the Heroku app.

After any big changes, advancements on my code, I would push my code to the Heroku app to check if it was functioning. 

With application running on Heroku the admin log in details are as follows

- Username: **admin**   
- Password: **IPS123** 

## Credits 

- I found [w3schools](https://www.w3schools.com//) to be very helpful

- [css-tricks](https://css-tricks.com//) was another site I found to be useful

- [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) as always very informative


The Data Centric Design Mini-Project forms the basis for the project so the site and application are based largely on it. So huge credit to Tim Nelson for that


## Footnote

I found this project challenging and very time consuming. I spent the vast bulk of the time writing and testing the application code and that was at the expense of the look and feel of the site. I intend to work on the project in the coming weeks while it is still fresh in my mind.
Again I found the whole project very interesting and am so impressed with the creative possibilites that can be achieved.
















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