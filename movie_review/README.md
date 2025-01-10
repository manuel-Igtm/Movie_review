## Movie Review API

### Overview
The **Movie Review API** is a Django-based project providing functionality to manage, search, filter, and interact with movie reviews. It includes authentication and allows users to create, update, and delete their reviews. The project also supports pagination, filtering, sorting, and searching to enhance the user experience.

### Features
- **CRUD Operations**: Users can create, read, update, and delete movie reviews.
- **Authentication**: Protected endpoints to ensure secure access.
- **Filtering**: Filter reviews by `movie_title` and `rating`.
- **Searching**: Search reviews by `movie_title` and `review_content`.
- **Sorting**: Sort reviews by `rating` or `created_at`.
- **Pagination**: Paginated results with customizable page sizes.

### Technology Stack
- *Backend*: Django, Django REST Framework
- *Database* : MYSQL
- *Authentication* : Django's built-in user authentication
- *Filtering*: Django Filter library

### Endpoints
| Endpoint               | HTTP Method | Description                           | Authentication |
|------------------------|-------------|---------------------------------------|----------------|
| `/reviews/`            | GET         | Get a list of all reviews             | Required       |
| `/reviews/`            | POST        | Create a new review                   | Required       |
| `/reviews/{id}/`       | GET         | Get a specific review                 | Required       |
| `/reviews/{id}/`       | PUT         | Update a review                       | Required       |
| `/reviews/{id}/`       | DELETE      | Delete a review                       | Required       |

### How to Run the Project
#### Prerequisites
- Python (>= 3.8)
- pip (Python package manager)
- Git
- Django and Django REST Framework
- `django-filter` library

#### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Movie_review
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000`.

#### Environment Variables
You can define your environment variables in a `.env` file. Examples include:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### Usage
1. Create a superuser to manage the project:
   ```bash
   python manage.py createsuperuser
   ```

2. Login to the Django admin panel at `/admin`.

3. Use tools like Postman or cURL to interact with the API.

### Contribution Guidelines
- Fork the repository.
- Create a feature branch.
- Commit your changes and push to the branch.
- Create a pull request explaining your feature.

