# PB14 Курсовий Проект Група 1
1. Alina Prokhorenko
2. Dmitryi Obukhov
3. Olena Babych
5. Tetiana Golovchenko
6. Виталий Сердитов

# Docker
Встановіть Docker. Перйдіть за посиланням та виконайте інструкції:
- для Mac [Mac Install](https://docs.docker.com/desktop/install/mac-install/ )
- для Ubuntu [Ubuntu Install](https://docs.docker.com/desktop/install/ubuntu/)

Встановіть Docker в режим для запуску без використання sudo, as a non-root user: 
[Instruction](https://docs.docker.com/engine/install/linux-postinstall/)

# .env
В кореневій дерикторії проекту (де зберігається файл .env.sample) створіть файл .env та
 перенесіть назви констант з .env.sample до .env і задайте свої знанчення

# Запуск контейнера
1. В терміналі виконайте команду: make bootstrap для створення і налаштування контейнера
2. Виконайте команду: make shell  для входу в контейнер і роботи в ньому  
Після цого перейдіть за посиланням і виконайте інструкції: [Instruction](https://dev.to/alvarocavalcanti/setting-up-a-python-remote-interpreter-using-docker-1i24)

# Видалення або пестворення контейнера
1. Для видалення контейнерів і всіх даних з бази виконайте команду: make down  
Після виконання цієї комнди для створення нового контейнера слід виконати кроки з запуску контейнера.

# Запуск бота
1. Для запуску і постіної роботи бота виконайте команду make up

# Для створення нової міграції
Запускати після змін в моделі даних, всередині docker контейнера
```bash
alembic revision --autogenerate --rev-id "<Number>_<Name>"
``` 
Автогенерація може не враховувати всих особливостей,
тому потрібно перевіряти файл міграції і вносити зміни, за необхідності, вручну