"# todo_list" 

The "todo_list" project: A small dashboard for one person 
that functions as a notebook, where you can add tasks, 
task types (implemented as tags), and mark them as completed or not completed.

List of models:
1. Task(models.Model).
2. Tag(models.Model).

List of pages:
1. Login.
2. Homepage.
3. Tags.

To create a superuser:
python manage.py createsuperuser

Instructions for running locally:
1. git clone https://github.com/Black-and-white-689/todo_list.git
2. cd "project"
3. python -m venv venv
4. venv\Scripts\activate (on Windows)
5. source venv/bin/activate (on macOS)
6. pip install -r requirements.txt
7. python manage.py migrate
8. python manage.py createsuperuser
9. python manage.py runserver
