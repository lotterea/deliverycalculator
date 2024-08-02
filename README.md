# Калькулятор стоимости доставки

Этот проект - тестовое задание. Это калькулятор стоимости доставки, который учитывает расстояние, размер груза, хрупкость и загруженность службы доставки.

## Установка

### Шаг 1: Клонирование репозитория

Клонируйте репозиторий на вашу машину:

```bash
git clone https://github.com/lotterea/deliverycalculator
```

### Шаг 2: Создание и активация виртуального окружения

Создайте виртуальное окружение и активируйте его:

```bash
python3.12 -m venv venv
source venv/bin/activate  # Windows: `venv\Scripts\activate`
```

### Шаг 3: Установка зависимостей

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Использование

### Основная функция

Основная функция `calculate_delivery_cost` находится в файле `delivery_calculator.py`. Она принимает четыре параметра: `distance` (расстояние до пункта назначения), `size` (размер груза), `fragile` (хрупкость груза) и `workload` (загруженность службы доставки). Функция возвращает стоимость доставки с учетом всех параметров.

### Пример использования

```python
from delivery_calculator.delivery_calculator import calculate_delivery_cost

cost = calculate_delivery_cost(15, 'large', True, 'high')
print(f"Стоимость доставки: {cost} рублей")
```

### Запуск тестов

Для запуска тестов выполните следующую команду:

```bash
pytest tests
```

### Подсчет покрытия тестов

Для подсчета покрытия тестов (test coverage) можно использовать инструмент `pytest-cov`. Следуйте этим шагам, чтобы установить и использовать его.

Установите `pytest-cov` с помощью pip:

```bash
pip install pytest-cov
```

Запустите тесты с включенным подсчетом покрытия и генерацией html-отчета:


```bash
pytest --cov=. --cov-report=html
```

## Контакты

Автор: Светлана Лебедева  
Email: svetlana.vl.koroleva@gmail.com  
GitHub: [lotterea](https://github.com/lotterea)


