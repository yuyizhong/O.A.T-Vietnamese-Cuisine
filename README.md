# O.A.T Vietnamese Cuisine

O.A.T Vietnamese Cuisine is an imaginary vietnamese restauraunt based in central London. The ideal is to provide londerners the most authentic vietnamese food with an website for staff to manage the daily menu and reply to customer reviews. It also allows customers to simply leave reviews to each dish on the menu list and view other's reviews. The average ratings of each menu item also gives both the staff and customers an idea of the most popular choices at O.A.T.
The live link can be found here: [Live Site - O.A.T Vietnamese Cuisine ](https://oat-vietnamese-cuisine-91aa08c21232.herokuapp.com/)

![Responsive Mock-Up](docs/readme_images/responsive.jpg)

## Table of Contents
- [O.A.T Vietnamese Cuisine](#O.A.T Vietnamese Cuisine)
  - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plan](#the-strategy-plan)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plan](#the-scope-plan)
  - [The-Structure-Plan](#the-structure-plan)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plan](#the-skeleton-plan)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plan](#the-surface-plan)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [Technolgies](#technolgies)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Version Control](#version-control)
  - [Heroku Deployment](#heroku-deployment)
  - [Run Locally](#run-locally)
  - [Fork Project](#fork-project)
- [Credits](#credits)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals
The site is aimed for restaurant staff to easily manage the daily menus on the website, keep track of the costomers' feedbacks to monitor the quality of the food and reply to each review for better customer care pratice. 

The site also aims to provide customers the opportunity to leave reviews and make suggestions to the restaurant menus. They can also rate the food from 1 to 5 based on their experience and an average rating is automatically generated for indival dish. 

### Agile Planning

This project was developed through applying agile methodologies by delivering small features in incremental sprints.

All projects were assigned to epics, which were broken into small tasks and prioritized as must have, should have, could have. "Must have" stories were completed first before "should haves", and the last "could haves". To ensure all core requirements completed first gives a complete product, with the nice to have features being added if the time frame allows.

#### Epics

The project had 8 main Epics (milestones):

**EPIC 1 - Base Setup**

The base setup epic was the first epic to be delivered as all other features depend on the completion of the base setup.

**EPIC 2 - Small Pages**

Instead of creating epics for tiny features, all the small pages were included to this epic.

**EPIC 3 - Authentication Epic**

The authentication epic is for all stories related to the registration, login and authorization of views. It allows restaurant staff to CRUD menus and reply to user’s reviews securely and users to leave their messages after signed in.

**EPIC 4 - Menu**

The menu epic is for all stories that relate to the creating, editing, toggling, deleting, and viewing of menus. This allows for regular users to view menus and for staff to manage them with a simple UI interface.

**EPIC 5 – Reviews and Ratings**

The Reviews epic is for all stories related to creating, viewing the reviews and ratings to displayed menus at website. This allows the site users to easily view feedbacks of individual menu and also for signed in customers to leave reviews and ratings.

**EPIC 6 - Reply**

The Reply epic is for all stories related to creating, viewing the replies to customers’ reviews. This allows the site users to view the reply messages and also the restaurant staff to reply to user’s feedbacks.

**EPIC 7 - Deployment Epic**

This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

**EPIC 8 - Documentation**

This epic is for all documents related stories and tasks to document the lifecycle of the project development. It aims to record the detailed documentations to all stages of development and necessary information on testing, deploying and running the application.

#### User Stories

The following user stories (by epic) were completed over the 3 sprints:

**EPIC 1 - Base Setup**

As a developer, I can create the base.html including navbar and footer as the basic structure so that other template pages can be extended based on it.

As a developer, I can create static resources so that images, css and javascript can be loaded and user templates can be styled and responsive to users.

As a developer, I can set up the project so that the core features can be implemented.

**EPIC 2 - Small Pages**

As a developer, I can implement a 404 error page to inform users that the page they accessed doesn't exist.

As a developer, I can implement a 500 error page to inform users when an internal server error occurs.

As a developer, I can implement a 403 error page to redirect users from unauthorised access, so that I can secure my views.

As a restaurant owner, I can have a home page so that customers can view restaurant information and navigate to the relevant web pages.

**EPIC 3 - Authentication Epic**

As a developer, I can implement allauth so that users can sign up and have access to the websites features.

As a user, I can receive messages when I register/login/logout an account so that I can know the actions are conducted successfully.


**EPIC 4 - Menu**

As a user, I can view menus so that I can decide if I would like to dine at the restaurant.

As a staff user, I can add a new menu when we have new dishes to offer.

As a staff user, I can create draft of a potential new menu so that I can display it to users later when it is confirmed.

As a staff user, I can edit a menu when updates are required.

As a staff user, I can toggle/hide a menu when it’s temperately not available for a particular day because shortage of the ingredients. 

As a staff user, I can delete a menu when it is not ordered for a reasonable period of time.

As a staff user, I can receive messages when I manage menus so that I can know the actions are conducted successfully.


**EPIC 5 – Reviews and Ratings**

As a user, I can leave comments on dishes so that I can share my experience with others/give improvement suggestions to restaurant owner

As a user, I can give a rating to a dish so that I can express how much I like/dislike it. 

As a user, I can view other’s feedbacks and ratings to menus so that I can decide what to order and what to avoid.

As a site owner, I can view the feedbacks and ratings of my menu list so that I can know how well the menus work to customers.

As a user, I can receive messages when I submit a review so I know it was completed successfully.

**EPIC 6 – Reply**

As a staff user, I can reply to users’ reviews so that I can let customers know we care about their experience with us.

As a user, I can view the replies from the restaurant so that I can see if they are responsible owner. 

As a staff user, I can receive messages when I reply to a review so I know it was completed successfully.


**EPIC 7 - Deployment Epic**

As a developer, I can deploy the project to heroku so that it is live for customers

**EPIC 7 - Documentation**

Tasks:

* Complete readme documentation
* Complete testing documentation



