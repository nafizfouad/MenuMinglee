# MenuMinglee

Welcome to the README for your Django project! This document provides information on how to set up and launch the project locally.

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
