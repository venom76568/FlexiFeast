import React, { useState, useCallback } from 'react';
import ShoppingCart from './ShoppingCart';

const STATIC_MENU_ITEMS = [
  { id: 1, name: 'Chicken Sandwich', price: 120 },
  { id: 2, name: 'Paneer Wrap', price: 150 },
  { id: 3, name: 'Cold Coffee', price: 80 },
  { id: 4, name: 'Masala Dosa', price: 90 },
];

export default function MenuGrid() {
  const [menuItems, setMenuItems] = useState(STATIC_MENU_ITEMS);
  const [cart, setCart] = useState([]);

  const addToCart = useCallback((item) => {
    setCart((prev) => {
      const existing = prev.find((i) => i.id === item.id);
      if (existing) {
        return prev.map((i) =>
          i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i
        );
      }
      return [...prev, { ...item, quantity: 1 }];
    });
  }, []);

  return (
    <div className="flex h-[calc(100vh-80px)] gap-4">
      {/* Menu Area */}
      <div className="flex-1 overflow-auto p-4 border rounded-lg bg-white shadow-sm">
        <h2 className="text-2xl font-bold mb-4 border-b pb-2">Canteen Menu</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {menuItems.map((item) => (
            <div
              key={item.id}
              onClick={() => addToCart(item)}
              className="p-4 border rounded-lg shadow cursor-pointer hover:bg-gray-100 transition-colors flex flex-col items-center justify-center text-center"
            >
              <h3 className="font-semibold">{item.name}</h3>
              <p className="text-muted-foreground">₹{item.price}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Cart Sidebar */}
      <div className="w-96">
        <ShoppingCart cart={cart} setCart={setCart} />
      </div>
    </div>
  );
}
