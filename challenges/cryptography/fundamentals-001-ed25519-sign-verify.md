# Challenge: Solana-style ed25519 Sign & Verify

**Topic:** cryptography > fundamentals
**Level:** beginner
**Date:** 2026-05-03
**Sources:**
- https://solana.com/docs/core/transactions
- https://www.solanakit.com/docs/concepts/keypairs
- https://cryptobook.nakov.com/digital-signatures/eddsa-and-ed25519
- https://pynacl.readthedocs.io/en/latest/signing/

## Problem

Build a small Python script that mimics how a Solana wallet generates a keypair, signs a transaction-like message, and verifies the signature — using the same primitive Solana uses (ed25519 / EdDSA).

You should walk away understanding:
- A Solana keypair = 32-byte private key + 32-byte public key (the public key IS the address)
- The "address" you see in Phantom/Solscan is just `base58(public_key)`
- A signature is 64 bytes, computed over the exact message bytes
- Tampering with even one byte of the message breaks verification

## Requirements

- [ ] Generate a fresh ed25519 keypair using `pynacl`
- [ ] Print the public key as a **base58-encoded** string (this is the wallet address as Solana would display it)
- [ ] Print the public key length in bytes (should be 32)
- [ ] Sign the message: `b"Send 1.5 SOL to alice"`
- [ ] Print the signature length (should be 64) and the signature in hex
- [ ] Verify the signature against the original message — print PASS/FAIL
- [ ] Tamper-test: flip one bit in the message, attempt verification, print PASS/FAIL — must fail
- [ ] Wrong-key test: generate a *second* keypair, try to verify the original signature with the second public key — must fail

## Setup

Install dependencies:
```
pip install pynacl base58
```

## Starter Code

See: `projects/cryptography/fundamentals-001-ed25519/sign_verify.py`

## Acceptance Criteria

- Output clearly shows: address (base58), pubkey length=32, signature length=64
- All three verification checks run and print PASS/FAIL with sensible labels
- Original signature: PASS
- Tampered message: FAIL (handled gracefully, not a crash)
- Wrong key: FAIL (handled gracefully)
- Bonus: also print the *seed* (32-byte private key part) in hex — this is what wallet exports look like

## Solution File

Write your solution in: `projects/cryptography/fundamentals-001-ed25519/sign_verify.py`
