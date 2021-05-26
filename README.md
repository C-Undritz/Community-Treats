# Community Treats - Readme document

<p align="center">
  <img src="" alt="Game title screen grab from main menu">
</p>


### Website can be viewed here: 
### Project GitHub site: 

### **Disclaimer: This Website is for educational purposes only.**

---
# Table of Contents
* [OVERVIEW](#overview)
* [STRATEGY](#strategy)
* [SCOPE](#scope)
* [STRUCTURE](#structure)
* [SKELETON](#skeleton)
* [SURFACE](#surface)
* [TECHNOLOGIES USED](#technologies-used)
* [TESTING](#testing)
* [NOTED DESIGN CHANGES](#noted-design-changes)
* [FURTHER DEVELOPMENT](#further-development)
* [DEVELOPMENT AND DEPLOYMENT](#development-and-deployment)
* [MODIFYING THE GAME](#modifying-the-game)
* [CREDITS AND THANKS](#credits-and-thanks)

---
># **OVERVIEW**
Online communities are groups of people who share knowledge and ideas on a common interest. Contributing, enabling and growing online communities gets a company involved with their target audience which can increase brand awareness.  People who already have a vested interested in the topic or content you’re promoting will be exposed to your brand, website and business. As a result, your business will be etched in their mind—much more so than a competitor who doesn’t contribute to the said community.

Creating and/or hosting relevant content will drive relevant traffic to your site; and lessen click through traffic.  By attracting relevant traffic (people who are actually interested in what you have to offer or say) to your website, they’re already more likely to purchase. Why? Because people purchase when they’re genuinely interested in something. 

This project is concerned with the build of a full-stack site that showcases full CRUD functionality to allow a user to view, manage and contribute to a baking recipe dataset.  The site is called 'Community Treats' which is associated with a fictional company called 'Mix'in Bowls' who need to increase brand awareness.  The project showcases the use of current technologies to deliver backend content to the user and present in an attractive responsive and user friendly fashion.

---
># **STRATEGY**
Mix'in Bowls is a small company that has enjoyed some high street success and is now due to launch its online commercial store within the next few months.  Mix'in Bowls has had presence on the main social platforms for a number of years, however, in the run up to their commercial website launch, they now want to also create an intimate community where their brand in front and center to the users and customers of the site.  

'Community Treats' by Mix'in Bowls is the answer to this.  It is a community website extension to the retail website that allows users to upload baking recipes and view others uploaded from other community members.  The aim is to grow an online community to promote home baking, increase company and product awareness which will covert into sales of the latest Mix'in Bowls products.

Increasingly baking attracts people from a number of demographics due to the popularity of baking programmes like 'The Great British Bake-off' and also more recently due to the global pandemic.  Therefore the website is designed to be attractive to a broad spectrum of users and abilities.  The sites uses mainstream current technologies to deliver a streamlined user experience that is responsive across devices.  

# User Stories

As the site buiness owner I want to:

* *Promote the Mix'in Bowls brand prior to commercial website launch*
* *Link through to the commercial website to promote Mix'in Bowl products that could be used for the recipes*
* *Gain an understanding of the demographic of customer by gaining basic information from them*
* *Administer the site through an admin login to manage content*

As a user of this software I want to be able to:
* *Easily use the site on any device*
* *Easily navigate the site*
* *View baking recipes across a number of categories*
* *Find easily a recipe through search functionality*
* *Login and have a personalised experience*
* *Upload my recipes*
* *Update and delete my recipes*
* *Contact Mix'in Bowls to report issues and/or provide feedback*
* *link through to the main social media sites from the website*

---
># **SCOPE**
# Content
### The presentation of the site is concerned with:
1.	Being attractive and engaging from the outset to encourage the user to explore the site.
2.	Being simple in presentation and use; the focus of the site is the creating, reading (viewing), updating and deleting (CRUD) the content.   

## Functional Requirements
1.	To be viewing a recipe within a couple of clicks/taps
2.	Mobile first; the site is designed to work on mobile and tablet screens first, but responsive design ensures that it scales up and looks good on laptop and desktop screens. 
3.	Login button (with hint to register) on the landing page to encourage users to register for additional functionality.
4.	Flexible Navbar and site options to reflect a logged in user and admin user to restrict some functionality of the website.
5.	A Contact function/form that will allow the sending of feedback to an existing email using JSMail.
6.	Clear and obvious links to social media platforms.
7.	Feedback animations to provide players with clear interaction cues.

---
># **STRUCTURE**
# Database Schema
![MongoDB schema v0.1](assets/readme/community_treats_database_design_v0.1.png)


# Navigation
Navigation of the site content is facilitated by:
1. Navigation Bar fixed at the top of each page and always displayed when the user scrolls.
2. User specific navigation options displayed in the Navigation bar menu.
3. Call to action button on the landing page that will ask the user to login or direct them to register if not already a registered user.
4. A free text search field to allow first time visitors or registered users to start searching for specific keywords straight away.
5. Images related to the type of recipes that can be found on the site presented as links on the main page, so first time visitors or registered users can query recipes by type. 
6. A user 'My Page' which will feature the recipes uploaded by the user and their favourites so they can navigate to them directly
7. dynamic buttons throughout the sites that will display depending on who is logged in.  For instance a 'update' option displayed with a recipe only if the recipe author is logged in and viewing it.

This is in line with current website design and UX trends.

---
# Consistent Features between pages
Each page has a responsive fixed navigation bar with the same links that reflect whether the user is logged in and who is logged in.  The navigation links are justified to the right and a logo is justified left that links to the home page.  

Each page features the same banner image with the text 'Community Treats by Mix'in Bowls' displayed.  Content dynamically displays over this.

A footer is present on every page with social media icons linking to the Facebook, twitter and Instagram

---
># **SKELETON**
# Wireframes
* [Mobile v0.1](assets/readme/community_treats_mobile-wireframe_v0.1)
* [Desktop v0.1](assets/readme/community_treats_desktop-wireframe_v0.1)

---
># **SURFACE**
# Theme
The website look and feel is consistent throughout, the ease of which is achieved through the use of Jinja templating and the Materialize framework 

The aim for the site to be simple yet engaging from the outset to encourage the site visitor to explore further.  However the pastel colour scheme, font choice and banner should leave the user in no doubt as to the content and purpose of the site.  

# Colours
The colours selected for the game are muted pastels which reflect the natural colours found in baking and associated ingredients

![Community Treats Colour Palette](assets/readme/community_treats-colour_palette.png)


# Text
## Fonts
* [Mountains of Christmas](https://fonts.google.com/specimen/Mountains+of+Christmas?query=Christmas&preview.text=Community%20Treats&preview.text_type=custom)
* [Henny Penny](https://fonts.google.com/specimen/Henny+Penny?query=Henn&preview.text=Community%20Treats&preview.text_type=custom)
* [Mystery Quest](https://fonts.google.com/specimen/Mystery+Quest?preview.text=Community%20Treats&preview.text_type=custom#standard-styles)



---
># **TECHNOLOGIES USED**
* HTML5
* CSS3
* JavaScript 
* Python
* Flask web application framework
* Jinja template engine for Python
* Werkzeug [WSGI](https://wsgi.readthedocs.io/en/latest/) web application library
* MongoDB
* Materialize framework
* EmailJS
* Gitpod
* GitHub
* Heroku
* Google Fonts
* Font Awesome
* Balsamiq

---
># **TESTING**
>Testing completed is detailed in the [TESTING.md](TESTING.md) document

---
># **NOTED DESIGN CHANGES**


---
># **FURTHER DEVELOPMENT**


---
># **DEVELOPMENT AND DEPLOYMENT**
* A repository was setup in GitHub using the Code Institute Gitpod [full template]( https://github.com/Code-Institute-Org/gitpod-full-template).
* Development was completed using Gitpod and code was regularly pushed back to the GitHub repository.

# Website deployment
# Running the project locally

---
># **CREDITS AND THANKS**

# Code
# Images and Content
## Images
## Content
* Information for Readme Overview section was found in the following website:
	* [Sendible.com article: 5 ways to use Online Communities to Promote your Content](https://www.sendible.com/insights/online-communities-for-content-promotion)

# Acknowledgments
