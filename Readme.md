This is a Django-based blog application that allows users to create, edit, and delete posts, categorize them, and interact via comments. It includes user authentication, a personal dashboard for managing posts, and an admin panel for managing categories and comments. Posts have automatic slugs for SEO-friendly URLs, and only authenticated users can create content or comment. The project demonstrates essential Django features such as models, forms, class-based views, and the built-in authentication system.


python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver