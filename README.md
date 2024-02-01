# MenuMinglee

Welcome to the README for MenuMinglee! This document provides information on how to set up and launch the project locally also the project description, architecture and the workflow of how the project was developed.

## Prerequisites

Before getting started, ensure you have the following installed on your machine:

- Python (3.x recommended)
- pip (Python package installer)
- virtualenv (recommended for isolating project dependencies)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/nafizfouad/MenuMinglee.git

2. Navigate to the project directory:

    ```bash

   cd MenuMinglee

3. Create a virtual environment (optional but recommended):

    ```bash

    python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash

    .\venv\Scripts\activate
    ```

    On macOS/Linux:

    ```bash

    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash

    pip install -r requirements.txt
    ```

6. Apply database migrations:

    ```bash

    python manage.py migrate
    ```

7. Create a superuser (for Django admin access):

   ```bash

   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash

   python manage.py runserver
   ```



# Project Description

## Overview

The MenuMinglee Web App is a Django-based solution developed for Brain Station 23 PLC, one of the largest and fast-growing companies in our country. The company faced challenges in providing diverse lunch options to its employees due to varying preferences. To address this, the app allows employees to vote for their favorite dishes from displayed restaurant menus. The menu with the most votes is chosen for the day, ensuring a fair and enjoyable lunch selection process.

## Features

### Authentication

The app incorporates robust authentication to secure user accounts and ensure a personalized experience. 
There are two types of users who will be using this system:
- Restaurant Owners
- Employees

   ![Sign In Page](https://drive.google.com/file/d/1nnNDFtZiupBffPMmcIbFQqeZYWrJyw9C/view?usp=drive_link)
  
<figure>
  <img src="https://drive.google.com/file/d/1YCermiV0kIm4_OoTLBfzhKDiTQnAqxfP/view?usp=drive_link" alt="Sign Up Page">
  <figcaption>Signup Page.</figcaption>
</figure>


### Restaurant Management

- **Creating Restaurant:** Administrators/restaurant owners can create new restaurants to participate in the lunch voting process.
- **Uploading Menu:** Restaurants can upload their menus, showcasing the variety of dishes they offer.


<figure>
  <img src="https://drive.google.com/file/d/1MTV2xQzsw0Mt7159yVsp0yrzzhKhzkvW/view?usp=drive_link" alt="Updating Menu">
  <figcaption>Updating Menu.</figcaption>
</figure>


### Employee Management

- **Creating Employee:** New employees can be added to the system, allowing them to participate in the voting process.
<figure>
  <img src="https://drive.google.com/file/d/1vmLNs9e_IksR1b6_x6mevzmU7oBBpJYt/view?usp=drive_link" alt="Employee Creation Successful">
  <figcaption>Employee Registration Successful.</figcaption>
</figure>

### Voting Process

- **Getting Current Day Menu:** Users can view the menus of participating restaurants for the current day.
- **Voting for Restaurant Menu:** Employees can cast their votes for their preferred dishes and contribute to the decision-making process.
<figure>
  <img src="https://drive.google.com/file/d/1-01DaGC4ADplS5O2_yWgf30d73klocAo/view?usp=drive_link" alt="Menu">
  <figcaption>Restaurant Menu.</figcaption>
</figure>  
<figure>
  <img src="https://drive.google.com/file/d/1_mZwY856LhPZsM7nVy-bk938I1poOsYx/view?usp=drive_link" alt="Voting Process">
  <figcaption>Voting Process.</figcaption>
</figure>  

### Results and Restrictions

- **Getting Results:** The app displays the results of the voting process, revealing the winning restaurant and menu for the day.
- **Anti-Repetition Rule:** To maintain variety, the winner restaurant is restricted from winning for three consecutive working days.
<figure>
  <img src="https://drive.google.com/file/d/1BNlOsT8e8enr-o_g2jyTHRanFSYrHx2_/view?usp=drive_link" alt="Vote Result for a day">
  <figcaption>Vote Result for a day.</figcaption>
</figure>  

### Logout

For security and user management, the app includes a logout feature to end user sessions.

## Implementation

The MenuMinglee Web App is implemented using the Django web framework, providing a scalable and maintainable solution. The app features a clean and intuitive interface, making it easy for both administrators and employees to navigate and participate in the lunch voting process.



