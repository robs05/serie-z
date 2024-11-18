## Comandi git

### Clone repository
```bash
git clone [ulr]
```

### Reset main/origin
```bash
git fetch origin
git reset --hard origin/main
```

## Comandi django

### Create virtual environment
```bash
python3 -m venv .venv
```

### Activate virtual environment
```bash
source .venv/bin/activate
```
per windows
```bash
.venv\Scripts\activate
```

### Deactivate virtual environment
```bash
deactivate
```

### Install Django
```bash
pip install django
```

### Create database
```bash
python manage.py migrate
```

### Update database
```bash
python manage.py makemigrations [nome_app]
python manage.py migrate
```

### Run server
```bash
python manage.py runserver
```
