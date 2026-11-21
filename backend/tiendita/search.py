"""SKU search strategies for Big-O comparison (linear, binary, hash table)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductRecord:
    sku: str
    name: str
    category: str
    price_cents: int
    stock: int


@dataclass
class SearchResult:
    product: ProductRecord | None
    operations: int


def linear_search(products: list[ProductRecord], target_sku: str) -> SearchResult:
    """Scan products one by one and count comparisons."""
    raise NotImplementedError("TODO: implementa linear_search en search.py")


def binary_search(sorted_products: list[ProductRecord], target_sku: str) -> SearchResult:
    """Binary search over products sorted ascending by sku, counting comparisons."""
    raise NotImplementedError("TODO: implementa binary_search en search.py")


def build_sku_index(products: list[ProductRecord]) -> dict[str, ProductRecord]:
    """Build a dictionary keyed by SKU for O(1) lookup."""
    raise NotImplementedError("TODO: implementa build_sku_index en search.py")


def dict_search(index: dict[str, ProductRecord], target_sku: str) -> SearchResult:
    """Lookup a SKU in the dictionary index in O(1)."""
    raise NotImplementedError("TODO: implementa dict_search en search.py")
