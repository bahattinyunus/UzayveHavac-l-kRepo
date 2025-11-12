"""Basit örnek: Aerocosmos proje yapısında Python örneği

Bu script basitçe bir proje meta verisini okur ve yazdırır.
"""

import json
import os

META = {
    "project": "Aerocosmos Example",
    "language": "Python",
    "description": "Basit örnek script"
}


def main():
    print("Aerocosmos Python örneği")
    print(json.dumps(META, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
