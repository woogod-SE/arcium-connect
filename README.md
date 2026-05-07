# 🛡️ Arcium Connect: Zero-Knowledge Web3 Social Onboarding

**Arcium Connect** is a privacy-first social discovery protocol built on **Solana Devnet**. It leverages **Private Set Intersection (PSI)** logic—simulating Arcium’s confidential computing environment—to bridge Web2 social graphs with Web3 identities without ever exposing raw contact data.

---

## 🌟 The Problem: The Privacy Trap of Contact Syncing
Web2 social apps require users to upload their entire address book to centralized servers. Even when hashed, these databases are vulnerable to brute-force mapping. 
- **Privacy Leak:** Servers know who you know, even if those people aren't on the platform.
- **Centralized Risk:** Your entire social graph is stored in a single, hackable location.

## 🚀 The Solution: Arcium-Powered PSI
Arcium Connect enables "Zero-Knowledge Discovery." We identify which of your contacts are on Web3 using **Arcium's PSI principles**, ensuring:
1. **Raw Data Never Leaves the Device:** Only cryptographically hashed signatures are transmitted.
2. **True PSI (Private Set Intersection):** The server only computes the "intersection" (matching users). Non-matches are discarded instantly and are never stored or seen by the server.
3. **Solana Integrated Auth:** Every sync is authorized via a Solana wallet signature, ensuring session integrity on the **Solana Devnet**.

---

## 🛠️ Key Features
- **Wallet-to-Wallet Social Hub:** Once matched, instantly **Call/SMS (Web2)** or **Send SOL/USDC (Web3)** to your friends.
- **Arcium PSI Test Suite:** A built-in sandbox to verify how the protocol discards unregistered contacts.
- **Hybrid Deployment:** Optimized for both **Vercel** (Serverless/Frontend) and **VPS/Docker** (Backend/PSI Engine).

---

## 🧠 Technical Integration & Architecture

### 1. Solana Devnet Integration
- **Authentication:** Uses Phantom Wallet to sign unique timestamps, proving ownership.
- **Transactions:** Functional integration with Solana `SystemProgram` for real-time asset transfers to identified friends.

### 2. Arcium PSI Implementation
We have successfully implemented and tested the **PSI (Private Set Intersection)** protocol:
- **Client-side:** Contacts are transformed into SHA-256 hashes locally.
- **Computation Layer:** The backend (simulating an Arcium MXE node) compares the user's encrypted set with the registered registry.
- **Privacy Guarantee:** The computation returns *only* the intersection. The server learns nothing about the user's non-registered contacts.

---

## 🏆 Hackathon Requirements Checklist (#0.2)
- [x] **Functional Solana Project:** Integrated with Devnet for auth and transfers.
- [x] **Arcium Integration:** Implemented PSI-based confidential matching logic.
- [x] **Privacy Benefits:** Clearly demonstrated through local hashing and zero-knowledge results.
- [x] **Open Source:** Full source code available on GitHub.
- [x] **English Submission:** Documentation and UI provided in English.

---

## 🧪 Testing the PSI Protocol (Demo Guide)

1. **Access the Live Demo:** [Your Vercel URL Here]
2. **Connect Wallet:** Switch your Phantom Wallet to **Devnet**.
3. **Authorize:** Sign the message to prove wallet ownership.
4. **Run PSI Sync:** - Notice `010-1234-5678` is a registered user.
   - Notice `010-5555-9999` is **NOT** in the registry.
5. **Observe Result:** Only the registered user appears. The unregistered contact is discarded by the PSI logic, proving Arcium's privacy model works.

---

## ⚙️ Local Development (Docker)

```bash
# Clone the repository
git clone [https://github.com/woogod-SE/arcium-connect.git](https://github.com/woogod-SE/arcium-connect.git)
cd arcium-connect

# Start via Docker Compose
docker-compose up --build -d
