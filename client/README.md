# Toy verifier

Run from this directory:

```bash
python verifier.py ../evidence/check_original.json
python verifier.py ../evidence/check_modified.json
```

This is deliberately tiny classroom RSA. It is **not** a secure implementation
of RSA signatures; in particular, it uses textbook RSA on a SHA-256 digest
reduced modulo the small classroom modulus.
