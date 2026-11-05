def greet(name: str) -> str:
    if name == "" or " " in name:
        raise ValueError("The input string cannot be empty or contain any spaces")
    return f"Salama, {name}"
