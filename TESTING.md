# Community Treats - Testing document

## [Associated Readme document](README.md)

---
# Table of Contents
* [RESPONSIVE DESIGN TESTING](#responsive-design-testing)
* [FUNCTIONALITY TESTING](#functionality-testing)
* [QUALITY CHECKS](#quality-checks)
* [USER STORIES TESTING](#user-stories-testing)
* [PROBLEMS AND FIXES](#problems-and-fixes)
* [REMAINING ISSUES](#remaining-issues)

---
># **RESPONSIVE DESIGN TESTING**
Research detailed screen resolutions that are most popular today (see [here](https://kinsta.com/blog/responsive-web-design/#common-responsive-breakpoints) and [here](https://www.browserstack.com/guide/responsive-design-breakpoints)).  This information was used along with the required resolutions for [am-i-responsive](http://ami.responsivedesign.is/) to determine 17 resolutions as a guide for media breakpoints and to test for responsive design using Google Chrome DevTools. The resolutions tested were:

    * 1920 x 1080
    * 1600 x 992
    * 1536 x 864
    * 1366 x 768
    * 1280 x 802
    * 1366 x 768
    * 768 x 1024
    * 540 x 720 (Surface Duo)
    * 414 x 896
    * 411 x 731 (Pixel 2)
    * 411 x 823 (Pixel 2 XL)
    * 375 x 812 (iPhone X)
    * 375 x 667 (iPhone 6/7/8)
    * 360 x 720
    * 360 x 640
    * 320 x 568 (iPhone 5)
    * 320 x 480

![Am I Responsive image showing the landing page across four devices of different screen sizes](assets/readme/am_i_responsive_landing_page.png)
![Am I Responsive image showing the results of a recipe type search across four devices of different screen sizes](assets/readme/am_i_responsive_type_search.png)
![Am I Responsive image showing the recipe view across four devices of different screen sizes](assets/readme/am_i_responsive_recipe_view.png)

The responsive design test sheets and results can be viewed using the below link.  

*Note - The test sheet linked below is stored as a single google docs sheet which contains images that do not seem to load in the initial window.   This document is therefore best viewed in Google Sheets once open.*

* [Community Treats Responsive Design test results](https://drive.google.com/file/d/1WW3HqHdbh4FxPSX5Nz79_YN6zn9hiIgM/view?usp=sharing)

For each resolution each page was tested to ensure that all text can be viewed and that all features of the page can be seen and do not overlap.

Also successfully tested the live site on the following devices:
* Huawei P smart 2019 smart phone
* Samsung A12 smart phone 
* Laptop at 1920 x 1080 resolution
* Amazon Fire HD 8 tablet
* Apple iPad 7th Generation
* Apple iPhone 8

---
># **FUNCTIONALITY TESTING**
Functionality testing of all of the implemented CRUD functionality was completed.  This was conducted on a desktop PC using Google Chrome dev tools.

*Note - The test sheets are linked below and are stored as google docs sheet.  Most of these files have mulitple tabs for each function so please do check to see the full range of tests completed.  Some of these also have images and are therefore best viewed in Google Sheets once open.*

The functionality test sheets and results can be viewed using the below links:
* [CREATE](https://drive.google.com/file/d/1RbawwFMKYuLDV1O0xnDrTe-lKLN1lYJu/view?usp=sharing)
* [READ](https://drive.google.com/file/d/11SzVZ2177d3hsJoUb8Y4LBBZHLew9a2q/view?usp=sharing)
* [UPDATE](https://drive.google.com/file/d/15f0skkOKx_7S72A-npP7XqQpiYzEqGtD/view?usp=sharing)
* [DELETE](https://drive.google.com/file/d/1cyloMQR1OJoU0xTZgKkvgPffjscJOqdY/view?usp=sharing)

># **SECURITY TESTING**
Security testing was conducted to test that any areas of the website that require a login or admin privileges cannot be accessed by manipulation of the url. 

*Note - The test sheet linked below is stored as a single google docs sheet with two tabs and is best viewed in Google Sheets once open.*

The security test sheet and results can be viewed using the below link:
* [Security tests](https://drive.google.com/file/d/1ArQhNUNXUrGTEk0enZY-GvhWzcjV3lQo/view?usp=sharing)  

---
># **QUALITY CHECKS**
# Approach
## CSS style sheet:
The following quality checks were completed on the css style sheet (style.css):
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check of the spacing between code lines.
* Code run through [Autoprefixer](https://autoprefixer.github.io/) to ensure compatibility across browsers.
* Code checked on [W3C CSS validation](https://jigsaw.w3.org/css-validator/) using direct input.

## HTML:
The following quality checks were completed on each of the four HTML files:
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check of the spacing between code lines.
* Code checked on [W3C Markup Validation](https://validator.w3.org/) using direct input.  Due to the Jinja template code within the HTML this was done by opening each page, right clicking and selecting 'view page source', and then copying the HTML code displayed for direct input.

## JavaScript:
The following quality checks were completed on each of the three JavaScript files:
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check to ensure that all console.log entries were removed.
* Manual check of the spacing between code lines.
* Code checked on [JSHint](https://jshint.com/) using direct input.  Note that '//jshint esversion: 6' was entered at the top of the code window prior to pasting in JS code. This ensures that the feedback received from JSHint takes into account that the JS code uses ECMAScript 6 specific syntax.

## Python:
The following quality checks were completed on the app.py file:
* Manual review on comments against code to ensure relevancy.
* Manual review to ensure all quoted-out code was removed.
* Manual check to ensure that all print() entries were removed.
* Manual check of the spacing between code lines.
* Addressing all PEP8 non-compliancy flags in Gitpod.
* Code checked on [pep8online.com](http://pep8online.com/).

## Website performance:
The site performance was tested on the following browsers by using Lighthouse :
* Chrome
* Opera
* Edge
* Firefox

N.B: Internet Explorer was not tested as the site uses ES6 so it's not fully compatible with Internet Explorer builds.

---
# Results
## W3C CSS Validation:
* Errors: No errors found.
* Warnings: 74 reported and no action taken as these were all related to the vendor extensions added by running the css through Autoprefixer.  So no action was taken to remove these.
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

## W3C Markup Validation:
* 404.html - No errors or warnings to show.
* 500.html - No errors or warnings to show.
* about.html - No errors or warnings to show.
* add_category.html - No errors or warnings to show.
* add_recipe.html - No errors or warnings to show.
* add_type.html - No errors or warnings to show.
* admin_category_display.html - No errors or warnings to show.
* admin_functions.html - No errors or warnings to show.
* admin_type_display.html - No errors or warnings to show.
* base.html - N/A
* contact.html - No errors or warnings to show.
* create_admin.html - No errors or warnings to show.
* edit_category.html - No errors or warnings to show.
* edit_password.html - No errors or warnings to show.
* edit_profile.html - No errors or warnings to show.
* edit_recipe.html - No errors or warnings to show.
* edit_type.html - No errors or warnings to show.
* index.html - No errors or warnings to show.
* login.html - No errors or warnings to show.
* profile.html - No errors or warnings to show.
* recipe_display_category.html - No errors or warnings to show.
* recipe_display_favourites.html - No errors or warnings to show.
* recipe_display_search.html - No errors or warnings to show.
* recipe_display_type.html - No errors or warnings to show.
* recipe_display_user.html - No errors or warnings to show.
* register.html - No errors or warnings to show.
* under_construction.html - No errors or warnings to show.
* view_recipe.html - No errors or warnings to show.

## JSHint:
* add_recipe_script.js - no reported issues.
* all_reviews_script.js - no reported issues.
* edit_recipe_script.js - no reported issues.
* password_check_script.js - no reported issues.
* user_rating_script.js - no reported issues.
* go_back_script.js - reported goBack() as an unused variable however necessary code for the function to work. Therefore no action taken in regards to this feedback.
* script.js 
  * One undefined variable
    * 8	M
    * 12	M
    * 16	M
    * 20	M
    * 24	M
  * Five unused variables
    * 8	instances_sidenav
    * 12	instances_form
    * 17	instances_modal
    * 20	instances_tooltip
    * 24	instances_collapsible

  These are from the Materialize required Javascript for the sidenav, interactive forms, modals, tool tips and collapsible.  These are necessary for this functionality to work and have been implemented as required. Therefore no action taken in regards to this feedback.

* send_email_script.js: 
    * One unused variable - line 2: 'sendMail'.
    * One undefined variable - line 3: 'emailjs'.

    These are necessry for the EmailJS service to work and have been implemented as required.  Therefore no action taken in regards to this feedback.

## Python PEP8:
* Code passed a PEP8 compliant by pep8online.com.  However there was one red flag in Gitpod shown below.  This was because the env python file was not pushed to GitHub.  So to avoid an error once the app is deployed to Heroku, the env file will only be imported if the os is able to find an existing file path for the env file itself.

   ![PEP8 issue](assets/readme/PEP8_issue.png)

## Lighthouse results:
### Chrome:
![Chrome Lighthouse results](assets/readme/chrome_lighthouse_report.png)
### Opera:
![Opera Lighthouse results](assets/readme/opera_lighthouse_report.png)
### Microsoft Edge:
![Edge Lighthouse results](assets/readme/edge_lighthouse_report.png)
### Firefox:
![Firefox Lighthouse results](assets/readme/firefox_lighthouse_report.png)

Brief testing on Safari browser was conducted by using the website on a relatives iPad.  The website functioned as expected and no problems observed.

---
># **USER STORIES TESTING**
The below details how the website meets the requirements of each user story. 

# Business Owner
## 1. *Raise awarenes and promote the Mix'n Bowls brand prior to commercial website launch*
* An about us page is accessible from the navbar and this details a brief history of Mix'n Bowls and their next steps into online commerce.  It also has three promotional sections that details the three product ranges offered by Mix'n Bowls: Baking equipment, baking ingredients and books.

  ![About Us page](assets/readme/about_us_page.png)

## 2. *link to the commercial website to promote Mix'in Bowl products that could be used for the recipes*
* From each of the product promotional sections there is a 'See our range' button, that at the moment directs the user to a page under construction.  Eventually it will link to a page that displays a range of products that can be purchased.  

## 3. *Administer the site through an admin login to manage content*
* Admin users can be easily created and will have secure access to the Admin functions from their 'My Page'.  Admin functions allow for the management of 'types', 'categories', and also add new admin roles.

# First time user of the software:
## 1. *Easily navigate and use the site on any device*
* Responsive design is employed across all pages to deliver a satisfying UX on mobile, tablet, laptop and large desktop PC displays. See screenshots in 'Responsive Design Testing' above.  
* The Nav bar is displayed at the top of the site on any platform on each page.
* The logo (in the top left) of the nav bar is displayed on each page and links to the home page.
* Navigation buttons and guide text are displayed at the top of most pages that will allow the user to navigate back to their previous page.

  ![Navigation features on a desktop screen](assets/readme/community_treats_navigation_aids_dt.png)
  ![Navigation features on a mobile screen](assets/readme/community_treats_navigation_aids_mb.png)

## 2. *View baking recipes across a number of categories*
* Users of the site initially return a search for recipes by a Type by clicking on one of the interactive 'type' boxes on the landing screen:

  ![Community Treats landing page](assets/readme/community_treats_landing_page.png)

* User can then refine the results of the Type search by selecting a category from the drop down box:

  ![Community Treats category search box](assets/readme/community_treats_category_search.png)  

## 3. *Find easily a recipe through search functionality*
* The website offers three different ways to search the recipe documents collection: free text search, search by type and search by category.  Each of these are clear and allow the users to be viewing a recipe with a couple of click/taps, from the home page.  

## 4. *Set up an account*
* The user is encouraged to login through a call to action button that appears on the banner when a user is not logged in.  Below that is a link to register if they do not have an account.  There is also a link from the log in page to the register page and vice versa.  The register page can also be accessed from the navbar.
* The register page is also minimal asking for only a few details.  The user has to enter the password twice to ensure that they match and feedback is in place to warn when the entries match / do not match.

  ![Community Treats category search box](assets/readme/community_treats_login_btn.png)  
  ![Community Treats category search box](assets/readme/community_treats_register.png)  

## 5. *Rate and review recipes*
## 6. *See and read other users opinions and views on the recipes*
* Users can rate a recipe through an interactive star array that allows them to rate a recipe out of five.  Once a rating is added then the current rating is displayed as a star array with the amount of stars filled representing the current rating average. The number of ratings displays alongside the star array.

  ![Recipe rating interface](assets/readme/rating_star_array_selected.png)  
  
* A logged in user can also leave a review for a recipe which is then displayed at the bottom of the view recipe screen when that recipe is displayed.

  ![Community Treats review modal](assets/readme/review_modal_ipad.png)
  ![Community Treats reviews](assets/readme/reviews_view_ipad.png)  

## 7. *Contact Mix'n Bowls to report issues and/or provide feedback*
* A contact us page is accessible from the envelope icon in the footer.  The contact page has been implemented to work through EmailJS. 

  ![Contact us page](assets/readme/community_treats_contact_us.png)

## 8. *Link through to the main social media sites from the website*
* links to social media sites facebook, instagram and twitter are found in the footer which is present on every page.

# Returning user of the software:
## 1. *Login and have a personalised experience*
* All visitors to the site are invited to register and log in.  Logging in will allow users to view recipes and save recipes as favourites, which can then be accessed from their profile page called 'My Page'.  Here they can also update or delete recipes that they have uploaded, and modify their profile and login details.

  ![Community Treats My Page](assets/readme/community_treats_my_page.png)  

## 2. *Upload my recipes*
* A logged in user will be able to access the 'add recipe' functionality either through the navbar or from their 'My Page'.  The add recipe function allows user to select a type and categories for their recipe and add as many input fields required for ingredients and instructions.  Adding an image to their recipe is done through pasting a URL link to the recipe image.

  ![Community Treats add recipe](assets/readme/community_treats_add_recipe.png)  

## 3. *Update and delete my recipes*
* The option to 'view my recipes' within 'My Page' takes the user to a list of their recipes which are displayed alongside two buttons: 'Edit' and 'Delete'.  The user can click on the image of the recipe to view it, or click on the edit or delete buttons to carry out those actions.

  ![My Page view recipes](assets/readme/my_page_view_recipes.png) 

* The delete function is faciltated through modal and any reviews or favourites associated with that recipe will also be deleted.
* The edit function is facilitated by a page similar to the add recipe page, where the user can delete and update any of the saved information  

## 4. *Save recipes that I like as favourites*
* A logged in user can favourite a recipe whilst viewing a recipe by clicking on the 'favourite heart' icon.  An unfilled heart icon indicates that it is not a favourite, where as a filled icon indicates that it is a current favourite.

  ![Favourite heart icon](assets/readme/community_treats_favourite_icon.png)

* The users favourites can then be quickly viewed and accessed from the 'view favourites' button on 'My Page':

  ![My Page view favourites](assets/readme/my_page_view_favourites.png)  

## 5. *Update my profile details*
* The ability to update profile details can be found as two functions on 'My Page': View/Edit profile and Change password.

  ![My Page view/edit profile](assets/readme/my_page_update_profile.png) 
  ![My Page view/edit password](assets/readme/my_page_update_password.png)  

---
># **PROBLEMS AND FIXES**
## 1. Console errors
* Issue: On the 'add recipe' form, when the buttons to add additional ingredients and additional instructions were clicked, two entries posted in the console:

  ![invalid form control errors](assets/readme/invalid_form_control_errors.png)

* *Fix: To solve this the following had to be added to all button elements on the page and those added by the JavaSript functions: type="button".  This solution was found on [stackoverflow](https://stackoverflow.com/questions/22148080/an-invalid-form-control-with-name-is-not-focusable?page=1&tab=votes#tab-top)*

## 2. Comparing _id's with string values
* Issue: The type and category values are recorded in the recipes as the type and category documents _id's but are saved as string values.  Within the edit_recipe.html code when populating the type and category input fields for the drop down list, the recipe.type and recipe.category are compared to the type and category _id values which are not strings. 
* *Fix: To do this, the type._id and category._id had to be converted to a string using the Jinja filter string().*

## 3. Modals in a Jinja loop
* Issue: The modal that triggers when delete selected for recipes and types was needed to be in the loop but that meant the modal was always deleting the first returned record in the loop.  
* *Fix: This was fixed by adding '-{{ recipe._id }}' to the href on the modal trigger and the modal id.  Thanks to Daisy_mentor on slack for the advice on this one.*

## 4. If 'user' in session statement:
* Issue: When the recipe was viewed it was required that the rendering of the favourite icon and also the state of and response of the 'leave review' text reflected whether the current user had already added the recipe to favorites and or reviewed the recipe already.  The functionality for this was working fine when a user was logged in, however the recipe would not display when a user was not logged in.  To gain the current user details two methods were tried and both returned errors:
  
  1) Within the python: current_user = mongo.db.users.find_one({"username": session["user"]})
  2) Within the html file to select the recipe to view: <a href="{{ url_for('view_recipe', recipe_id=recipe._id, username=session['user']) }}" 

  Stating a default parameter value for 'username' when passing it from the frontend to back was tried along with an If-else statement on this value, but an error still resulted.
  
* *Fix: BenKav_lead stated that an if else statement could be used in the Python that checked whether the 'user' was in session.  This solved the issue: 

  ![if 'user' in session](assets/readme/slackreturn_benkav.png)*

## 5. Navigation 
* Issue: When adding nav buttons throughout the site for improved navigation problems were encountered as the the user could reach a recipe view by five means: free-text search, results after clicking on one of the the types, results of refining the search by category, from the 'My Page' view recipes and from the 'My Page' view favourites.  Initially, it was planned to call the Flask Python functions for the previous pages, however this was not always possible as the variables were not always able to be passed back from the recipe view.  
* *Fix: where possible, the Flask Python function was called.  Where this was not possible the 'History back() method' was used as shown at [w3cschools.com](https://www.w3schools.com/jsref/met_his_back.asp)*

## 6. Delete category values from recipes
* Issue: It was required that the removal of a category from the categories collection also removed any reference to that category from the category array on each recipe document.  A number of database calls were tried using the Mongo DB update many method using the $all array query operator and $pull array update operator, however the desired result was not returned.  This proved to be difficult and so this was posted on stackoverflow.
* *Fix: A kind gentleman advised and helped me work through the problem to gain a solution.  Please see the stackoverflow page [here](https://stackoverflow.com/questions/68237365/mongodb-deleting-an-array-value-in-multiple-documents-in-one-collection-using-p)*

## 7. Selecting drop-down values on an apple device
* Issue: When testing on apple devices it was found that a drop down value could not be selected in the usual way; by tapping on it.  This resulted in the interactive element behind the tapped value being selected.
* *Fix: This was googled and it was found that other users had found this to be an [issue with drop down menu on iOS Safari](https://discussions.apple.com/thread/8356119).  The solution found was to tap the option is the menu with two fingers instead of one.*

---
># **REMAINING ISSUES**
## 1. Pagination

Pagination was implemented using Flask Pagination as below and it worked very well.  Screen grabs of the implemented code (subsequently removed) are below:

  ![Pagination functions](assets/readme/pagination_implementation_functions.png)
  ![Pagination functions](assets/readme/pagination_implementation_function-call.png)

There are four ways to get recipe results from within the application:
1) recipes returned as a result of a free text search,
2) returned as a result of a 'type' search (cakes, cookies, bread etc),
3) returned as a result of a category search (chocolate, tangy, seasonal, etc)
4) As a result of the user searching for only their recipes in the profile page.

Each of these have their own view function and pagination was applied to all.  However testing revealed that it worked for two and not the other two.  The two that do not work properly are where the search parameter comes from an input field that is part of a form which has the POST action.  When performing a search on any of these, the first page is returned with all of the pagination info and links, but click on page 2 or any other pages and a 'TypeError' was returned stating *"The view function for 'search' did not return a valid response. The function either returned None or ended without a return statement."* A solution to this was not determined during development and so it was removed entirely from the project and moved to an feature for further development.

## 2. Use of Username and Recipe title in other collections
The author (username) of each review is displayed against each review displayed at the bottom of each recipe.  The display of the reviews is conducted by looping through the 'review' collection and then using dot notation to display information.  This is the same where the recipe title of each favourite is shown within the users favourites by looping through the favourites collection.  Username and recipe title can be changed.

During development, it was not determined how to loop through one collection and extract information from another in the front end to display the latest username and recipe title.  Therefore the username is stored within the reviews collection and the recipe title is stored within the favourites collection.  If these are changed within the users collection and the recipes collection (as functionality allows), out of date information will be shown in the reviews and favourites documents.

The good news is that the relationships between the recipes and favourites, and users and reviews collections are facilitated via the ObjectId's (like all relationships within the app).  Therefore the correct reviews will always show for a recipe (just the author name may be out of date) and the correct recipe will display from a favourite link (just the recipe title may be out of date).

Further work will be completed to enable the functionality where an up to date username and recipe title can be displayed.  This can be done two ways:
  1. Run a database query when one is updated to update the records in other collections
  2. Perform the query in real time with the database call to display this data.

## 3. Removal of id's from edit recipe HTML
When validating the edit_recipe.html, the W3C HTML Validator picked up that the page display of the ingredients and instructions generated multiple identical id's (id="ingredient" & id="instruction").  Therefore to pass validation the id's were removed and therefore the input labels needed to be removed.  It is understood that unique ID's can be generated by stating 'id="ingredient-{% loop.index %}", however there was not the time available to fully implement and test this.  

The impact is minimal, the populated list of ingredients displays under the ingredients header and the same is true for instructions, therefore the user is not left in any doubt as to what is displayed and what they can do to update or delete content.  However further work will be completed on this to try and re-implement the id's and therefore an input label. 

># **REMAINING BUGS**
## 1. Add recipe issues
### Test CRE-86 fail: HTML form pop up fail.
In this, when the upload button is clicked on the add recipe form and the recipe title is not filled in or incorrectly filled in, it is expected that the HTML form controls will focus on this input field and display a mesage detailing the error.  During testing the focus did shift to that input field preventing upload, however no message is displayed informing the user as to the issue.

It was not determined what is causing this issue during the project development time and the HTML matches other input fields.  Different values for the pattern attribute was tried, the pattern attribute was removed, yet this did not solve the issue.

### Tests CRE-87, 88, 96, 97 fail: HTML form focus and pop up fail.
This concerns the type and category drop down input fields on the add recipe form.  Item 1 in the section Problems & Fixes details console log entries that were fixed.  However later testing revealed that the submit button for the form also generated the same console log entries.  The same fix could not be applied as the upload recipe button needs to contain 'type="submit"'.

Currently if the user tries to submit the add recipe form with no selected value in these fields nothing happens that directs them to the issue.

This was researched online and and on slack and it is a common problem.  Unfortuanately research did not reveal a suitable solution to this and the implemented code seems to match the code in the CI walkthrough project.  No solution was found or implemented during the project development time. So to attempt to mitigate the issue to a degree, messages have been added above the Type select and Category select to indicate to the user that these are required inputs.

## 2.  Edit recipe issues
### Tests UPD-73, 74, 75, 76, 77 fail: HTML form pop up fail.
This concerns the following input field on the edit recipe form:
* recipe title
* recipe description
* preparation time
* cooking time
* serves

This is the same issue as described above for the first add recipe issue.  When the upload button is clicked on the form and any of these fields are not filled in or incorrectly filled in, it is expected that the HTML form controls will focus on this input field and display a mesage detailing the error.  During testing the focus did shift to the input fields preventing upload, however no message is displayed informing the user as to the issue.  

It was not determined what is causing this issue during the project development time and the HTML matches other input fields.  Different values for the pattern attribute was tried, the pattern attribute was removed, yet this did not solve the issue.
