# 🧠 Neural Style Transfer WebApp

## 📌 Описание

Это веб-приложение реализует метод переноса художественного стиля (Neural Style Transfer), позволяющий наложить визуальный стиль одного изображения на содержимое другого. Пользователь загружает изображение-контент и изображение-стиль, после чего модель генерирует результат, сочетающий их характеристики.

Проект состоит из backend-сервиса на Python с использованием FastAPI и модели на PyTorch, а также frontend-приложения на React для удобного взаимодействия с пользователем.

## 📊 Структура проекта

```
.
├── style-transfer-backend
│   ├── presentations
│   │   ├── fastapi_app.py
│   │   └── requirements.txt
│   ├── services
│   │   ├── st_service.py
│   │   └── requirements.txt
│   ├── utils
│   │   ├── image_preparation.py
│   │   ├── style_transfer.py
│   │   └── requirements.txt
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
│
├── style-transfer-frontend
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   ├── package-lock.json
│   ├── requirements.txt
│   └── .gitignore
│
├── README.md
└── .gitignore
```

## ⚙️ Установка и запуск

### Backend

1. Перейдите в папку `style-transfer-backend`:

```bash
cd style-transfer-backend
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите приложение:

```bash
python main.py
```

### Frontend

1. Перейдите в папку `style-transfer-frontend`:

```bash
cd style-transfer-frontend
```

2. Установите зависимости:

```bash
npm install
```

3. Запустите приложение:

```bash
npm start
```

## 📌 requirements.txt

**Общий для backend:**

```
fastapi
uvicorn
torch
torchvision
Pillow
python-multipart
```

**presentations/requirements.txt:**

```
fastapi
```

**services/requirements.txt:**

```
torch
```

**utils/requirements.txt:**

```
torchvision
Pillow
```

**style-transfer-frontend/requirements.txt (для справки):**

```
react
react-dom
react-scripts
```

Используется Node.js и npm — основные зависимости описаны в `package.json`.

## 🖼️ Интерфейс

Здесь можно разместить скриншот работы веб-приложения.

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробнее — в файле LICENSE.
