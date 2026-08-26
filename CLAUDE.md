# CLAUDE.md — Flavbest / Business

Read this first. It is the shared memory between Flavbest, Claude (claude.ai chat = strategy), and Claude Code (you = hands on this repo).

## Who you're working with

Flavbest — Saudi citizen launching an e-commerce business. Not purely money-driven: wants to build something that genuinely helps people. Loves automation, hates repeating manual work. Works Windows PC + iPhone.

**Communication style he expects:** short, direct, action-first. No long explanations, no filler, no lectures. "The sauce, not the news." If a task is done, say done and what changed.

## The mission

Launch a real e-commerce store for the **Saudi market** within a 30-day window: **Aug 24 → Sep 25, 2026**. Test one product with real ads and real orders. Kill or scale by Sep 25.

## Decisions already made (do not reopen these)

| Decision | Choice | Why |
|---|---|---|
| Platform | **Salla** (salla.sa) | KSA-native: mada, Apple Pay, Tabby/Tamara, COD, SAR settlement. Has full REST API + webhooks for automation later. |
| NOT Shopify | ruled out | Shopify Payments unavailable in KSA; needs 3rd-party gateway + extra fees. |
| NOT Amboras | ruled out | Stripe-only payments; Stripe doesn't onboard Saudi merchants. |
| Legal | **وثيقة العمل الحر** (freelance.sa) + **Maroof** | Free, no CR needed at this stage. |
| Model | Buy & resell first, own product later | Test demand cheap before manufacturing. |
| Testing | **Sequential** — one product live at a time, 3 candidates per cycle | One-person team. Lab store + max one winner. Never 5 brands in parallel. |
| Sourcing | Alibaba samples via express air (DDP later) or Riyadh/Jeddah wholesale | Never dropship from AliExpress direct to customers (3-week delivery kills KSA stores). |
| Ads | TikTok + Snapchat, broad targeting, creative-first | KSA audience lives there. Min ~SAR 75/day per ad set. |
| Rejected | US LLC / Shopify Payments path, paid "guru" communities, extra tools | Solves problems he doesn't have; affiliate-funnel advice. |

## This repo

- `Checklist.html` — interactive 30-day launch checklist. **Live at https://flavbest.github.io/Business/Checklist.html via GitHub Pages (main branch, root).**
- Progress/notes are stored in each device's browser (window.storage in Claude viewer, localStorage elsewhere) + a sync-code system. **The file contains no user data. Never add any personal/sensitive data to this repo — it is public, and must stay public or the live site dies.**
- Editing rules: keep the storage key `launch30-v1` and existing task IDs (w1a…w5c) stable or saved progress breaks. Keep `color-scheme: light only` (dark-mode viewers blacked out the page before). Test JS syntax before pushing.

## Current state (as of Aug 26, 2026)

- Infrastructure done: repo public, Pages live, checklist deployed.
- Week 1 tasks mostly NOT done yet: freelance document, Maroof, Salla store, social handles (TikTok/Snap/IG/WhatsApp Business, same name), Metricool, bank account, product radar (TikTok Creative Center filtered to KSA + FB Ad Library + Google Trends KSA), ask 10 people, shortlist 3 products.
- Priority: get Flavbest OFF infrastructure and INTO Week 1 execution. If he asks for more tooling before Week 1 boxes are checked, remind him of Rule 2 below.

## Rules of the month (enforce these)

1. Every day has one action.
2. No new tools, no research rabbit holes after Day 7.
3. "Not perfect" is not a blocker. Ugly store + real orders beats beautiful store + zero.

## Division of labor

- **claude.ai chat**: strategy, research, web verification, plans, Arabic copywriting, mentorship. Has memory of the full journey.
- **You (Claude Code)**: edit files in this repo, commit, push. Site auto-updates via Pages. Verify pushes built successfully.
- When Flavbest brings a task planned in chat, he may paste an instruction written there. Execute it; don't re-litigate the strategy behind it.

## Roadmap after launch (context, not current tasks)

Automation layer once the store is live: Salla webhooks → n8n/Make → order/questions sheet, WhatsApp abandoned-cart + review flows, product-launch script via Salla API, weekly TikTok Creative Center KSA radar. Flavbest will love building these — but only after first product test is running.
