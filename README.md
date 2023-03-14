
Technologies
HTML, CSS, JavaScript, Python+Django
Relational database (recommending MySQL or Postgres)


Front end CRUD (Create Read Update Delete) functionality, including:
Front end UI elements that allow users to Create, Read, Update, and Delete records in the database, without having to access the admin panel.
The use of Agile methodologies:
Ensure you use an agile tool, such as Github projects, to track the tasks involved in creating your project.
Relate tasks to specifically identified user stories.
One or two tasks that cover all user stories will not be assessed as sufficient.
Ensure your GitHub project has public visibility, as it is private by default. Click on … then settings, then visibility to alter it.


Reddit style news site
External user’s goal:

Users want to post, read and comment on news stories.
Site owner's goal:

The site owner would like to create a discussion community.
Potential features to include:

Posts can be up/downvoted
Comments can be left on a post
Time/Date of posting
Topic groupings/categories



Learning Outcomes
LO1	Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies.
LO2	Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
LO3	Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution.
LO4	Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies
LO5	Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies.
LO6	Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform
LO7	Understand and use object-based software concepts



[__Setting up basic Django Project and Deploying to Heroku__](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

Install librieries:
pip3 install 'django<4' gunicorn
pip3 install dj_database_url==0.5.0 psycopg2
pip3 install dj3-cloudinary-storage

Create requirements.txt
pip3 freeze --local > requirements.txt

START NEW PROJECT 
django-admin startproject PROJECT_NAME .