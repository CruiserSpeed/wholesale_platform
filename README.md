# Структура проекта
```
whosale_platform
|-- backend
|    |-- admin_app       // бэкенд админки
|    |    |-- src
|    |    |    | run.py  // entrypoint
|    |    |-- tests
|    |    | Dockerfile
|    |    | build.sh     // сборка контейнера
|    |    | run.sh       // запуск контенера
|    |    | .env         // admin-env для запуска без контейнера
|    |-- admin_db        // контейнер с базой данных для админки
|    |    | Dockerfile 
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

Запуск тестов\
`cd whosale_platform && ./run.sh --test`\
or\
`cd whosale_platform && ./run.sh -t`
без стайлчекинга
`cd whosale_platform && ./run.sh -t -v`
or\
`cd whosale_platform && ./run.sh -t --vital`

**NB**: должны быть определены необходимые переменный окружения:
<details>
<summary>Шаблон для root-env</summary>
<pre>
ADMIN_APP_EXTERNAL_PORT=5000
ADMIN_APP_INNER_PORT=5000
ADMIN_APP_IS_DEBUG=1
ADMIN_DB_USER=postgres
ADMIN_DB_PASSWORD=???
ADMIN_DB_PORT=5432
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

**NB**: должны быть определены необходимые переменный окружения:
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
PEP8 -_-

<br>


Тестирование
