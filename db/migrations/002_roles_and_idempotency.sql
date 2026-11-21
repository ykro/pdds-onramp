-- Migration 002: admin roles and idempotency keys (applied on top of live 001 data)

-- TODO (CA-4.1): crea las tablas sin modificar 001_init.sql:
--   admins(user_id TEXT PRIMARY KEY, granted_at TIMESTAMPTZ DEFAULT NOW())
--   idempotency_keys(key TEXT PRIMARY KEY, user_id TEXT, order_id INTEGER REFERENCES orders(id), created_at TIMESTAMPTZ DEFAULT NOW())
SELECT 1 WHERE FALSE;
