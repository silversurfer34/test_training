def basic_capitalize(data: str) -> str:
    return data.capitalize()


def custom_capitalize(data: str) -> str:
    if isinstance(data, str):
        return data.capitalize()
    return data
