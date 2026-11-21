-- Migration 001: core Tiendita tables with business rules as constraints

-- TODO (CA-3.1): completa los constraints (UNIQUE en sku, CHECK >= 0, llaves foráneas y estados válidos)
-- Columnas esperadas por db/load.py:
--   products(id SERIAL PRIMARY KEY, sku TEXT, name TEXT, category TEXT, price_cents INTEGER, stock INTEGER)
--   orders(id SERIAL PRIMARY KEY, user_id TEXT, status TEXT, total_cents INTEGER, created_at TIMESTAMPTZ)
--   order_items(id SERIAL PRIMARY KEY, order_id INTEGER, product_id INTEGER, quantity INTEGER, unit_price_cents INTEGER)
SELECT 1 WHERE FALSE;
