"""FIFO order fulfillment queue using collections.deque (Step 2 extended)."""

from __future__ import annotations

from collections import deque


class FulfillmentQueue:
    """Dispatches paid orders in First-In, First-Out order."""

    def __init__(self) -> None:
        self._queue: deque[int] = deque()

    def enqueue(self, order_id: int) -> None:
        raise NotImplementedError("TODO: implementa enqueue en fulfillment.py")

    def dequeue(self) -> int | None:
        raise NotImplementedError("TODO: implementa dequeue en fulfillment.py")

    def pending_count(self) -> int:
        raise NotImplementedError("TODO: implementa pending_count en fulfillment.py")
