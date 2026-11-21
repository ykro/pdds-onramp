import { useCallback, useMemo, useState } from 'react';
import type { Product } from '../lib/api';

export interface CartItem {
  product: Product;
  quantity: number;
}

export interface UseCartResult {
  items: CartItem[];
  itemCount: number;
  totalCents: number;
  formattedTotal: string;
  addItem: (product: Product) => void;
  updateQuantity: (productId: Product['id'], quantity: number) => void;
  removeItem: (productId: Product['id']) => void;
  clearCart: () => void;
}

export function formatQuetzales(cents: number): string {
  return `Q ${(cents / 100).toFixed(2)}`;
}

export function useCart(initialItems: CartItem[] = []): UseCartResult {
  const [items, setItems] = useState<CartItem[]>(initialItems);

  const addItem = useCallback((product: Product) => {
    throw new Error("TODO: implementa este método en useCart.ts");
  }, []);

  const updateQuantity = useCallback((productId: Product['id'], quantity: number) => {
    setItems((prev) => {
      if (quantity <= 0) {
        return prev.filter((item) => item.product.id !== productId);
      }
      return prev.map((item) => {
        if (item.product.id !== productId) {
          return item;
        }
        const bounded = Math.min(quantity, item.product.stock);
        return { ...item, quantity: bounded };
      });
    });
  }, []);

  const removeItem = useCallback((productId: Product['id']) => {
    throw new Error("TODO: implementa este método en useCart.ts");
  }, []);

  const clearCart = useCallback(() => {
    setItems([]);
  }, []);

  const itemCount = useMemo(
    () => items.reduce((sum, item) => sum + item.quantity, 0),
    [items],
  );

  const totalCents = useMemo<number>(() => {
    throw new Error("TODO: implementa este método en useCart.ts");
  }, [items]);

  const formattedTotal = useMemo(() => formatQuetzales(totalCents), [totalCents]);

  return {
    items,
    itemCount,
    totalCents,
    formattedTotal,
    addItem,
    updateQuantity,
    removeItem,
    clearCart,
  };
}
