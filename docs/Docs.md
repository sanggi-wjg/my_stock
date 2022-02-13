### Commands
```shell

```

### Lint
.flake8 파일 작성 후
```shell
# 폴더별
flake8 --ignore E501,E251 common/
flake8 --ignore E501,E251 stocks/

# 전체
flake8 .
```

### Coverage
.coveragerc 파일 작성
```shell
coverage run --source='.' manage.py test

# 통계
coverage report
# Html 로
coverage html
# 이전 기록 삭제
coverage erase
```

### Test
```shell
python manage.py test
```

### Model
```shell
python manage.py makemigrations stocks
python manage.py sqlmigrate stocks 0001
python manage.py migrate
```