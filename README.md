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

