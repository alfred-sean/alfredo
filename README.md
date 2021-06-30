## Running the app
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py init_db [-n <num_of_facilities>]
python manage.py runserver
```