
### Install
```shell

```

### Lint
```shell
flake8 --ignore E501,E251 common/
flake8 --ignore E501,E251 stocks/
```


### Model
```shell
python manage.py makemigrations stocks
python manage.py sqlmigrate stocks 0001
python manage.py migrate
```