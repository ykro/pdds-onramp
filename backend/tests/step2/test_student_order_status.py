"""Student tests for order_status.py (CA-2.3).

Your tests must pass against tiendita.order_status and fail with AssertionError
against three versions with planted bugs.
"""

from __future__ import annotations

import pytest

from tiendita import order_status as os_mod


def test_example_pending_to_paid_is_allowed() -> None:
    """Example test that already passes once can_transition is implemented."""
    assert os_mod.can_transition("pending", "paid") is True


# TODO (CA-2.3): escribe tests que detecten:
# 1. Cancelar un pedido que ya fue enviado o entregado.
# 2. Saltar de pending directo a shipped o delivered.
# 3. Salir de un estado terminal (delivered o cancelled).
