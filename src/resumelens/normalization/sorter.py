def sort_for_profile(normalized: list[str], order: list[str]) -> list[str]:
    rank = {token: i for i, token in enumerate(order)}
    return sorted(normalized, key=lambda token: rank.get(token, len(order) + 100))
