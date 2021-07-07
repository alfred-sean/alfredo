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
GET       'api/communities'           list		ListCreateAPIView
POST      'api/communities'           create	CreateAPIView
GET       'api/communities/<uuid:id>' retrieve	RetrieveAPIView
PUT/PATCH 'api/communities/<uuid:id>' update	UpdateAPIView
DELETE    'api/communities/<uuid:id>' destroy	DestroyAPIView
```

## URLS
### Generic Views
```
/communities/
/communities/<uuid:id>
```

### ViewSets
```
/api/communities/
/api/communities/<uuid:id>
/api/addresses/
/api/addresses/<uuid:id>
```
