import React, { useState } from 'react';

export default function LedgerTable() {
  const [transactions, setTransactions] = useState([
    { id: 'TRX-001', employee: 'John Doe', cartTotal: 250, walletDeducted: 200, personalPaid: 50, date: '2023-10-05 12:30 PM' },
    { id: 'TRX-002', employee: 'Jane Smith', cartTotal: 150, walletDeducted: 150, personalPaid: 0, date: '2023-10-05 01:15 PM' },
    { id: 'TRX-003', employee: 'Alex Jones', cartTotal: 300, walletDeducted: 250, personalPaid: 50, date: '2023-10-05 01:45 PM' },
  ]);

  return (
    <div className="bg-white p-6 rounded-lg shadow-sm border">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">HR Unified Ledger</h2>
        <button className="bg-secondary text-secondary-foreground px-4 py-2 rounded">Export CSV</button>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-50 border-b text-left">
              <th className="p-3 font-semibold">Transaction ID</th>
              <th className="p-3 font-semibold">Date</th>
              <th className="p-3 font-semibold">Employee</th>
              <th className="p-3 font-semibold">Cart Total</th>
              <th className="p-3 font-semibold text-green-700">Wallet Deducted</th>
              <th className="p-3 font-semibold text-red-700">Personal Out-of-Pocket</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((trx) => (
              <tr key={trx.id} className="border-b hover:bg-gray-50">
                <td className="p-3 text-sm text-gray-500">{trx.id}</td>
                <td className="p-3 text-sm">{trx.date}</td>
                <td className="p-3 font-medium">{trx.employee}</td>
                <td className="p-3">₹{trx.cartTotal}</td>
                <td className="p-3 text-green-600 font-semibold">₹{trx.walletDeducted}</td>
                <td className="p-3 text-red-600 font-semibold">₹{trx.personalPaid}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
