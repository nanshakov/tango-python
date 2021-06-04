# Задача
Взять список уникальных идентификаторов пользователей (100 шт хватит);

Написать на Flask 2 сервиса

a) сервис (GENERATOR) запускается каждую секунду, генерит рандомное число для каждого ID юзера и записывает информацию в Редис, например: {"user123456": SOMERANDOM_INT};

b) Второй сервис (INVOKER):

    i) Имеет метод getinfo, который по конкретному юзеру выдает из Редиса реверсивное значение SOMERANDOM_INT;
    
    ii) Необходим локальный кэшинг этого значение на 5 секунд. Если по данному юзеру нет данных в локальном кэшинге - брать кэш из редиса. Кэш хранится в отдельном ключе;
    Все сервисы задеплоить на Cloud Run;
    Развернуть на Compute Engine / Memorystore базу данных Redis и сделать коннект между API и Redis;
    В каждом API сделать один метод GET “/ping”, который выдаёт ответ {“pong”}

# Архитектура
## Локальный synchronized cache

# Запуск
## howto
### Билд
```gcloud builds submit --tag gcr.io/PROJECT-ID/Invoker```
```gcloud builds submit --tag gcr.io/PROJECT-ID/Generator```

```gcloud builds submit --tag gcr.io/magnetic-guild-315806/invoker```
```gcloud builds submit --tag gcr.io/magnetic-guild-315806/generator```
## Примеры команд