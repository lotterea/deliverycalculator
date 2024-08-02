def calculate_delivery_cost(
    distance: float | int, size: str, fragile: bool, workload: str
) -> int:
    """
    Calculate the delivery cost based on various parameters such as
    distance, size, fragility, and workload.

    :param distance: The distance of the delivery in kilometers. Must be a positive number.
    :param size: The size of the item to be delivered. Must be either 'small' or 'large'.
    :param fragile: Indicates if the item is fragile. True if fragile, False otherwise.
    :param workload: The current workload. Must be one of 'very high', 'high', 'increased', or 'normal'.

    :return: The total delivery cost in integer value. The minimum delivery cost is 400.

    :raises TypeError: If distance is not an int or float, or if fragile is not a boolean.
    :raises ValueError: If distance is less than or equal to 0, or if an invalid size or workload is provided,
                        or if fragile items are attempted to be delivered for distances greater than 30 km.
    """

    # Базовая стоимость
    base_cost = 0

    # Проверка типа данных аргумента distance
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be int or float")

    # Проверка типа данных аргумента fragile
    if not isinstance(fragile, bool):
        raise TypeError("fragile parameter must be a boolean")

    # Надбавка к стоимости на основе расстояния
    if distance <= 0:
        raise ValueError("Distance must be more than 0")
    elif 0 < distance <= 2:
        base_cost = 50
    elif distance <= 10:
        base_cost = 100
    elif distance <= 30:
        base_cost = 200
    elif distance > 30:
        if fragile:
            raise ValueError(
                "Fragile items cannot be delivered on a distance greater than 30 km"
            )
        base_cost = 300

    # Надбавка для хрупких предметов
    fragile_cost = 300 if fragile else 0

    # Определение множителя загрузки
    workload_multipliers = {
        "very high": 1.6,
        "high": 1.4,
        "increased": 1.2,
        "normal": 1,
    }

    # Определение надбавки на основе размера
    size_costs = {"large": 200, "small": 100}

    # Проверка валидности аргумента workload
    if workload not in workload_multipliers:
        raise ValueError("Invalid workload")
    # Выбор стоимости на основе коэффициента загрузки
    workload_multiplier = workload_multipliers[workload]

    # Проверка валидности аргумента size
    if size not in size_costs:
        raise ValueError("Invalid size")
    # Выбор стоимости на основе размера груза
    size_cost = size_costs[size]

    # Общий расчет стоимости
    total_cost = (base_cost + size_cost + fragile_cost) * workload_multiplier

    # Если стоимоисть меньше 400, возвращаем 400, иначе - полученную стоимость до рубля
    return max(int(total_cost), 400)
