# 🛡️ Arcium Connect: Zero-Knowledge Web3 Social Onboarding

A privacy-first contact discovery protocol built on Solana, leveraging **Arcium's Private Set Intersection (PSI)** to seamlessly connect Web2 contacts to Web3 without ever exposing raw user data.

## 🌟 The Problem
Traditional applications require users to upload their entire phonebook to centralized servers. Even with hashed data, servers can perform brute-force attacks to reveal personal phone numbers. This is a severe privacy vulnerability.

## 🚀 The Solution: Arcium Connect
Users can discover which of their phone contacts are already using Web3 wallets, enabling seamless USDC transfers. By using Arcium MPC (Multi-Party Computation), no one—not even the dApp servers—knows the full contact list.

### How Arcium Provides Privacy
1. **Client-Side Hashing:** When a user clicks "Find Friends", their local contacts are hashed (SHA-256) directly in the browser.
2. **Arcium PSI Execution:** The hashed data is sent to the Arcium network. 
3. **Zero-Knowledge Matching:** The network computes the intersection between the user's hashed contacts and the smart contract registry. It **only** returns the matching wallet addresses. Non-matching contacts are completely discarded.

## 🏆 Hackathon Judging Criteria Met
* **Innovation (#0.3):** Brings Web2 "Upload Contacts" feature to Web3 using MPC.
* **Technical Implementation:** Full stack integration combining Solana Rust Contracts, Python backend, and a lightweight Client.
* **User Experience (UX):** Simple Phantom wallet connection. The complex cryptography is hidden behind a sleek, informative UI.
* **Impact:** Lowers the barrier to entry for Web3 fintech/social apps.

## 🛠️ How to Run Locally

**1. Navigate to the project directory**
```bash
cd /Users/whjeon/Desktop/Server/Arcium-1
