# TaskMaster - API
## Project Description

TaskMaster is a web based platform that allows its users to manage their tasks, based on a categories that they assign a task, what the task is in terms of giving it a title and a description, whether it is urgent or not. They can assign a due date for when they need the task to be finished by. The application consists of the React app and an API. Welcome to the Django Rest Framework API project section.

### API Documentation Sections

In this API documentation, you'll find the following sections:

- **User Stories**: The functionality of the API and how it works for the user.

- **Entity Relationship Diagram**: Illustrates the relationships between different entities for a comprehensive overview.

- **Models and CRUD breakdown**: Delve into the specifics of API endpoints, including how to create, retrieve, update, and delete data, along with filtering and text search capabilities.

- **Tests**: Understand the quality assurance measures taken to ensure the reliability and functionality of the API.

- **Deployment steps**: Learn how to deploy the API to various environments, enabling you to use it effectively in your projects.

- **Acknowledgments**: Recognition of any libraries, frameworks, or tools used in the project.

## User Stories

### Authentication and User Profiles

| Category | as | I want to | so that I can | mapping API feature |
| :--- | :--- | :--- | :--- | :--- |
| Auth | User | Register for an account | Have a personal profile with a picture | dj-rest-auth Create profile (signals) |
| Auth | User | Log in to my account | Access my personalized dashboard | dj-rest-auth Login |
| Auth | User | Log out of my account | Ensure the security of my account | dj-rest-auth Logout |
| Auth | User | Reset my password | Regain access to my account | dj-rest-auth Password Reset |
| Profile | User | Update my profile information | Keep my profile up to date | Profile Update (API endpoint) |
| Profile | User | Upload a profile picture | Personalize my profile | Profile Update (API endpoint) |

### Task Management

| Category | As a | I want to | So that I can | Mapping API Feature |
| :--- | :--- | :--- | :--- | :--- |
| Tasks | User | Create a new task | Keep track of things I need to do | Task Create (API endpoint) |
| Tasks | User | Edit a task | to change details such as due date, description and complete status | Task Update (API endpoint) |
| Tasks | User | Delete a task | Remove unnecessary or completed tasks | Task Delete (API endpoint) |
| Tasks | User | Assign a category to a task | Organize my tasks efficiently | Task Create (API endpoint) |
| Tasks | User | Mark a task as completed | Track my progress | Task Update (API endpoint) |
| Tasks | User | Set a due date for a task | Prioritize my work | Task Update (API endpoint) |
| Tasks | User | Filter tasks by category | Find tasks related to specific projects | Task List (API endpoint) |
| Tasks | User | Filter tasks by complete status | Find tasks related to that are incomplete or completed | Task List (API endpoint) |
| Tasks | User | Filter tasks by urgent status | Find tasks related to are urgent | Task List (API endpoint) |
| Tasks | User | View all my tasks | Have an overview of my to-do list | Task List (API endpoint) |
| Tasks | User | View the number of incomplete tasks | Understand the urgency of my work | IncompleteTaskCountView (API endpoint) |
| Tasks | User | View the number of urgent tasks | Prioritize my immediate work | UrgentTaskCountView (API endpoint) |
| Categories | User | Create a new category | Organize my tasks effectively | Category Create (API endpoint) |
| Categories | User | Update a category | Modify the category's details | Category Update (API endpoint) |
| Categories | User | Delete a category | Remove unnecessary categories | Category Delete (API endpoint) |



## Entity Relationship Diagram

![image](https://github.com/Neillcllghn/drf_api_TO_DO_mock/assets/109948740/89887618-b823-4d3d-80c0-209c812caa34)


## Models and CRUD breakdown

| Model | endpoints | create | retrieve | update | delete | filter | text search |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| User | users/ users/:id | yes | yes | yes | no | no | no |
| Profiles | profiles/ profiles/:id/ | yes (signals) | yes | yes | no | no | no |
| Tasks | tasks/ tasks/:id | yes | yes | yes | yes | completed, urgent | title |
| Tasks | incomplete-task-count/ | no | yes | no | no | no | no |
| Tasks | urgent-task-count/ | no | yes | no | no | no | no |
| Category | category/ category/:id | yes | yes | yes | yes | no | title |

## Tests

- **Tasks app:**
  - logged out users cannot list tasks.
  - logged in users can create a task.
  - logged out users can't create a task.
  - logged in users cannot create a task without a category.
  - logged out users cannot retrieve a tasks with a valid id.
  - logged out users can't retrieve a tasks with an invalid id.
  - logged in users can update a task they own.
  - logged in users can't update a task they don't own.
  - logged in users can't create a task if all fields are blank.
  - logged in users can't create a task with a due date in the past.
 
- **Category app:**
  - logged out users cannot list categories.
  - logged in users can create a category.
  - logged out users can't create a category.
  - logged out users cannot retrieve a category with a valid id.
  - logged out users can't retrieve a category with an invalid id.
  - logged in users can update a category they own.
  - logged in users can't update a category they don't own.

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python files. All files returned no errors or warnings.

## Deployment steps

- **set the following environment variables:**
  - CLIENT_ORIGIN
  - CLOUDINARY_URL
  - DATABASE_URL
  - DISABLE_COLLECTSTATIC
  - SECRET_KEY
  
- **installed the following libraries to handle database connection:**
  - psycopg2
  - dj-database-url

- **configured dj-rest-auth library for JWTs**
- **set allowed hosts**
- **configured CORS:**
  - set allowed_origins
  
- **set default renderer to JSON**
- **added Procfile with release and web commands**
- **gitignored the env.py file**
- **generated requirements.txt**
- **deployed to Heroku**


##  Acknowledgments:

I would like to acknowledge the following people and notes/other material used for this project:

- Jubril Akolade - My Code Institute Mentor.
- The Code Tutors for assisting me with errors I was running into from time to time and testing my code to confirm that they were free of bugs.
- The various leactures and notes - Django Rest Framework Walkthrough on the Moments API was of great benefit and was the foundation for this project.
- ChatGBT - for troubleshooting issues that I encountered and review of code (mistakes or errors in code that I could not see).
