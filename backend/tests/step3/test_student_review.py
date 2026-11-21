"""Student review tests for find_orders_by_sku (CA-3.4).

Your tests must pass against tiendita.repositories.orders_repo.find_orders_by_sku
and fail with AssertionError against steps/03-sql/buggy_snapshot.py.
"""

from __future__ import annotations

from typing import Any

import psycopg

from tiendita.repositories import orders_repo

find_orders_fn = orders_repo.find_orders_by_sku


# TODO (CA-3.4): escribe tests que fallen contra buggy_snapshot.py y pasen con tu corrección:
# 1. Verificar que los pedidos con status='cancelled' no aparezcan.
# 2. Verificar que un SKU con "' OR '1'='1" no devuelva filas.
def test_placeholder(seeded_db: psycopg.Connection[Any]) -> None:
    assert seeded_db is not None
