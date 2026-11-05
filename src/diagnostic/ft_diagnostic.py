def top_vendors(sales: dict[str, int], n: int) -> list[tuple[(str, int)]]:
    return sorted(sales.items(), key=lambda x: x[1], reverse=True)[:n]
