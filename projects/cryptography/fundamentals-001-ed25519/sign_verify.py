"""
Solana-style ed25519 sign & verify.

Goal: prove to yourself that a Solana wallet address is just an ed25519 public
key, and that a signature is bound to the exact message bytes.

Fill in the TODOs. Run with:
    pip install pynacl base58
    python sign_verify.py
"""

import nacl.signing
import nacl.exceptions
import base58


def main() -> None:
    # 1. Generate a fresh ed25519 keypair.
    #    nacl.signing.SigningKey.generate() returns the private key (the "seed").
    #    Its .verify_key attribute is the matching public key.
    # TODO: signing_key = ...
    # TODO: verify_key = ...

    # 2. The public key is 32 bytes. Solana shows it as base58.
    #    Use bytes(verify_key) to get raw bytes.
    # TODO: pubkey_bytes = ...
    # TODO: address = base58.b58encode(pubkey_bytes).decode()
    # TODO: print address, len(pubkey_bytes)

    # 3. Sign a transaction-like message.
    message = b"Send 1.5 SOL to alice"
    # TODO: signed = signing_key.sign(message)
    #       signed.signature is the 64-byte ed25519 signature
    #       signed.message is the original message bytes
    # TODO: print signature length and signature.hex()

    # 4. Verify with the correct public key & original message → PASS expected
    # TODO: try verify_key.verify(message, signed.signature) and print PASS
    #       except nacl.exceptions.BadSignatureError → print FAIL

    # 5. Tamper test: flip one bit in the message and verify → FAIL expected
    # TODO: tampered = bytes([message[0] ^ 0x01]) + message[1:]
    # TODO: try/except verify and print result

    # 6. Wrong-key test: new keypair, verify original signature with its pubkey → FAIL expected
    # TODO: other_signing_key = nacl.signing.SigningKey.generate()
    # TODO: try other_signing_key.verify_key.verify(message, signed.signature) and print result

    # Bonus: print the seed (private key) in hex — this is what wallet "export private key" gives you
    # TODO: print bytes(signing_key).hex()


if __name__ == "__main__":
    main()
