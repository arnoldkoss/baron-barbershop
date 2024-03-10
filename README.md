# Baron Barbershop
Welcome to the official website of Baron Barbershop, the premier destination for those seeking a blend of traditional craftsmanship and modern styling in the heart of the city. Our website is designed to provide our patrons with a seamless experience, offering a glimpse into our world where precision meets artistry.

Under the hood, Baron Barbershop operates on the robust Python programming language, leveraging the Django framework to ensure a dynamic and efficient web experience. The front-end design is meticulously developed with Bootstrap CSS and JavaScript, offering an intuitive and responsive user interface. Additionally, Baron Barbershop's deployment on the Heroku cloud platform ensures seamless accessibility and scalability, providing a reliable service directly from the cloud.

The live site is here: [Baron Barbershop](https://baron-barbershop-8a2745877c29.herokuapp.com/)



## CONTENT
### Technologies Used
  - GitHub – storage and deployment
  - Heroku - Deployment
  - Cloudinary - Cloud storage for static images
  - ElephantSQL - for database hosting

### Languages Used 
Python, HTML/CSS, Java Script

### Frameworks, Libraries & Programs Used
- Git / Github
- Bootstrap
- Django-allauth
- Django-crispy-forms
- Django-summernote
- Pexels (Imaging Library)
- Font Awesome
- Google Fonts

### User Experience and Workflow
#### Target Audience
Our website is designed with our diverse clientele in mind—individuals who value not just a haircut, but a grooming experience. Whether you're a regular who's been with us since day one, a newcomer looking to find your new go-to spot, or someone in need of a quick trim or a complete makeover, we've got you covered. We cater to all ages and styles, from classic cuts to the latest trends. Our target audience is anyone who appreciates attention to detail, a welcoming atmosphere, and the skillful artistry of experienced barbers. 

#### User Stories
Features in this project are structured through [User Stories](https://github.com/arnoldkoss/baron-barbershop/issues?q=is%3Aissue+is%3Aclosed).


 Each User Story contains:
- User Objective: This field outlines the user's goal or objective. It should clearly state what the user wants to achieve or accomplish. The format follows: "As a user, I can [action], so that [reason or benefit]." With this Objective in mind, User Stories are created to align with the target audience.
- Acceptance Criteria: This field specifies the conditions or criteria that must be met for the user story to be considered complete. It helps define the boundaries and expectations for implementing the user story.

#### Workflow
In the development process, a Kanban board in form of a [github project](https://github.com/users/arnoldkoss/projects/5/views/1) is used to manage the tasks and track their progress. Initially, all issues are collected and placed in the backlog. During each iteration, a set number of issues are selected to be developed. These selected issues are then moved to the 'To Do' column on the Kanban board, indicating that they are ready to be worked on.

When working on the tasks begins, the status of the issues is updated to 'In Process'. This signifies that active development is underway.

If an issue meets the acceptance criteria it is considered 'Done' and is moved to the final column on the Kanban board.

![Kanban Board](/static/images/readme/kanbanB.png)


### Design
#### Colour Scheme
![Color Scheme](/static/images/readme/colorScheme.png)
For the Baron Barbershop website, I've carefully selected a color scheme that embodies the essence of our brand, offering a modern twist on the classic barbershop experience. Our palette combines #212529 (Eerie black), #D3D3D3 (Timberwolf), and #343A40 (Onyx), chosen for their timeless elegance and versatility.

#### Typography
![Typography](/static/images/readme/googleFonts.png)
I went for a Google 'Annapurna SIL'  for its unique blend of traditional elegance and modern clarity. This font, with its roots in the Devanagari script, evokes a sense of worldly sophistication and cultural richness, aligning perfectly with our barbershop's ethos of combining classic grooming traditions with contemporary style. I used it in the navbar and footer.

### Wireframes
#### PC
![Home wireframe](/static/images/readme/wireframeHome.png)

![About wireframe](/static/images/readme/aboutPage.png)

![Our Work wireframe](/static/images/readme/wireframeOurWork.png)

#### Mobile

![Home wireframe mobile](/static/images/readme/wfHomeTel.png)

![About wireframe mobile](/static/images/readme/wfAboutTel.png)

![Our Work wireframe mobile](/static/images/readme/wfOurWorkTel.png)

### Features

- ### Navigation Bar
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.
  - Featured on all pages, the full responsive navigation bar includes links to the Logo, Home page, About, Our Work, Reservations, Register, Login and Logout page and is identical in each page to allow for easy navigation.

  People who haven't created a user account yet have the option to sign in. People with user accounts can use the login.

#### Visitors

PC
![Navbar PC](/static/images/readme/navbarPC.png)

Mobile
![Navbar mobile](/static/images/readme/navbarMobile.png)


For people that have registered, the Navigation Bar gives the Users easy acces to the Reservations page.

#### Signed-In Users

![Navbar reservations](/static/images/readme/navbarRes.png)



- ### User Account

The User Accounts in this project are managed by the AllAuth Django package.

- ### User Sign up

Users can register on the page with a username, an optional email, and password. After registration all their information is stored in the database.

![Sign Up Page](/static/images/readme/signUp.png)


- ### User Login

Registered users can log in to their accounts using their credentials.
![Login Page](/static/images/readme/login.png)


- ### User Logout

Logged-in users can log out of the site by clicking the logout link in the navigation bar. They have to confirm their decision.

![Logout Page](/static/images/readme/logout.png)

- ### User Content Display

The Our Work page displays all posts created by the admin from the admin panel.

![Our Work posts](/static/images/readme/owPost.png)

![Our Work post](/static/images/readme/bPost.png)


- ### User Comment section

Logged-in users can create comments on the platform. Comments appear below the thread they relate to.

Comment awaiting for admin approval.

![comment pending](/static/images/readme/commentPend.png)

Comment approved by admin.

![comment approved](/static/images/readme/commentAppr.png)

Comment count is updated also.

![comment count](/static/images/readme/commCount.png)

As a logged-in user you can update or delete your own comment

![comment update delete](/static/images/readme/updateDel.png)

After the comment was created or updated a confirmation message is displayed.

![confirmation message](/static/images/readme/pendMessage.png)

When a user wants to delete a comment, a confirmation modal is displayed.

![confirmation modal](/static/images/readme/confModal.png)

- ### User About section

The About page showcases a description and an image curated by the admin through the admin panel.

![about page](/static/images/readme/aboutPageS.png)

- ### User Reservation section


The reservation section allows logged-in users to schedule a service by providing their name, desired date, preferred time, and gender. After the reservation is made, the booking is displayed in the admin panel for management and tracking purposes.

![reservation page](/static/images/readme/resPage.png)

After the reservation is made, the user receives a confirmation message containing the date and time of the booking

![reservation message](/static/images/readme/resTime.png)

- ### User Home page, Information section

The home page serves as a hub for information about the barbershop, featuring a brief self-description along with details about the services provided.

![home page](/static/images/readme/homeInf.png)

- ### Pagination
For a better load time and usage with multiple threads, the blog has a pagination feature.

![pagination](/static/images/readme/pag.png)

- ### Messages

Users get notified about changes on the platform through the django message system.

![django message](/static/images/readme/loginMess.png)


- ### Django Admin Panel
Inside the Django Admin panel, Administrators have acces to the models of the django project.

![admin panel](/static/images/readme/admin.png)

### Features Left to Implement

- Implement CRUD capability to allow users to update or delete reservations.
- I Consider adding a profile page for users to manage their information and preferences.
- I Explore the possibility of adding a feature for users to like posts or content for increased engagement and interaction.

### Data
#### Database schema
- Posts ERD
![posts ERD](/static/images/readme/PostsERD.png)

- Comments ERD
![comments ERD](/static/images/readme/commentsERD.png)

- Reservations ERD
![reservations ERD](/static/images/readme/ReservERD.png)

- About post ERD
![about page ERD](/static/images/readme/aboutERD.png)

### Security

I strive to maintain optimal security measures in my Django project. I've ensured that only logged-in users can perform specific actions within the app. When a comment is made but not yet approved by the admin, only the author can view, update, or delete the comment. It's only after the admin's approval that the comment becomes visible to all users. Additionally, non-logged-in users are unable to leave comments; instead, they see a message prompting them to log in first before leaving a comment. These steps ensure both security and user engagement within the platform. Similarly, only logged-in users have the capability to make reservations, further enhancing security while fostering user engagement within the platform.

The safety of user registration and login processes by integrating the AllAuth Django extension. This extension provides a robust framework for managing user authentication securely, offering features such as secure password storage and authentication workflows.

Sensitive information (such as the email adress) remains accessible only to authorized individuals, like admins an the owner of the data. Users are restricted from viewing or accessing sensitive data belonging to other users. This is due to the database, which requires a login.

### Testing

![lighthouse](/static/images/readme/lighthouse.png)
![lighthouse](/static/images/readme/lighthouse2.png)

### Jigsaw CSS Validator


The Jigsaw CSS Validator does not throw any errors.

![jigsaw validator](/static/images/readme/jigsaw.png)

### W3C Validator

The W3C HTML Validator shows no errors.

Home page
![Home](/static/images/readme/homeValidation.png)

Our Work page
![Our Work](/static/images/readme/blogValidator.png)

Post
![Post](/static/images/readme/postValidation.png)

Reservation page
![Reservations](/static/images/readme/resValidation.png)

Logout page
![logout](/static/images/readme/logoutValidation.png)

### JS Hint Validator
The JS Hint Validator shows no errors.

![JShint](/static/images/readme/JShint.png)

### PEP8
The Pep8 CI Linter has been diligently applied, ensuring that all files adhere impeccably to the esteemed guidelines of PEP 8.

### Manual Testing
#### Sign Up, invalid Sign Up, Login, invalid Login, Logout testing table:

| Feature       | Expected Outcome                                                                                         | Testing Performed                                                                                   | Result                                                                    | Pass/Fail |
|---------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-----------|
| Sign Up       | When the User is signing up with valid credentials, an account should be created. After Signing up, the User is logged in. (Email is optional) | Signing up with username = test, email = test@test.se, password = Secure123!                        | The User is logged in. An Account has been created.                       | Pass      |
| Invalid Sign Up | When the User is signing in with invalid credentials, they get informed about the invalid data.            | Signing up with username = superlongusername123456789superlong, password = 123 | The User gets informed about an invalid password. The Username gets shorten to the appropriate length after creation. | Pass      |
| Login         | Can login in with the correct password and username.                                                      | Login with username = test, password = Secure123!                                                    | User is logged in.                                                        | Pass      |
| Invalid Login | Users can't login with invalid credentials.                                                               | Login with username = test, password = InSecure123!                                                  | The user is not logged in.                                                | Pass      |
| Logout        | After Confirming to logout, the user gets logged out.                                                     | Pressing Button to confirm the logout.                                                               | User is logged out.                                                       | Pass      |

#### Comments testing table:

| Feature    | Expected Outcome                                                                                                     | Testing Performed                                                                                     | Result                                                                                     | Pass/Fail |
|------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------|
| Submit Comment | When a logged-in user fills the comment form and clicks on submit, the expected result is the comment is pending for admin approval. | A logged-in user fills the comment form and submits.                                                  | The comment is pending for admin approval.                                                 | Pass      |
| Edit Comment  | When the user clicks on edit, the expected result is that the comment they wrote reappears in the comment form and the user can update. | A user clicks on edit for their comment.                                                              | The comment reappears in the comment form for updating.                                    | Pass      |
| Delete Comment | When the user clicks on delete, the expected result is that a modal appears with the options to close the modal or confirm the delete of the comment. If the user clicks on delete, the comment is deleted. | A user clicks on delete for their comment, a modal appears, and they confirm the delete. | A modal appears with options to close or confirm deletion. After confirming, the comment is deleted. | Pass      |


#### Reservations testing table:

| Feature                  | Expected Outcome                                                                                                   | Testing Performed                                                                                                    | Result                                                                                                                   | Pass/Fail |
|--------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
| Complete Booking Submission | When a user fills in the reservation form with their name, date for booking, time, gender, and submits, a reservation is created and a confirmation message is displayed. | A user fills in the form with valid details including name, date (at least one day in advance), time, gender, and submits. | The reservation is successfully created, and the user receives a Django message confirming the date and time of the booking. | Pass      |
| Incomplete Booking Submission | The form cannot be submitted if any required field (name, date, time, gender) is missing.                              | A user attempts to submit the form with one or more required fields missing.                                          | The submission is prevented, and the user is informed that all fields must be completed.                                | Pass      |
| Booking Date Too Soon      | The user is alerted if the booking date is not at least one day in advance.                                           | A user attempts to book a reservation for the current day.                                                             | The user receives an alert message that they must choose a date at least one day in advance.                           | Pass      |


#### About page testing table:

| Feature                 | Expected Outcome                                                                                       | Testing Performed                                                                                   | Result                                                                                          | Pass/Fail |
|-------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------|
| Post About Page Content | When the admin user posts new content to the About page, including a picture, the changes are visible on the About page. | The admin uploads a picture and creates content for the About page, then publishes the changes.   | The new content and picture are successfully posted and visible on the About page.             | Pass      |
| Update About Page Content | When the admin user updates existing About page content, including changing the picture, the updates are immediately reflected. | The admin edits the existing About page content, changes the picture, and updates the changes. | The updated content and new picture are successfully reflected on the About page.              | Pass      |


#### Our Work page testing table:

| Feature            | Expected Outcome                                                                                                                  | Testing Performed                                                                                                                      | Result                                                                                                                       | Pass/Fail |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------|
| Create New Post    | When the admin creates a new blog post with a title, username, optional image, content, status (draft or published), and an excerpt, the post is saved accordingly. | The admin navigates to the blog post creation panel, fills in the title, chooses a username, optionally picks an image, writes content, selects the status, writes an excerpt, and saves. | The blog post is successfully saved with the provided details, and its status is correctly set as either draft or published.  | Pass      |


#### Admin comment approval table:

| Feature                | Expected Outcome                                                                                          | Testing Performed                                                                                       | Result                                                                                        | Pass/Fail |
|------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------|
| Approve User Comment   | When the admin approves a pending comment, the comment becomes visible on the site under the relevant post. | The admin navigates to the comment management panel, selects a pending comment, and approves it.       | The comment is successfully approved and becomes visible on the site.                         | Pass      |
| Disapprove User Comment | When the admin disapproves a pending comment, the comment is deleted and not visible on the site. | The admin navigates to the comment management panel, selects a pending comment, and disapproves it.    | The comment is successfully disapproved and is not visible on the site.                       | Pass      |


### Automatic Testing

This project contains Unittests to automatically test the application.
Tests were performed for the about page views.py, for the blog forms.py and views.py, and for the reservations page forms.py and views.py.

![python tests](/static/images/readme/tests.png)

### Deployment

#### Deployment Using Github
- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

#### Deployment Using Heroku

- Register for an account on Heroku or sign in.
- Create a new app.
- Name your App.
- Connect your github repository to Heroku app.
- Create a Live Database by adding the 
ElephantSQL  add-on.
- Create and Set up an email account for verification mails.
- Deploy from "deploy", or choose an automatic deploy option.

### Credits

#### Code used

I used the Blog walkthrough project as inspiration for the blog section of my project, but not to the full extent. I have tailored it to fit my view of how the site should look.

#### Content

- The icons in the footer were taken from Font Awesome
- The pictures used were taken from Pexels.com
- Django pagination
- I learned about django unittests from The Dumbfounds

#### Acknowledgments

I want to thank my mentor Luke for his great guidance and support and to the CI tutors for the great help I got.