# Movie Review API

## Setup Instructions

### Prerequisites
- Python 3.x
- pip
- Virtual Environment

### Installation
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

