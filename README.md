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
![Login Page](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Login%20Page.jpg)
  
![Signup Page](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Signup%20Page.jpg)

### Restaurant Management

- **Creating Restaurant:** Administrators/restaurant owners can create new restaurants to participate in the lunch voting process.
  ![Creating Restaurant](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Creating%20Restaurant.jpg)
- **Uploading Menu:** Restaurants can upload their menus, showcasing the variety of dishes they offer.

![Uploading Menu](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Menu.jpg)


### Employee Management

- **Creating Employee:** New employees can be added to the system, allowing them to participate in the voting process.
 ![Creating Employee Account](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Authentication%20Successful.jpg)


### Voting Process

- **Getting Current Day Menu:** Users can view the menus of participating restaurants for the current day.
![Available Restaurants](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Available%20restaurants%20with%20menu.jpg)

   ![Getting Menu](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Menu.jpg)
   
- **Voting for Restaurant Menu:** Employees can cast their votes for their preferred dishes and contribute to the decision-making process.

  ![Voting Process](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Voting%20Process.jpg)


### Results and Restrictions

- **Getting Results:** The app displays the results of the voting process, revealing the winning restaurant and menu for the day.
- **Anti-Repetition Rule:** To maintain variety, the winner restaurant is restricted from winning for three consecutive working days.
 
![Vote Results](https://github.com/nafizfouad/MenuMinglee/blob/main/Screenshot/Vote%20Count%20of%20a%20particular%20day.jpg)

### Logout

For security and user management, the app includes a logout feature to end user sessions.

## Implementation

The MenuMinglee Web App is implemented using the Django web framework, providing a scalable and maintainable solution. The app features a clean and intuitive interface, making it easy for both administrators and employees to navigate and participate in the lunch voting process.



