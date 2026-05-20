# FlexiFeast Project Setup Plan

## Overview
FlexiFeast is a unified corporate food wallet bridging WFH Swiggy delivery and onsite office canteens. It features an automated AI rule engine for HR compliance and a cashier-facing POS system.

## Project Type
WEB and BACKEND (Full-stack web application with a Python FastAPI backend and a React/Tailwind frontend)

## Success Criteria
- POS Cashier interface lists items, processes carts, and handles split payment logic correctly.
- SMS OTP verification triggers and validates securely (with simulated sandbox backup).
- Slack/Teams chatbot searches menu items and handles Swiggy deep-linking for split out-of-pocket payments.
- HR Dashboard parses English spending rules via AI, saves compiled filters, and showcases a real-time ledger breakdown.
- System passes all linting, building, and performance audit steps.

## Tech Stack
- Frontend: React (Vite-powered), Tailwind CSS
- Backend: FastAPI (Python 3.10+), SQLAlchemy ORM, Uvicorn
- Database: PostgreSQL (or local SQLite for dev environments)
- AI Engine: OpenAI/Anthropic SDKs (with mocked developer fallback)
- Integrations: Twilio/Fast2SMS APIs, Slack Bot framework

## File Structure

```text
flexifeast/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── menu.py
│   │   │   │   ├── wallet.py
│   │   │   │   ├── hr_rules.py
│   │   │   │   └── transactions.py
│   │   │   └── api.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── ai_engine.py
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   └── models.py
│   │   ├── schemas/
│   │   │   ├── menu.py
│   │   │   ├── wallet.py
│   │   │   ├── hr_rules.py
│   │   │   └── transactions.py
│   │   ├── services/
│   │   │   ├── swiggy_mcp.py
│   │   │   ├── sms_service.py
│   │   │   └── slack_bot.py
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CashierPOS/
│   │   │   │   ├── MenuGrid.jsx
│   │   │   │   ├── ShoppingCart.jsx
│   │   │   │   └── CheckoutModal.jsx
│   │   │   ├── HRDashboard/
│   │   │   │   ├── LedgerTable.jsx
│   │   │   │   ├── RuleEditor.jsx
│   │   │   │   └── EmployeeManager.jsx
│   │   │   └── Shared/
│   │   ├── hooks/
│   │   ├── context/
│   │   │   └── WalletContext.jsx
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── docs/
│   └── PLAN-flexifeast-setup.md
└── prd.md
```

## Task Breakdown

### Phase 1: Database Setup and Core Schema (P0 Foundation)

- Task 1.1: Initialize PostgreSQL database connections and SQLAlchemy base engine.
  - Agent: database-architect
  - Skill: database-design
  - INPUT: Database credentials and model requirements.
  - OUTPUT: backend/app/db/session.py containing database session loaders.
  - VERIFY: Run connection checks to ensure session establishes successfully.

- Task 1.2: Create the Employee and Wallet models with allowance columns.
  - Agent: database-architect
  - Skill: database-design
  - INPUT: Employee schema specs (id, name, phone, daily_limit, monthly_balance, is_active).
  - OUTPUT: SQLAlchemy Employee model in backend/app/db/models.py.
  - VERIFY: Query the table metadata to verify schema fields match specifications.

- Task 1.3: Create Canteen Menu and Transactions tables supporting split-pay records.
  - Agent: database-architect
  - Skill: database-design
  - INPUT: Menu item fields (id, name, price, is_active) and transaction fields (id, employee_id, total_cart_amount, wallet_deducted_amount, personal_paid_amount, items_list, created_at).
  - OUTPUT: Menu and Transaction models in backend/app/db/models.py.
  - VERIFY: Verify constraints and table schemas using validation tools.

### Phase 2: FastAPI Core REST Services (P1 Core API)

- Task 2.1: Establish FastAPI basic scaffolding with CORS config and router routing.
  - Agent: backend-specialist
  - Skill: api-patterns
  - INPUT: Backend setup configs.
  - OUTPUT: backend/app/main.py and backend/app/api/api.py.
  - VERIFY: Run the server and check the GET /docs OpenAPI playground page.

- Task 2.2: Build POS Canteen Menu API endpoints for canteens to list and save foods.
  - Agent: backend-specialist
  - Skill: api-patterns
  - INPUT: Models for Menu.
  - OUTPUT: REST routes GET/POST /api/pos/menu in backend/app/api/endpoints/menu.py.
  - VERIFY: Send HTTP requests to POS endpoints and confirm items write/read successfully.

- Task 2.3: Build Split-Payment Calculator backend logic.
  - Agent: backend-specialist
  - Skill: api-patterns
  - INPUT: Employee wallet balance and total cart value.
  - OUTPUT: Calculation utility returning wallet deduction and personal balance due.
  - VERIFY: Unit test calculation outputs with total cart values exceeding or matching balances.

