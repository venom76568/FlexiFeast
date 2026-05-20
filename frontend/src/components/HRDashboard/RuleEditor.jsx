import React, { useState } from 'react';

const RuleEditor = () => {
  const [ruleText, setRuleText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitting rule:", ruleText);
    setRuleText('');
  };

  return (
    <div className="p-4 bg-white rounded shadow">
      <h3 className="text-lg font-semibold mb-2">HR Rule Editor</h3>
      <form onSubmit={handleSubmit}>
        <textarea 
          className="w-full border p-2 rounded mb-2"
          rows="3"
          placeholder="e.g. Limit daily spend to 250"
          value={ruleText}
          onChange={(e) => setRuleText(e.target.value)}
        />
        <button type="submit" className="px-4 py-2 bg-green-600 text-white rounded">Save Rule</button>
      </form>
    </div>
  );
};

export default RuleEditor;
