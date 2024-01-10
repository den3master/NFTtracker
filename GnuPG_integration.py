import subprocess
import getpass

passphrase = getpass.getpass("Passphrase:")
passphrase2 = getpass.getpass("Passphrase:")

if passphrase != passphrase2:
  raise ValueError("Passphrases not identical!")

# Зашифровка
print("Encrypting...")

args = [
  "gpg",
  "--batch",
  "--passphrase-fd", "0",
  "--output", "encrypted.gpg",
  "--symmetric",
  "--yes",
  "--cipher-algo", "AES256",
  "plain.txt",
]

result = subprocess.run(
  args, input=passphrase.encode(),
  capture_output=True)

if result.returncode != 0:
  raise ValueError(result.stderr)