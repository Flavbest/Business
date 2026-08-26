# CLAUDE.md — Flavbest / Business

Read this first. It is the shared memory between Flavbest, Claude (claude.ai chat = strategy), and Claude Code (you = hands on this repo).

## Who you're working with

Flavbest — Saudi citizen launching an e-commerce business. Not purely money-driven: wants to build something that genuinely helps people. Loves automation, hates repeating manual work. Works Windows PC + iPhone.

**Communication style he expects:** short, direct, action-first. No long explanations, no filler, no lectures. "The sauce, not the news." If a task is done, say done and what changed.

## The mission

Launch a real e-commerce store for the **Saudi market** within a 30-day window: **Sep 1 → Oct 3, 2026**. Test one product with real ads and real orders. Kill or scale by Oct 3.

## Decisions already made (do not reopen these)

| Decision | Choice | Why |
|---|---|---|
| Platform | **Salla** (salla.sa) | KSA-native: mada, Apple Pay, Tabby/Tamara, COD, SAR settlement. Has full REST API + webhooks for automation later. |
| NOT Shopify | ruled out | Shopify Payments unavailable in KSA; needs 3rd-party gateway + extra fees. |
| NOT Amboras | ruled out | Stripe-only payments; Stripe doesn't onboard Saudi merchants. |
| Legal | **وثيقة العمل الحر** (freelance.sa) + store verification on **منصة الأعمال / business.sa** | Free, no CR needed. **Maroof is dead for e-stores** — the Ministry of Commerce moved verification to the Saudi Business Center. business.sa also requires a commercial bank account for the store. |
| Model | Buy & resell first, own product later | Test demand cheap before manufacturing. |
| Testing | **Sequential** — one product live at a time, 3 candidates per cycle | One-person team. Lab store + max one winner. Never 5 brands in parallel. |
| Sourcing | Alibaba samples via express air (DDP later) or Riyadh/Jeddah wholesale | Never dropship from AliExpress direct to customers (3-week delivery kills KSA stores). |
| Ads | TikTok + Snapchat, broad targeting, creative-first | KSA audience lives there. Min ~SAR 75/day per ad set. |
| Rejected | US LLC / Shopify Payments path, paid "guru" communities, extra tools | Solves problems he doesn't have; affiliate-funnel advice. |

## This repo

- `Checklist.html` — **GENERATED, do not hand-edit.** Public reference copy of the checklist, live at https://flavbest.github.io/Business/Checklist.html via GitHub Pages (main branch, root).
- **The source of truth is the Claude artifact**, whose source lives at `F:\AI\Business
otes\checklist-artifact.html` (outside this repo, private). It saves progress into the page itself so phone and PC stay in step.
- `build-checklist.py` regenerates `Checklist.html` from that source. It empties the state block first — **progress and the scratchpad (supplier names, prices, margins) must never be committed to this public repo.** Edit the artifact source, run the script, commit.
- Progress/notes are stored in each device's browser (window.storage in Claude viewer, localStorage elsewhere) + a sync-code system. **The file contains no user data. Never add any personal/sensitive data to this repo — it is public, and must stay public or the live site dies.**
- Editing rules: keep the storage key `launch30-v1` and existing task IDs (w1a…w5c) stable or saved progress breaks. Keep `color-scheme: light only` (dark-mode viewers blacked out the page before). Test JS syntax before pushing.

## Current state (as of Aug 26, 2026)

- Infrastructure done: repo public, Pages live, checklist deployed.
- Week 1 tasks NOT done yet (13, in this order): Salla store → freelance document → **commercial bank account** → **business.sa verification** → house name → social handles (TikTok/Snap/IG/WhatsApp Business, same name) → brand kit → Metricool → product radar (TikTok Creative Center filtered to KSA + FB Ad Library + Google Trends KSA) → ask 10 people → shortlist 3 products. 30 tasks total.
- **Corrected Aug 26, 2026:** this file said "Maroof" and that was stale — the Ministry of Commerce moved e-store verification to منصة الأعمال (business.sa) back in **March 2023**. Flavbest caught it. The bank account moved ahead of verification because business.sa requires one; it is a dependency now, not housekeeping. **Verify KSA government process against the source before repeating what this file says** — it has been wrong once.
- **Window moved (decided Aug 26, 2026):** the launch window was Aug 24 → Sep 25; Flavbest chose to start Sep 1 instead. Blocks are now Week 1 `Sep 1–7`, Week 2 `Sep 8–14`, Week 3 `Sep 15–21`, Week 4 `Sep 22–28`, Decide `Sep 29 – Oct 3`. Do not reopen; the checklist and this file agree.
- Priority: get Flavbest OFF infrastructure and INTO Week 1 execution. If he asks for more tooling before Week 1 boxes are checked, remind him of Rule 2 below.

## Branding (decided Aug 26, 2026)

**One house brand, not one brand per product.** Flavbest doesn't know what he's selling yet, so a brand per candidate is 3x the work to throw 2 away. Pick ONE neutral parent name tied to no product category — it survives all three tests and every pivot. Each product gets a product *name* and a landing page, never its own identity.

- Name must work in Arabic AND Latin. Most AI logo generators mangle Arabic script — check the render before committing.
- Tools: Namelix (names, free) + Canva (logo, brand kit, social pack, free). Arabic fonts: Tajawal, Cairo, IBM Plex Sans Arabic.
- Do NOT buy Looka / Brandmark / Tailor Brands. Per-brand pricing, weak Arabic output.
- Never use AI-generated images of the actual product. Photograph and film the real sample — a mismatch between the ad and what arrives drives returns and bad reviews, which kills a new KSA store faster than a plain logo ever would.

## Paperwork note — the website field

The freelance document (وثيقة العمل الحر) requires: Saudi national 18+, Absher/Nafath, a specialization from their list, and proof of practising the profession (certificates or work samples). **A website is not in the requirements.** If a website/portfolio field blocks him, the answer is to open the free Salla store FIRST — it needs no document and its subdomain is a real business URL. That is why `w1c` now precedes `w1a`. Never put a URL that does not exist on a government form.

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
