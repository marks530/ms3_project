
## Milestone 3 Project

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1 align="center">Python and DAta Centric Developement Milestone 3 Project 
<h2 align="center">Create a Service Department Database :robot: :golf: </h2>


Here is the deployed version on the site : 
**[Service Database](https://github.com/marks530/ms3_project)**

# **Table of Contents**

- [**Project Introduction**](#project-introduction)
- [**Project Goals**](#project-goals)
- [**User Goals**](#user-goals)
- [**User Stories**](#user-stories)
- [**Site Owner Goals**](#site-owner-goals)
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



## Project Goals

The goal of the project is to provide a web based application to access a database with Create, Read, Update and Delete functionality.
I have followed Code Inititute 


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

## User Goals

The user of the site will be initially be the organizer of the event usually the captain of the golf society. The captain will set up the event and he will then instruct the competitors to log in with their names and be taken to the score entry page.
This method of collecting scores will give the organizer a immediate update on the players scores and information on who is leading the competition. The player who is entering his score will get a total of the number of strokes and a verification that his score has been entered on the system.
The player can also view the leaderboard and see how they have fared in the competition.
## User Stories

The user/player is introduced to the site by the event organizer.
When the user connects to the website he/she is presented with event information. The home page contains images of the course they are playing and details of the days timetable.

When the player has finished their round they connect to the site and click in the "Score Entry" button.
They are presented with a score card in the form of a table showing the the golf hole number, the golf hole index (which is the degree of difficulty of the each hole 1 being the most difficult) and the empty score area. The table also shows the par value for each of the golf holes which is the expected score for each hole. The par 3 holes are usually the shortest usually reachable in one shot, the 
par 4 holes are longer and reachable in 2 shots and the par 5 holes are the longest reachable in 3 shots. 
Above the score card the user will find the score entry area with a header showing a hole number, an increment and decrement buttons and the score entry box.

The score entry area is programmed the present the golf holes starting at hole 1 and ending at hole 9 (18 holes will introduced as the app evolves)and the score entry box will already contain the par value for the given hole and that will be the default score for each hole. 
This application will reduce the onerous task of collating all the scores for all the players and the organizer. At the moment the application is limited in its scope and will be developed as the Full Stack course progress.
The user enters their name and hits the "Click to enter Score button" and the name is entered above the score card. They then proceed to enter their score by using the increment/decrement buttons and clicking the submit button when the score is correct. So all the scores are entered with clicks of the mouse.

The answer box or score box automatically picks up the par value for each hole and enters it in the score box. Each time the submit button is clicked for a hole the score is added to hole row on the score card. At hole 9 the user is presented with an alert and a congratulations message, their name and their total number of strokes or score. 
The players name and score are added to the leaderboard on a separate page using the web storage feature of the browser. Each player can see their position on the leaderboard.

## Site Owner Goals

The site owner is getting a web application which has copied a typical score entry system used in golf clubs and is making it available to casual golfers and golf society members.  In the club environment this service is provided by Howdiddo.com and it works so well it is in constant use. 
Scores for each golf tournament are stored and available to the user at any time. The site owner is offering an effective professional service to the casual golfer. Golfers casual or club members are hugely interested in their statistics, the score achieved,the number of points scored each round , reducing their handicap, and so on.
All of which means that golfers players/users(the terms are all interchangeable here) are all regularly referring to the database of their statistics and thereby looking up information from the website. 
The service is intended to be free to use with sign up and log in required. 
In the professional environment the user is presented with stream of advertising for all sorts of golf products and services. This provides the site owner will regular users who can be exposed to relevant advertising.
## UX

The home page is designed to be a relatively simple page with a Navigation bar, a hero image of the golf course and banner message with information on the event. 
This is followed by a carousel allowing the site to show the user multiple images of the golf course. The footer will contain useful contact information.
This page serves as an introduction to the event as all the users will already be familiar with.
The most important element on the page is the "Score Entry" button which is a link that takes the user to the score entry page.
The layout of the page is based on the score entry system used by HowdidIdo.com used by golf clubs and the Maths game used in the Code Institute course on Javascript demonstrated by Matt Rudge.
This combination seemed to fit perfectly the requirements for the purpose.
The increment/decrement buttons around the par value and the hole count keeping track of the hole number
## Design Choice     

The site layout contains a navigation bar, a banner image, a welcome message and event details section, a carousel with multiple images of the golf course, an information section and a footer.
This is a simple layout which can be developed to suit many different courses throughout the country and indeed abroad
In the center of the page is the "Score Entry" button which is the call to action for the page. This takes the user to the score entry page 

This page contains the business area of the site. The layout directs the user to log in and enter their score via the score entry area to appear in the score card table. The structure and layout of the score entry area is based on the Maths game used in the JavaScript course. The increment and decrement were a perfect fit for the score entry structure. The JavaScript content takes some elements from the game but is largely modified. Extra functions to get the players name, fetch the par values and present them in the score entry box, log the scores in the score card, total the numbers of strokes and add the total score to the score card 
The leaderboard page contains a table with a column for the players names and a column for the total scores for each individual. The structure is based on the local storage property that allows access to a storage object saved across browser sessions. This accessed by functions created in both the JavaScript files on the site. The site is configured for a maximum of 9 players but can easily be extended

 
## Wireframes

I have in included three desktop wireframes, one for iphone and one for ipad
Desktop Wireframes:

![alt text](https://github.com/marks530/Second-Milestone-Project-MS2/blob/a16527227dd48bca4d76d307e7a5ad2675357ea6/wireframes/index_desktop_wireframe.png)

![alt text](https://github.com/marks530/Second-Milestone-Project-MS2/blob/a16527227dd48bca4d76d307e7a5ad2675357ea6/wireframes/score_entry_desktop_wireframe.png)

![alt text](https://github.com/marks530/Second-Milestone-Project-MS2/blob/a16527227dd48bca4d76d307e7a5ad2675357ea6/wireframes/leaderboard_desktop_wireframe.png)

iPad Wireframe:

![alt text](https://github.com/marks530/Second-Milestone-Project-MS2/blob/a16527227dd48bca4d76d307e7a5ad2675357ea6/wireframes/ipad_index_desktop_wireframe.png)

iPhone Wireframe:
![alt text](https://github.com/marks530/Second-Milestone-Project-MS2/blob/master/wireframes/score_entry_iphone.png "iPhone score entry wireframe")
## Features

The site is made up of three html pages supported by a css file and two javascript files. The home page has no interactive features with the exception of a link button. The score entry page gather the players name and their score and the leaderboard page stores the player name and the total score.
The main features of the site are the interactive score card and leaderboard which allow the user view playing statistics and those of fellow competitors.
A carousel on the home page can show a range of images of a given course. Many more images can easily be added.
#### Features Left to Implement 

As the project was implemented using only front-end interactive technologies there is plenty of scope for development by employing backend services. The app was setup with 9 holes and a limit of 9 players. It would be very easy to extend this. But the first task was to get the app to work and then to extend later. I will look at improving the user experience by experimenting with different layouts and use of buttons 

In order to keep the user coming back to the site records of each event and associated statistics could be made available. The user could look up every time a round of golf was played and the individual scores at the time. Using the historical data a host of other useful statistics can be calculated. The user can measure their performance over time. As with similar sites relevant advertisements can be displayed to the user and an e-commerce utility could be added to the site.Using the landing page with its carousel and banner image it is possible to show multiple images of a given course and it would be a feature that could be extended over time. Templates could be set up for any number of different courses

## Technologies Used

 -   [HTML5](https://www.w3schools.com/html/)
 -   [CSS](https://www.w3schools.com/css/default.asp)
 -   [Javascript](https://www.javascript.com/)
 


## Testing

Completed testing of all the html code at the following address [W3 Validator](https://validator.w3.org/nu/#textarea and the css.style file using the css checkbox on the same page 
On each page I evaluated the navbar, from Desktop to Mobile, watching the behaviour of the dropdown menu on each of the different screens. I also ensured the hamburger dropdown menu was working correctly and in position once it was visible on screen.
The hamburger element proved to be troublesome this time around as it did not work on all the pages only the landing page. I discover this was because I had used different versions of the Bootstrap CDN on each page
During testing I discovered that on the iPad in Chrome Dev Tools the score entry section is jumbled yet it works on an iPad Pro. I was able to correct this by modifying the css rules
Javascript code was checked on 
  -  [jshint](https://jshint.com/)
 

## Bugs

I had some issues with the bootstrap link and did not have enough time to resolve all of them
This link was causing problems in the footer section not working to display the logos for the social media links. Using a link with version 4.7.0 fixed the problems on one of the pages. I intend to investigate this issue when more time is available.
There is still a problem with the iphone screen size with the with the buttons overlapping somewhat.
Unfortunately I will not have time to resolve this issue before the deployment. 
However I do intend to get to the bottom of the matter
Another issue is the logos for the social media links are not showing on the leaderboard and the score entry page. I will also coorect this with more time

[StackOverflow](https://stackoverflow.com/questions/48919200/github-pages-only-showing-readme-file) whilst trying to deploy I could only see my ReadMe on Github Pages

## Deployment

Create Github repo 

add links here to deployed site 

  - [deployed site](https://marks530.github.io/Second-Milestone-Project-MS2/index.html)


**CLI commands** 

```
git add 
git commit -m 
git push 
git status

``` 

## Credits 

- I found [w3schools](https://www.w3schools.com//) to be extremely helpful

- [css-tricks](https://css-tricks.com//) was another site I found to be useful

- [Bootstrap 4](https://getbootstrap.com/docs/4.1/components/) documents proved to be 

- [Javascript docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)



The structure of the Maths game proved to be ideal for the score entry system I needed for the site so this area  is based on that game. So credit to Matt Rudge for that
The score card and leaderboard are based on the tables found in the Jquery section of the course 
## Content

The image used in the site are almost all my own with the exception of one image taken from 
 - [golf images](https://unsplash.com/s/photos/golf)

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
Inevitably some tying errors will occur and trying to identify them can be difficult and time comsuming. However,
using the Traceback in the Jinja Error page proved to be very useful in tracing the exact location of the
syntax error
Example:
File "/workspace/ms3_project/templates/login.html", line 40, in template
    <a href="{{ url_for('register' }}" class="light-blue darken-4 text-shadow">Register Account</a>
jinja2.exceptions.TemplateSyntaxError: unexpected '}', expected ')'

jinja2.exceptions.TemplateSyntaxError
jinja2.exceptions.TemplateSyntaxError: unexpected '}', expected ')'