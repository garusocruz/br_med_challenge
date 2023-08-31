# br_med_challenge

> Build a Docker containers

```bash
    docker compose build --no-cache
```

---

> Load a Currency Fixture

```bash
    docker compose up -d brmed_database && docker compose run --rm brmed_api bash -c "
    python manage.py loaddata fixtures/currencies.json"
```

or

```bash
    sudo docker compose up -d brmed_database && sudo docker compose run --rm brmed_api bash -c "
    python manage.py loaddata fixtures/currencies.json"
```

---

> Run a project

```bash
    docker compose up
```

---
## To use example bellow you needs to have your server running at localhost:8000
> To access the Api see the examples bellow:
- [get rate by date](http://127.0.0.1:8000/rates/?date=2023-03-18)
- [get rate by date range](http://127.0.0.1:8000/rates/?date=2023-03-18&until_date=2023-03-23)
- [get all rates on DB](http://127.0.0.1:8000/rates)
```bash
    pip install poetry
```

---

> Start br_med_db database

```bash
    docker compose up -d
```
