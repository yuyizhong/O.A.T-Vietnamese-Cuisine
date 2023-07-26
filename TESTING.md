## Functional Testing

**Authentication**

*Register*

Ensure a user can sign up to the website

Steps:

1. Navigate to [O.A.T-Vietnamese-Cuisine](https://oat-vietnamese-cuisine-91aa08c21232.herokuapp.com/) and click ``Register`` at the nav bar
2. Enter Username and Password 
3. Click Sign up

Expected:

A message to confirm a successful register and user will be directed to the home page.

Actual: 

A message popped up to confirm a successful register and user is directed to the home page.

<hr>

*Login*

Ensure a user can log in once signed up

Steps:
1. Navigate to [O.A.T-Vietnamese-Cuisine](https://oat-vietnamese-cuisine-91aa08c21232.herokuapp.com/) and click ``Login`` at the nav bar
2. Enter login detailscreated in previous test case
3. Click login

Expected:

A message popping up to confirm a successful login and user is directed to the home page.

Actual:

A message popped up to confirm a successful login and user is directed to the home page.

<hr>

Description:

*Logout*

Steps:

1. Login to the website
2. Click the ``logout`` at navbar
3. Click confirm on the confirm logout page

Expected:

A message came out to confirm User is logged out. Home page is loaded.

Actual:

A message came out to confirm User is logged out. Home page is loaded.

<hr>

A message poped up to confirm a successful register and user will be directed to the home page
**Menu Page**

*Add Menu*

Ensure a new menu can be created to add to the menu list

Steps:

1. Login as a staff
2. Navigate to the Daily Menu page by clicking ``Menu`` at the nav bar
3. Click on the  <u>Add Menu</u>  at the top of the page and go the Add Menu Page
4. Fill up the Add Menu Form with the following details:
    - Name: Test Menu    
    - Description: Test Item
    - Price: 15.00
    - Image: Any
    - Status: Change from 'Draft' to 'Approved'    
    - Category: choose Main Course from drop down menu

5. Click ``Add Menu``
6. All the above fields are required before submitting the form otherwise an error message appears

Expected:

-New menu item is successfully added and a confirmation message to inform the menu is added
-It can be seen at the Daily Menu page if status is selected as Approved
-It cannot be seen at the Daily Menu page if status is Draft

Actual:

-New menu item is successfully added and a confirmation message appeared to inform the menu is added
-It can be viewed at the Daily Menu page

<hr>

*Edit Menu*

Ensure a menu can be updated when requires

Steps:

1. Navigate to the ``Daily Menu`` page from the site navbar by clicking on ``Menu``
2. Go to the particular menu which you'd like to update and Click <u>Edit</u> at the footer of that menu cart
3. Edit form is pre-filled with the current menu information and only amend the fields which requires updates
4. Update the menu contents at the Edit Form, and click ``Save``

Expected:

Menu has been updated and a flash message displayed to the user it was updated

Actual: 

Menu has been updated and a flash message displayed to the user it was updated

<hr>

*Hide/Unhide Menu*

Ensure a menu can be toggled off and add it back to the Daily Menu page

Steps:

1. Navigate to the ``Daily Menu`` page from the site navbar by clicking on ``Menu``
2. Go to the particular menu which you'd like to hide/unhide and Click <u>Hide/Unhide</u> at the footer of that menu cart

Expected:
- After clicking on <u>Hide</u>, the link text changes to <u>Unhide</u>
- Nun Staff users won’t be able to view this menu from the Daily Menu page
- After clicking on <u>Unhide</u>, the link text changes to <u>Hide</u>
- All users can view this menu from the Daily Menu page

Actual:

- After clicking on <u>Hide</u>, the link text changes to <u>Unhide</u>
- Nun Staff users won’t be able to view this menu from the Daily Menu page
- After clicking on <u>Unhide</u>, the link text changes to <u>Hide</u>
- All users can view this menu from the Daily Menu page
<hr>

*Delete Menu*

Ensure a menu can be deleted from the Daily Menu page

Steps:

1. Navigate to the ``Daily Menu`` page from the site navbar by clicking on ``Menu``
2. Go to the particular menu which you'd like to delete and Click <u>Delete</u> at the footer of that menu cart

Expected:

Menu is deleted and won’t be viewed from Daily Menu

Actual:

Menu is deleted and won’t be viewed from Daily Menu
<hr>

*View Menu Description*

Ensure a menu’s description can viewed when a user want to know more about it

Steps:

1. Navigate to the ``Daily Menu`` page from the site navbar by clicking on ``Menu``
2. Go to the particular menu which you'd like to have more information and Click ``View Details`` button underneath the Menu name and Price

Expected:

-	A modal box pops out with Menu Name and detailed information including allergies 
-	It can be closed by clicking on the ‘x’ at the modal header or ‘Close’ button at the modal footer

Actual:

-	A modal box pops out with Menu Name and detailed information including allergies 
-	It can be closed by clicking on the ‘x’ at the modal header or ‘Close’ button at the modal footer

<hr>

**Reviews Page**

*Add Review*

Ensure a review can be left to each menu by users
Steps:
1.	Navigate to the Daily Menu page by clicking ``Menu`` at the nav bar
2.	 Go to the particular menu which you'd like to leave a review and Click ``Leave Review`` button underneath the Menu name and Price
3.	If users are not logged in, they will be directed a login page 
4.	After log in, users are redirected back to the ``Leave Review`` page for the menu they chose 
5.	 Fill up the Leave a Review Form with the following details:
 	- Rating: Choose from the drop down arrow, eg: 4-Very Good  
    	- Contents: Review message
               - Image:  image related to the review (optional)
               -Visit date: dd/mm/yy
4. Click ``Submit``
5. All the above fields except image are required before submitting the form otherwise an error message appears

Expected:

-User is directed to the reviews page for that particular menu with the most recent review listed on the top under the menu name and menu image
-A confirmation message informs the user that the review was left successfully

Actual:

-User is directed to the reviews page for that particular menu with the most recent review listed on the top under the menu name and menu image
-A confirmation message informs the user that the review was left successfully
<hr>

*View Review and Rating*

Ensure a review and rating can be left to each menu by users

Steps:

1.	Navigate to ``Reviews`` page by clicking on ``Reviews`` at the nav bar
2.	 At here, all users can view the average rating and total number of reviews the menu received from users
3.	Click on the <u> number </u> of the reviews for a particular menu

Expected:

-	Users will be directed to the detailed review page for that menu 
-	Al l the ratings and reviews left by different user are listed there for viewing 

Actual:

-	Users will be directed to the detailed review page for that menu 
-	Al l the ratings and reviews left by different user are listed there for viewing 
<hr>

*Reply Page*

Ensure a staff can reply a message to the reviews left by users

Steps:

1.	Login as staff
2.	Navigate to ``Reviews`` page by clicking on ``Reviews`` at the nav bar
3.	Click on the <u> number </u> of the reviews for a particular menu which staff would like to view
4.	Navigate to the detailed review page for that menu with all the ratings and reviews left by different users
5.	Find the review to reply, just click on the ``Reply`` button under that review message

Expected:

-	Staff will remain at the detailed review page with updated reply message listed under the review they just replied
-	A confirmation message informs a reply is successful.

Actual:

-	Staff will remain at the detailed review page with updated reply message listed under the review they just replied
-	A confirmation message informs a reply is successful
<hr>

**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

  * Home -> index.html - Visible to all
  * Menus -> menu_list.html - Visible to all
  * View Details -> menu modal - Visible to all
  * Add Menu -> add_menu.html - Visible to staff
  * Edit Menu -> edit_menu.html - Visible to staff
  * Leave Review -> leave_review.html - Button Visible to all but page accessible by logged in users only; Unlogged in users will be directed to login 
  * Reviews -> reviews.html- Visible to all
  * View Details & Rating -> review_details.html - Visible to all
  * Reply -> reply.html – Visible to staff 
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users
  * Contact -> contact.html - Visible to all  
All navigation links directed to the correct pages as expected.
<hr>

## Negative Testing

 Forms cannot be submitted when required fields are empty


## Unit Testing

Unit tests were created to test menu basic functionality such as templates used and redirects. These can be found in the test_menu_views.py files in the menu app.

Results:

![unit tests](docs/testing/unit-test.jpg)

## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

I couldn't fix the empty link error identified by WAVE Accessibility. The Edit Menu Form were prefilled with the current menu information including the imgae. However the menu image is stored at cloudinary and WAVE recognises it as an empty link.

![Cloudinary-lead-error](docs/testing/bug.jpg)

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). Initially there were some errors due to missuse <a></a> within a button and didn't have an alt for the logo image. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copy and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

![HTML Validator](docs/testing/html.jpg)

All pages were run through the CI [Pep8](https://pep8ci.herokuapp.com/) validator to ensure all code was pep8 compliant. Some errors were shown due to white trailing spaces and lines too long, empty lines expected. All of these errors were resolved and code passed through validators with the exception of the settings.py file.


![PEP8](docs/testing/pep8.jpg)

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator. It mentioned one undefined variable. This function is to set the time interval for bootstrap alert messages.

![JS validator](docs/testing/js.jpg)
![JS validator](docs/testing/js1.jpg)
![JS validator](docs/testing/js2.jpg)

## Lighthouse Report

Lighthouse report showed areas for improvement on SEO and Best practices. Meta descriptions keywords and js were added to boost the SEO and accessability to 100. 

![Lighthouse Desktop](docs/testing/lighthouse-desktop.jpg)

![Lighthouse Mobile](docs/testing/light-house-mobile.jpg)

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [O.A.T-Vietnamese-Cuisine](https://oat-vietnamese-cuisine-91aa08c21232.herokuapp.com/contact/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.


## Bugs

Instead of bug, there is a feature I would like to improve if I have longer time. Current 'delete menu' function has no confirmation before deleting. I would like to build a delete view. When clicking on delete button, instead of deleting the menu immediately, it would direct the user to a delete view where confirmation is reassured. Also a protection of PermissionDenied will be added to view level to prevent unauthorised access. 