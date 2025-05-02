from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(2048)
public_key = key.publickey()

consent_form = input("Enter your consent form text: ")
consent_hash = SHA256.new(consent_form.encode())
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(consent_hash)

print("\n Consent form digitally signed.")

verify_hash = SHA256.new(consent_form.encode())
verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(verify_hash, signature)
    print(" Signature verification successful. Consent is valid and unaltered.")
except ValueError:
    print(" Signature verification failed. Consent form may have been forged or altered.")
