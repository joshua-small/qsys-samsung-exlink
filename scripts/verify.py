"""Verify reviewed source bytes and product/release identity before packaging."""
import argparse
import hashlib
from pathlib import Path
from package_checks import check_identity

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--release-tag", help="Exact release tag; must equal v + source and project version")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = (root / "content/SamsungExLink.qplug").read_bytes()
if hashlib.sha256(source).hexdigest() != "2f0ce65351c88760e74720fc8720e1dd8df72a17e6f7e605a0418a9661317d87":
    raise SystemExit("Update the reviewed source digest for an intentional plugin revision")
try:
    version = check_identity(source.decode("utf-8-sig"), (root / "SamsungExLink.csproj").read_text(),
        "JoshuaSmall.Qsys.SamsungExLink", args.release_tag)
except ValueError as error:
    raise SystemExit(str(error)) from error
if not (root / "icon.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
    raise SystemExit("Invalid package icon")
if "https://joshua-small.github.io/qsys-samsung-exlink/registration/joshuasmall.qsys.samsungexlink/index.json" not in (root / "README.md").read_text():
    raise SystemExit("README Library feed does not match package identity")
print("Verified", "SamsungExLink.qplug", version, hashlib.sha256(source).hexdigest())
