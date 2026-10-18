from pathlib import Path
import hashlib
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parents[1]
source = (root / "content/SamsungExLink.qplug").read_bytes()
assert hashlib.sha256(source).hexdigest() == "2f0ce65351c88760e74720fc8720e1dd8df72a17e6f7e605a0418a9661317d87"
assert b'Version = "1.1.0.3"' in source
assert ET.parse(root / "SamsungExLink.csproj").getroot().findtext("PropertyGroup/Version") == "1.1.0.3"
print("Verified ExLink package 1.1.0.3 / plugin 1.1.0.3")
