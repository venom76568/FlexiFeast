import React, { createContext, useContext, useState } from 'react';

const WalletContext = createContext();

export const WalletProvider = ({ children }) => {
  const [balance, setBalance] = useState(5000);
  const [dailyLimit, setDailyLimit] = useState(250);

  return (
    <WalletContext.Provider value={{ balance, setBalance, dailyLimit, setDailyLimit }}>
      {children}
    </WalletContext.Provider>
  );
};

export const useWallet = () => useContext(WalletContext);
