## Summarize Backend

[![GitHub Stars](https://img.shields.io/github/stars/FOSWLY/summarize-backend?logo=github&style=for-the-badge)](https://github.com/FOSWLY/summarize-backend/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/FOSWLY/summarize-backend?style=for-the-badge)](https://github.com/FOSWLY/summarize-backend/issues)
[![Current Version](https://img.shields.io/github/v/release/FOSWLY/summarize-backend?style=for-the-badge)](https://github.com/FOSWLY/summarize-backend)
[![GitHub License](https://img.shields.io/github/license/FOSWLY/summarize-backend?style=for-the-badge)](https://github.com/FOSWLY/summarize-backend/blob/master/LICENSE)

**Summarize Backend** - cервер, предоставляющий унифицированные конечные точки для API суммаризации из библиотеки [@toil/neurojs](https://github.com/FOSWLY/neurojs).

## 📝 Функционал

- Суммаризация статей
- Суммаризация текста
- Суммаризация видео
- Получение ссылки на суммаризацию статей (необходимо указать токен к оф. апи)
- Получение суммаризации по токену (`https://300.ya.ru/TOKEN`)

## 📦 Деплой

### С Docker

1. Установите Docker
2. Соберите образ

```bash
docker build -t "summarize-backend" .
```

3. Запустите контейнер

```bash
docker run -p 3312:3312 summarize-backend
```

### Вручную

1. Установите [Bun](https://bun.sh/)
2. Клонируйте репозиторий:

```bash
git clone https://github.com/FOSWLY/summarize-backend
```

3. Установите зависимости

```bash
bun install
```

3.1. (опционально) Переименуйте `.example.env` в `.env` и заполните необходимые поля

4. Запустите сервер

```bash
bun start
```

Если вы хотите использовать PM2:

1. Установите зависимости:

```bash
bun install -g pm2-beta && pm2 install pm2-logrotate
```

2. Запустите сервер

```bash
pm2 start ecosystem.config.json
```

## 📖 Кому это будет полезно

1. Если вы хотите использовать логику из [neurojs](https://github.com/FOSWLY/neurojs) с помощью другого языка программирования, но не хотите переносить весь функционал в ваш код
2. Если вы не хотите тянуть зависимости от neurojs
3. Если вы хотите иметь простой унифицированный апи
