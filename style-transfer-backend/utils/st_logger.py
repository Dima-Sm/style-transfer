import logging
import sys

def setup_logger(name: str, log_file: str = "style_transfer.log") -> logging.Logger:
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Уровень логирования

    # Формат сообщений
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Обработчик для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Обработчик для файла
    file_handler = logging.FileHandler(log_file, mode="a")  # 'a' - дозапись
    file_handler.setFormatter(formatter)

    # Удаляем старые обработчики (если есть)
    if logger.handlers:
        logger.handlers.clear()

    # Добавляем новые обработчики
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger