def basic_capitalize(data: str) -> str:
    return data.capitalize()


def safe_capitalize(data: str) -> str:
    if isinstance(data, str):
        return basic_capitalize(data)
    return data
