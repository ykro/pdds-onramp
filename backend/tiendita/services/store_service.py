"""Layered business service with dependency injection and authorization rules."""

from __future__ import annotations

from typing import Any, Protocol

from tiendita.repositories.orders_repo import OrderSummary


class StoreRepository(Protocol):
    def list_products(self) -> list[dict[str, Any]]: ...
    def get_product_by_sku(self, sku: str) -> dict[str, Any] | None: ...
    def create_order(self, user_id: str, sku: str, quantity: int) -> OrderSummary: ...
    def list_orders_for_user(self, user_id: str) -> list[dict[str, Any]]: ...


class StoreService:
    """Coordinates business rules, authorization, and persistence without knowing HTTP or SQL."""

    def __init__(self, repo: StoreRepository) -> None:
        self._repo = repo

    def get_catalog(self) -> list[dict[str, Any]]:
        return self._repo.list_products()

    def get_product(self, sku: str) -> dict[str, Any]:
        # TODO (CA-4.2): consulta self._repo.get_product_by_sku(sku) y lanza KeyError si es None.
        raise NotImplementedError("TODO: implementa get_product en StoreService")

    def create_order(self, user_id: str, sku: str, quantity: int) -> OrderSummary:
        if quantity <= 0:
            raise ValueError("quantity must be greater than zero")
        return self._repo.create_order(user_id=user_id, sku=sku, quantity=quantity)

    def get_my_orders(self, user_id: str) -> list[dict[str, Any]]:
        """Authorization rule: return only orders belonging to user_id."""
        # BUG (CA-4.1): devuelve todos los pedidos sin verificar que pertenezcan a user_id.
        return self._repo.list_orders_for_user(user_id)