- Task 2.4: Implement Twilio/Fast2SMS SMS OTP microservice with developer console logging backup.
  - Agent: backend-specialist
  - Skill: api-patterns
  - INPUT: Developer sandbox options and Twilio API keys.
  - OUTPUT: SMS OTP service in backend/app/services/sms_service.py.
  - VERIFY: Confirm SMS triggers correctly (or prints safely to terminal output when credentials are mock).

### Phase 3: Canteen POS Frontend (P2 Web Interface)

- Task 3.1: Initialize React (Vite) project with Tailwind CSS configuration.
  - Agent: frontend-specialist
  - Skill: frontend-design
  - INPUT: Clean React directory.
  - OUTPUT: frontend/ package.json, tailwind.config.js, and App.jsx initialization.
  - VERIFY: Run npm run dev and confirm blank page loads without style errors.

- Task 3.2: Design Canteen Menu Manager settings dashboard interface.
  - Agent: frontend-specialist
  - Skill: frontend-design
  - INPUT: Menu API endpoints.
  - OUTPUT: Settings management screen in frontend/src/components/CashierPOS/MenuGrid.jsx.
  - VERIFY: Insert food test card and observe successful list rendering.

- Task 3.3: Build Canteen Checkout side-panel Cart with Interactive Cards.
  - Agent: frontend-specialist
  - Skill: frontend-design
  - INPUT: State management for shopping cart selections.
  - OUTPUT: Sidebar cart component in frontend/src/components/CashierPOS/ShoppingCart.jsx.
  - VERIFY: Click multiple items to increment cart totals and counts perfectly.

- Task 3.4: Build interactive checkout modal with split payment calculations and OTP.
  - Agent: frontend-specialist
  - Skill: frontend-design
  - INPUT: POS API.
  - OUTPUT: Modal logic in frontend/src/components/CashierPOS/CheckoutModal.jsx.
  - VERIFY: Verify split balance displays cash due correctly on cart sizes exceeding limit.

- Task 3.5: Build redirect post-verification state logic.
  - Agent: frontend-specialist
  - Skill: frontend-design
  - INPUT: Verification outcomes.
  - OUTPUT: Verification routes and successful completion state resets.
  - VERIFY: Ensure cart empties entirely, session resets, and page redirects smoothly on success.

### Phase 4: WFH Slack Bot Ordering & Swiggy MCP Integration (P1 Core Integrations)

- Task 4.1: Integrate conversational Slack/Teams mock router using LLM menu lookups.
  - Agent: backend-specialist
  - Skill: python-patterns
  - INPUT: Natural language prompt and canteen menus.
  - OUTPUT: Conversational router in backend/app/services/slack_bot.py.
  - VERIFY: Query user request and assert matches correct items.

- Task 4.2: Build Swiggy MCP adapter and deep-linking generator for WFH orders.
  - Agent: backend-specialist
  - Skill: api-patterns
  - INPUT: Swiggy item lists.
  - OUTPUT: Swiggy deep-linking URL creator backend/app/services/swiggy_mcp.py.
  - VERIFY: Confirm deep-links contain pre-populated item arguments correctly.

- Task 4.3: Implement AI guardrails split-payment logic checks for chatbot deliveries.
  - Agent: backend-specialist
  - Skill: python-patterns
  - INPUT: HR rule check calculations.
  - OUTPUT: Allowance filtering checks inside the conversational Slack workflow.
  - VERIFY: Request order exceeding budget limit and assert chatbot recommends out-of-pocket split pay.

### Phase 5: HR Compliance Dashboard (P2 Web Interface)

- Task 5.1: Build Plain English HR rule engine parser parsing rules into Postgres filters.
  - Agent: backend-specialist
  - Skill: api-patterns
  - INPUT: AI text prompts.
  - OUTPUT: Save endpoint POST /api/hr/rules in backend/app/api/endpoints/hr_rules.py.
  - VERIFY: Input "Limit daily spend to 250" and assert structured rule compiles to JSON logic.

- Task 5.2: Create HR Unified Ledger real-time transactional dashboard view.
  - Agent: frontend-specialist
  - Skill: frontend-design
  - INPUT: Database ledger records.
  - OUTPUT: Admin ledger table view in frontend/src/components/HRDashboard/LedgerTable.jsx.
  - VERIFY: Assert wallet deduction amounts and personal paid out-of-pocket shares display cleanly in tables.

## Phase X: Verification Checklist

- Run lint audit on backend: `npm run lint` or `flake8`
- Run vulnerability verification scans: `python .agent/skills/vulnerability-scanner/scripts/security_scan.py .`
- Run design and touch targets audits: `python .agent/skills/frontend-design/scripts/ux_audit.py .`
- Confirm full production build executes successfully: `npm run build`
- Confirm local application servers boot: `npm run dev` and `uvicorn backend.app.main:app`
