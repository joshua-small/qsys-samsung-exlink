from pathlib import Path
import hashlib
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parents[1]
source = (root / "content/SamsungExLink.qplug").read_bytes()
assert hashlib.sha256(source).hexdigest() == "7dde71e232ad47d1e3a51a0ff9a16afe4f73c28ebe5945948a37b607282149c5"
assert b'Version = "1.1.0.1"' in source
assert ET.parse(root / "SamsungExLink.csproj").getroot().findtext("PropertyGroup/Version") == "1.1.0.2"
print("Verified ExLink package 1.1.0.2 / plugin 1.1.0.1")
