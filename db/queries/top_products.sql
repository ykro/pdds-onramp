-- Top 5 products by total units sold (excluding cancelled orders)
-- Columns: sku, name, units_sold
-- Order: ORDER BY units_sold DESC, p.sku ASC (desempate por SKU ascendente)
-- TODO (CA-3.2): une order_items, products y orders excluyendo status = 'cancelled'.

SELECT '' AS sku, '' AS name, 0 AS units_sold WHERE FALSE;
