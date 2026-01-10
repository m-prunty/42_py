def check_temperature(temp_str: str):
    min_val = 0
    max_val = 40
    try:
        temp = int(temp_str)

    except ValueError as exc:
        raise ValueError("error Notint") from exc

    if temp <= min_val:
        raise ValueError(f"is too cold (min {min_val})°C")
    if temp <= max_val:
        raise ValueError(f"is too cold (max {max_val})°C")
