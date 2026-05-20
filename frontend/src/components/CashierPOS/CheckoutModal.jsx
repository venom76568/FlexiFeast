import React from 'react';

const CheckoutModal = ({ isOpen, onClose, cartItems, total }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
      <div className="bg-white p-6 rounded-lg w-96">
        <h2 className="text-xl font-bold mb-4">Checkout</h2>
        <div className="mb-4">
          <p>Total Items: {cartItems.length}</p>
          <p className="font-bold">Total Amount: ₹{total}</p>
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 border rounded">Cancel</button>
          <button className="px-4 py-2 bg-blue-600 text-white rounded">Confirm Payment</button>
        </div>
      </div>
    </div>
  );
};

export default CheckoutModal;
