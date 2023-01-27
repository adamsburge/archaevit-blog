# Welcome to Archaevit

![Am I Responsive Screenshot](static/images/am_i_responsive.png)

The deployed webapp can be accessed [here](https://archaevit.herokuapp.com/).

Archaevit is designed to be a social media web application for historians, archaeologists and anyone who has an interest in history. Users are able to read articles about archaeological sites, mark the sites as interesting, important, and/or underrated. Additonally, they are able to comment and discuss their opinions about each archaeological site. Admin users are able to add, update and delete posts about archaeological sites.


# Project Planning 

## Wireframes
I used [balsamiq wireframes](https://balsamiq.com/) to design the UX and UI of the site. 

### Home Page

![Home Page Wireframe](static/images/Home%20Page.png)

### Archaeological Site Page

![Post Page Wireframe](static/images/Archaeological%20Site%20Page.png)

### About Page

![About Page Wireframe](static/images/About.png)

**Note**: This page is not yet completed and could be a future development of the site.

### Register

![Register Page Wireframe](static/images/Register.png)

### Sign in

![Log in Page Wireframe](static/images/Log%20in.png)

### User Stories
To access and read the user stories for this project, see my Github project [Archaevit User Stories](https://github.com/users/adamsburge/projects/3). Many of these user stories were taken from the Code Institute 'I think therefore I blog' walkthrough project. Two of the user stories are incomplete and are areas where future work could be done on the project.

![User Stories](static/images/user_stories.png)


### Databse Structures
The database models used for this project were based on the models used in Code Institute's 'I think therefore I blog' walkthrough project. However, these have been adjusted and added to for the purpose of the current project. Notably, this project extends Django's default user model and adds extra fields to this model where the Code Institute models kept the default model.

Note: Included here is the database model for the 'updates' comment thread which, as mentioned in the user stories above, outlines areas where this project could develop with future work.

![Database Models](static/images/Database%20Models.png)

# Features

## General Features

### Sign up, Sign in, Sign Out
Any site visitor can register for an account. Once they have done so, they can sign in and out.

![Signup](static/images/signup.png)

![Mobile Sign up](static/images/mobile_sign_up.png)

![Signin](static/images/sign_in.png)

![Mobile Signin](static/images/mobile_sign_in.png)

![Sign out](static/images/sign_out.png)

![Mobile signout](static/images/sign_out_mobile.png)

## Features for Site Visitors, Users with Profiles and Admin Users

### View Home Page
All site visitors can access the home page, which contains the main post feed.

![Normal Home Page](static/images/non-admin_user_home.png)


### Filter Posts by Trending Criteria
All site visitors can also select any of the three trending criteria ('interesting', 'important' and 'underrated') to view archaeological sites that other users have collectively indicated rank the highest in those categories.

![Normal Home Page](static/images/non-admin_user_home.png)

### View Posts and Comments
All site visitors can view the archaeological site pages and the comments other users have left.

![Blog Post](static/images/post_head.png)

![Comments](static/images/comment_logged_out.png)

![Mobile likes](static/images/mobile_post.png)

## Features Users with Profiles and Admin Users


### Comment on Posts
Users who have signed up for an account have access to comments.
![Comments](static/images/comments.png)


### Mark a Post as Interesting, Important and/or Underrated
Users who have an account are able to access the 'like' buttons and indicate a post as being interesting, important and/or underrated.

![Likes](static/images/likes.png)

![Mobile likes](static/images/mobile_post_contents.png)

## Features for Admin Only

### Add, Update and Delete Posts
The home page for site admins allows them to add, update and delete posts.
![Admin Dashboard](static/images/admin_dashboard.png)

![Add post](static/images/add-post.png)

![Update post](static/images/update_post.png)

# Technologies

### Languages
- HTML
- CSS
- Python
- Javascript
- Postgresql

### Libraries, Frameworks, Programmes & Tools
- Github - Version control and storing code 
- Gitpod - Coding platform
- Django - Primary coding framework
- Psycopg2 - Databse adapter between Postgreql and Python
- Cloudinary - Media storage
- Herokuapp - Web app deployment
- Allauth - Building user registration 
- Gunicorn - Python Web Server Gateway Interface HTTP server
- Django-Summernote - Allow forms to have customisable input
- Django-Crispy-Forms - Build comment forms
- Bootstrap - General Styling
- FontAwesome - Icons for webapp
- Google Fonts - Fonts


# Testing
To read about the manual testing employed in this project, read the [TESTING.md file](TESTING.md).

# Deployment
This project is deployed using Heroku.

Steps for Deployment:
1. Fork or Clone this Depository
2. Create new Heroku app
3. Install django, cloudinary, gunicorn, psycopg2, django-summernote, django-crispy-forms and django-allauth
4. Create a Cloudinary account, get your secret url and put it into the env.py file
5. Create a free account with Elephantsql, obtain a database url and put it into the env.py file
6. Create a unique secret key and put that into the env.py file 
7. Make migrations
8. Link the Heroku app to the repository
9. Click Deploy


# Credits
- Deployment aesthetic:
    - The color theme came from Adobe Color.
    - The layout of the Post-Detail view was inspired by Wikipedia's recent interface update.
- Concept:
    - The concept of this app is my own.
- Content:
    - The content (both text and images) of the current blog posts on the site are taken, usually word for word, from the Wikipedia pages associated with the archaeological sites.
- Code: 
    - Much of the code for this project was based on the Code Institue walkthrough project 'I think therefore I blog'. Much of this project has been changed, but that project provided an outline for this one.
    - I spent several hours watching videos by John Elder on his channel [Codemy.com](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy), particularly his Django Wednesdays playlist. It would be impossible to list every line of my code that was influenced by his videos, though his most significant influence was in helping solidify my understanding of the Django framework as a whole.
    - Various forums such as Stack Exchange and Stack Overflow helped to solve small problems when I was stuck on a line of code.
- Individuals:
    - My Mentor, [Adegbenga Adeye](https://github.com/deye9), provided comments and feedback.
    - My wife, Megan, provided wonderful feedback, and, most importantly, saw me through the project by making every break a delight.

