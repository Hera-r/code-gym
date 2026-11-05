def top_vendors(sales: dict[str, int], n: int) -> list[tuple[(str, int)]]:
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")
    return sorted(sales.items(), key=lambda x: x[1], reverse=True)[:n]
