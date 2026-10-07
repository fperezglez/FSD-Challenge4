import hashlib, json, sys
from pathlib import Path

def sha256_int(data: bytes) -> int:
    return int.from_bytes(hashlib.sha256(data).digest(), "big")

def verify(path, signature, e, n):
    data = Path(path).read_bytes()
    h = sha256_int(data)
    recovered = pow(int(signature), int(e), int(n))
    return h == recovered, h, recovered

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verifier.py check.json")
        raise SystemExit(1)
    cfg = json.loads(Path(sys.argv[1]).read_text())
    ok, h, recovered = verify(
        Path(sys.argv[1]).parent.parent / "evidence" / cfg["document"],
        cfg["signature"], cfg["public_key"]["e"], cfg["public_key"]["n"])
    print("VALID" if ok else "INVALID")
    print(f"hash mod n: {h % cfg['public_key']['n']}")
    print(f"recovered:  {recovered}")
