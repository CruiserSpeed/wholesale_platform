# Структура проекта
```
whosale_platform
|-- backend
|    |-- protos          // grpc-сервисы
|    |-- admin_app       // бэкенд админки
|    |    | Dockerfile
|    |    |-- src
|    |    |    | run.py  // entrypoint
|    |    |-- tests
|    |    | build.sh     // сборка контейнера
|    |    | run.sh       // запуск контенера
|    |    | .env         // admin-env для запуска без контейнера
|    |-- admin_db        // контейнер с базой данных для админки
|    |    | Dockerfile
|    |-- api_walker      // микросервис для оценки товаров/поставщиков
|    |    | Dockerfile
|    |    | -- src
|    |    | -- tests (TODO)
|    |...                // остальные бэки
|-- frontend
|    |-- admin-app       // фронт админки
|    |...                // остальные фронты
| docker-compose.yaml
| build.sh               // сборка композа
| run.sh                 // запуск композа
| .env                   // root-env
```

<br> 

# Запуск

## Запуск в контейнерах
Сборка\
`cd whosale_platform && ./build.sh`

Запуск\
`cd whosale_platform && ./run.sh`

Для запуска тестов нужно при запуске `run.sh` добавить один из флагов:
* `--test | -t`\
заупyск всех тестов
*  `--vital | -v`\
заупyск тестов без стайлчекинга

**NB**: должны быть определены необходимые переменный окружения:
<details>
<summary>Шаблон для root-env</summary>
<pre>
ADMIN_APP_EXTERNAL_PORT=5000
ADMIN_APP_INNER_PORT=5000
ADMIN_APP_IS_DEBUG=1
ADMIN_DB_USER=???
ADMIN_DB_PASSWORD=???
ADMIN_DB_PORT=5432
API_WALKER_EXTERNAL_PORT=50051
API_WALKER_INNER_PORT=50051
</pre>
</details>

<br>

## Локальный запуск бэка админки
Сборка\
`cd admin_app && ./build.sh`

Запуск\
`cd admin_app && ./run.sh`

Запуск тестов\
`cd admin_app && ./run_tests.sh`
(добавить `--vital | -v` для запуска без стайлчекинга)

**NB**:
нужно установить необходимые библиотеки\
`cd admin_app && pip install -r requirements.txt`\
а также должны быть определены необходимые переменный окружения:
<details>
<summary>Шаблон для admin-env</summary>
<pre>
DB_USER=postgres
DB_HOST=localhost
DB_PORT=5432
DB_PASSWORD=???
APP_PORT=5000
APP_IS_DEBUG=1
</pre>
</details>

<br>

## Локальный запуск api_walker
Сборка\
`cd api_walker/build && cmake .. && cmake --build .`

Запуск\
`cd api_walker/build && ./api_walker`

Запуск тестов\
**(TODO)**

<br>

# Codestyle

## C++

* Для названий классов, неймспейсов, енамов, методов и полей используется `PascalCase`, остальное - `camelCase`
* Все классы должны иметь префикс `T`, неймспейсы - `N`, енамы - `E`
* Приватные поля должны иметь суффкс `_`

```c++
namespace NServiceName {

enum EDirection {
    RIGHT,
    LEFT
};

class TServer {
public:
    int PublicField;

    void SomeMethod() {
        int localVariable;
    }

private:
    int PrivateField_;
};

} // namespace NServiceName
```

<br>

## Python
`PEP8` -_-
**(TODO)** добавить автоматический `black`

<br>

