# Superheroes Unite

Superheroes Unite is my fourth portfolio project and is a Superhero blog with posts relating to the Marvel and DC Universes. It's aimed at anyone who has an exisitng, or new interest in the world of superheroes, and who may be keen to submit their own comments on existing posts.

The full website is available to view [here](https://project4-blog-ap-0464f823fc69.herokuapp.com/)

![am-i-responsive](static/images/am-i-responsive.png)

## UX Design

### **Project Goals**

The primary goal for this project was to create a blog with full CRUD functionality so that users can register an account, view posts, add comments and also edit and delete them if needed.

### **Strategy**

An agile methodology was used when planning this project - a kanban board ([view it here](https://github.com/users/alanpaterson82/projects/7/views/1)) was used in Github with various issues having their own acceptance criteria and tasks to be completed.

## User Stories

As a user admin I can review and manage all content so that all inappropriate or irrelevant details can be removed

* AC1 - When logged in, they can read, review, edit and delete comments and posts

<br>

As a new user I can register my details so that I can access my account and post personalised content

* AC1 - Username/ email field to be added
* AC2 - Unique password field to be added
* AC3 - When logged in they can post under their unique details

<br>

As a site user I can comment on posts so that I can interact with others through personalised views and responses

* AC1 - When logged in, a user can add a comment
* AC2 - When logged in, any other users can respond
* AC3 - A conversation can be started

<br>

As a guest user I can view all posts so that I can gain information

* AC1 - A guest user can click on, and read, all comments and posts but will be unable to leave their own comment

<br>

As a site user I can edit and delete my comments so that I am in control of my personal content

* AC1 - When logged in, they can delete their existing comments
* AC2 - When logged in, they can amend their existing comments

<br>

As a site user I can click on the Background link so that I can learn about the history of the blog content

* AC1 - When the background link is clicked the content is available to read

<br>

As a site admin I can update and amend the Background page so that it remains informative

* AC1 - The Background app can be seen in the admin portal

<br>

As a site user I can leave a comment so that the site admin can receive feedback

* AC1 - Site user can leave their personalised feedback
* AC2 - To leave a testimonial, input your name, username and message

<br>

As a site admin I can review testimonials so that the site can be improved where needed

* AC1 - Testimonials to be stored in the database for review

## Features

**Navigation Bar when logged out**

![navigation bar](static/images/navigation-bar-logged-out.png)

**Navigation Bar when logged in**

![navigation bar 2](static/images/navigation-bar-logged-in.png)

**Homepage**

![homepage](static/images/homepage.png)

**Background & Testimonial Page**

![background and testimonial](static/images/background-and-testimonial-page.png)

**Comments Page - Example**

![comments page](static/images/comments-page.png)

**Django Administration**

![django administration](static/images/django-administration.png)


## Technologies

**Languages:**

- Python
- JavaScript
- HTML5
- CSS

**Framework:**

- Django

**Database:**

- PostgreSQL

**Other**

- ElephantSQL
- GitHub - for storage and monitoring of the user stories
- Heroku - to deploy the app
- Cloudinary
- Chrome Developer Tools - to test responsiveness and generate a Lighthouse report
- Font Awesome - for any site icons
- Am I Responsive - to demonstrate suitability on all devices
- CI's Python Linter - for automated testing of the Python code
- W3C Markup Validator - to test the HTML code
- W3C CSS Validator - to test the CSS code

## Manual Testing

Unfortunately, due to time constraints I was unable to complete the intended manual testing, however, testing was completed as the project took shape to ensure that there were no obvious issues.
<br>

![forms.py testing](static/images/forms-py-testing.png)

## Browser compatibility

Tested in Google Chrome and on an iphone 13 Pro Max

## Bugs resolved & unresolved

![module-not-found](static/images/ModuleNotFoundError.png)

When implementing the testimonial form, there were various errors received (example above) due to incorrect coding which was eventually resolved using various resources including:

- Stack Overflow
- The Slack Community

There was a query regarding committing insecure keys, however this was resolved with the clarification of env.py being included in the .gitignore file.

As I was referencing the walkthrough project, and was initially using CodeAnywhere before transferring to Gitpod Workspaces, there were certain queries to be overcome, including replacing existing code such as the CSRF Trusted Origins being amended to gitpod.io.

When trying to migrate with 0001_initial.py I received the following error:

_It is impossible to add a non-nullable field 'content' to post with specifying a default. From the source code, content = models. TextField() had no content in the parentheses._

The above was resolved with a system reset via Tutor Support.

The latter deployments to Heroku don't appear to be successful in transferring the stylistic changes that have been made, however, all of the relevant forms, notifications and commands appear to be working, as well as the Django Administration functions. This may be related to the Debug value (True/ False).

## Lighthouse testing

![lighthouse](static/images/lighthouse.png)

## Code validation

**W3C Markup**

![W3C Markup Validation](static/images/w3c-markup-validation.png)

**W3C CSS**

![W3C CSS](static/images/w3c-css.png)


## Deployment

The application was deployed to Heroku and this was completed following the steps below;

- Logging in to the Heroku dashboard
- Clicking on 'New' then 'Create new app'
- Choosing a unique name for the app and clicking 'create app'
- Clicking on the 'Resources' tab and deleting any existing add-ons
- Navigating to the Settings tab and clicking on 'Reveal Config Vars'
- Copying the DATABASE_URL url value to the clipboard
- Creating a new env.py file in the top level directory and completing as below

<br>

![env.py](static/images/env-py.png)

- **The secret key should be unique to you**

- In Heroku clicking on 'Settings' then 'Reveal Config Vars'
- Adding SECRET_KEY to the Config Vars with the unique key as the value

<br>

The Heroku resources tab should mirror the below;

<br>

![heroku](static/images/heroku.png)

When the project is ready to be submitted, the following actions must be taken;

- Set Debug to False in settings.py
- Git add, commit and push all changes
- Deploy on Heroku by clicking Deploy Branch in the Deploy tab

<br>

![deploy-branch](static/images/deploy-branch.png)


## References

This project relied heavily on following the walkthrough project 'I Think Therefore I Blog', with customisation added to demonstrate my capability and produce an interesting and unique app for users. Any direct copying of existing code is completely unintentional

[Medium.com](https://medium.com/) for inspiration

## Future Actions/ Features

- Significantly more testing to ensure that everything is in working order
- Detailed database schema diagrams
- Addition of labels and milestones
- More detailed user stories
- Debugging
- Improved styling
- Increased functionality when logged in eg ability to reset passwords
- Increased functionality when trying to post a comment when not logged in i.e sending the user back to the login page
- Increased security for editing and deleting comments



