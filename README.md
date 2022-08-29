# EV Forklift Fastapi
clone project
```
git clone git@github.com:cuongtv-smartosc/template-fastapi.git
cd template-fastapi
```

# Requirements
1. `>= Python 3.10`

## Install environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Install pre-commit
```
pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## [Option] Run docker-compose
```
docker-compose up -d
```

## Run dev server
```
uvicorn main:app --reload
```

online doc address
```
http://127.0.0.1:8010/redoc
```

## Run test
Create new database for test and update in config.yml file
```
DB_DATABASE="db_test"
```
Run test
```
pytest
```
