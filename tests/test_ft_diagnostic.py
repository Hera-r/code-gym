import pytest

from diagnostic.ft_diagnostic import top_vendors


@pytest.mark.parametrize(
    "sales, n, expected",
    [
        # Top 3 with two vendors having the same revenue
        (
            {"Rasoa": 120, "Hery": 300, "Fidy": 120, "Tiana": 90},
            3,
            [("Hery", 300), ("Rasoa", 120), ("Fidy", 120)],
        ),
        # Top 1 vendor
        ({"Hery": 300, "Fidy": 120}, 1, [("Hery", 300)]),
        # Empty dictionary
        ({}, 3, []),
        # N greater than the number of vendors
        ({"Hery": 300, "Fidy": 120}, 5, [("Hery", 300), ("Fidy", 120)]),
        # N equals zero
        ({"Hery": 300, "Fidy": 120}, 0, []),
        # Single vendor
        ({"Hery": 300}, 1, [("Hery", 300)]),
        # All vendors
        (
            {"Rasoa": 120, "Hery": 300, "Fidy": 120},
            3,
            [("Hery", 300), ("Rasoa", 120), ("Fidy", 120)],
        ),
        # All vendors have the same revenue
        ({"Hery": 100, "Fidy": 100, "Rasoa": 100}, 2, [("Hery", 100), ("Fidy", 100)]),
    ],
)
def test_top_vendors(
    sales: dict[str, int], n: int, expected: list[tuple[str, int]]
) -> None:
    assert top_vendors(sales, n) == expected


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_top_vendors_negative_n(n: int) -> None:
    sales = {"Hery": 300, "Fidy": 120}

    with pytest.raises(ValueError, match="n must be greater than or equal to 0"):
        top_vendors(sales, n)
