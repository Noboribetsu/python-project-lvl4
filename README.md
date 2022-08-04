### Description:
Task Manager – система управления задачами, подобная http://www.redmine.org/. Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация.
Не зарегестрировану пользователю доступен только список пользователей.
Задачи, Статусы, Метки доступны после регистрации.

### Link:
https://sleepy-temple-25868.herokuapp.com/

### Requrements:
* Python 3.9+
* Poetry
* GNU Make

### Setup:
```bash
make setup
```
### Run server
```bash
make start
# Open http://0.0.0.0:8000/
```

## Check codestyle
```bash
make lint
```

## Run tests
```bash
make test
make test-coverage # run tests with coverage report
```



### Hexlet tests and linter status:
[![Actions Status](https://github.com/Noboribetsu/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/Noboribetsu/python-project-lvl4/actions)

### Codeclimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/6b998c5b391bf7d8aacf/maintainability)](https://codeclimate.com/github/Noboribetsu/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6b998c5b391bf7d8aacf/test_coverage)](https://codeclimate.com/github/Noboribetsu/python-project-lvl4/test_coverage)

### CI:
[![Project CI](https://github.com/Noboribetsu/python-project-lvl4/actions/workflows/projectci.yml/badge.svg)](https://github.com/Noboribetsu/python-project-lvl4/actions/workflows/projectci.yml)
