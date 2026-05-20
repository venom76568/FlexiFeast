import React, { useState } from 'react';

const ShoppingCart = React.memo(({ cart, setCart }) => {
  const [isCheckout, setIsCheckout] = useState(false);
  const [phone, setPhone] = useState('');
  const [otp, setOtp] = useState('');
  const [step, setStep] = useState(1); // 1: Cart, 2: Phone, 3: OTP, 4: Success
  const [splitData, setSplitData] = useState(null);

  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  const handleCheckoutInit = () => {
    if (cart.length === 0) return;
    setIsCheckout(true);
    setStep(2);
  };

  const handlePhoneSubmit = (e) => {
    e.preventDefault();
    // Simulate API call to split-payment calculator backend
    const dailyLimit = 200; // Mock daily limit
    const walletDeducted = Math.min(total, dailyLimit);
    const personalPaid = total - walletDeducted;
    setSplitData({ walletDeducted, personalPaid });
    setStep(3); // Proceed to OTP
  };

  const handleOtpSubmit = (e) => {
    e.preventDefault();
    // Simulate OTP verification success
    setStep(4);
    setTimeout(() => {
      setCart([]);
      setStep(1);
      setIsCheckout(false);
      setPhone('');
      setOtp('');
    }, 2000);
  };

  return (
    <div className="h-full border rounded-lg bg-white shadow-sm flex flex-col p-4">
      <h2 className="text-xl font-bold mb-4 border-b pb-2">Current Order</h2>
      
      {step === 1 && (
        <>
          <div className="flex-1 overflow-auto">
            {cart.length === 0 ? (
              <p className="text-muted-foreground text-center mt-10">Cart is empty</p>
            ) : (
              <ul className="space-y-3">
                {cart.map((item) => (
                  <li key={item.id} className="flex justify-between items-center border-b pb-2">
                    <div>
                      <p className="font-semibold">{item.name}</p>
                      <p className="text-sm text-muted-foreground">₹{item.price} x {item.quantity}</p>
                    </div>
                    <p className="font-bold">₹{item.price * item.quantity}</p>
                  </li>
                ))}
              </ul>
            )}
          </div>
          <div className="border-t pt-4 mt-4">
            <div className="flex justify-between items-center text-lg font-bold mb-4">
              <span>Total:</span>
              <span>₹{total}</span>
            </div>
            <button 
              onClick={handleCheckoutInit}
              disabled={cart.length === 0}
              className="w-full bg-primary text-primary-foreground py-3 rounded-lg font-semibold disabled:opacity-50"
            >
              Checkout via Wallet
            </button>
          </div>
        </>
      )}

      {step === 2 && (
        <div className="flex-1 flex flex-col justify-center">
          <h3 className="text-lg font-semibold mb-2">Employee Verification</h3>
          <form onSubmit={handlePhoneSubmit}>
            <input 
              type="tel" 
              placeholder="Enter phone number" 
              className="w-full border p-2 rounded mb-4"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              required
            />
            <button type="submit" className="w-full bg-primary text-primary-foreground py-2 rounded">
              Verify & Calculate
            </button>
          </form>
          <button onClick={() => setStep(1)} className="mt-4 text-sm text-gray-500 hover:underline">Cancel</button>
        </div>
      )}

      {step === 3 && splitData && (
        <div className="flex-1 flex flex-col justify-center">
          <h3 className="text-lg font-semibold mb-2">Payment Split</h3>
          <div className="bg-gray-100 p-4 rounded-lg mb-4 space-y-2">
            <div className="flex justify-between">
              <span>Wallet Pays:</span>
              <span className="font-bold text-green-600">₹{splitData.walletDeducted}</span>
            </div>
            <div className="flex justify-between border-t pt-2 mt-2">
              <span>You Owe Cash/UPI:</span>
              <span className="font-bold text-red-600">₹{splitData.personalPaid}</span>
            </div>
          </div>
          <form onSubmit={handleOtpSubmit}>
            <input 
              type="text" 
              placeholder="Enter 6-digit OTP" 
              className="w-full border p-2 rounded mb-4"
              value={otp}
              onChange={(e) => setOtp(e.target.value)}
              required
            />
            <button type="submit" className="w-full bg-primary text-primary-foreground py-2 rounded">
              Confirm Payment
            </button>
          </form>
          <button onClick={() => setStep(2)} className="mt-4 text-sm text-gray-500 hover:underline">Back</button>
        </div>
      )}

      {step === 4 && (
        <div className="flex-1 flex flex-col justify-center items-center text-center">
          <div className="text-green-500 text-5xl mb-4">✓</div>
          <h3 className="text-xl font-bold">Transaction Successful!</h3>
          <p className="text-muted-foreground mt-2">Redirecting to menu...</p>
        </div>
      )}
    </div>
  );
});

export default ShoppingCart;
