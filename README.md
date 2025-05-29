## Neural Style Transfer

Простой и настраиваемый проект для переноса художественного стиля с одного изображения на другое, написанный на PyTorch.

---

## Установка

Создай и активируй виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows
```

## Для запуска на CPU:

```bash
pip install -r requirements.txt
```

## Для запуска на GPU (CUDA 12.4):

```bash
pip install -r requirements-gpu.txt
```

---

## Запуск

```bash
python main.py path/to/content.jpg path/to/style.jpg \
    --steps 300 \
    --style-weight 1e6 \
    --content-weight 1 \
    --imsize 512
```

> По умолчанию используется `VGG19`.

---

## Структура проекта

```
├── image_preparation.py   # Загрузка, преобразование и сохранение изображений
├── style_transfer.py      # Основная логика переноса стиля
├── main.py                # Точка входа (CLI)
├── requirements.txt       # Зависимости для CPU
├── requirements-gpu.txt   # Зависимости для GPU (CUDA 12.4)
└── README.md
```

---

## Параметры

| Аргумент           | Описание                                    | По умолчанию |
| ------------------ | ------------------------------------------- | ------------ |
| `--steps`          | Количество итераций оптимизации             | `500`        |
| `--style-weight`   | Вес функции потерь стиля                    | `1e5`        |
| `--content-weight` | Вес функции потерь содержимого              | `1`          |
| `--imsize`         | Размер изображения (обрезается до квадрата) | `512`        |
| `--input`          | (Опционально) начальное изображение         | `input.jpg`  |

---
