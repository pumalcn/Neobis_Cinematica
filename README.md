# Neobis E-Store
"e Store" is an online platform offering a wide range of products for convenient purchasing and selling. Our project aims to provide users with a simple and secure way to buy and sell goods online.

## Table of Contents
- [Tech Stack](#tech_stack)
- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)

# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23336791.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-%236DB33F.svg?style=for-the-badge&logo=swagger&logoColor=white)


## Installation

### Cloning from GitHub Repository

To get started with the URL shortener, you can clone the repository from GitHub using the following steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pumalcn/Neobis_E-Store_Project.git
 
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   py -m venv myworld
   myworld\Scripts\activate.bat
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
5. Create a superuser account (for admin access)
   ```bash
   python manage.py createsuperuser
   
6. Start the development server:
   ```bash
   python manage.py runserver
   
7. Open your web browser and go to http://localhost:8000 to access the E-Store.

## Contributing

We welcome contributions to improve the REST API's. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and test them thoroughly.

4. Submit a pull request with a clear description of your changes.

5. Ensure your code follows best practices and includes necessary tests if applicable.
