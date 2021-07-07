## Running the app
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py init_db [-n <num_of_facilities>]
python manage.py runserver
```

## API Design

```
Methods   URL                         Function  CBV
GET       'api/community'             list		ListCreateAPIView
POST      'api/community'             create	CreateAPIView
GET       'api/community/<uuid:id>'  retrieve	RetrieveAPIView
PUT/PATCH 'api/community/<uuid:id>'  update	UpdateAPIView
DELETE    'api/community/<uuid:id>'  destroy	DestroyAPIView
```

