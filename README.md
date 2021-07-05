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
GET       'api/community'             list		ListAPIView
POST      'api/community'             create	CreateAPIView
GET       'api/community/<uuid:_id>'  retrieve	RetrieveAPIView
PUT/PATCH 'api/community/<uuid:_id>'  update	UpdateAPIView
DELETE    'api/community/<uuid:_id>'  destroy	DestroyAPIView
```

