from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

key = DSA.generate(2048)

def sign_document(document, private_key):
    document_hash = SHA256.new(document.encode())

    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(document_hash)
    return signature

def verify_signature(document, signature, public_key):
    document_hash = SHA256.new(document.encode())

    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(document_hash, signature)
        return True
    except ValueError:
        return False

resume = input("Enter your resume text: ")

signature = sign_document(resume, key)

public_key = key.publickey()

if verify_signature(resume, signature, public_key):
    print("Signature is valid. Resume integrity is maintained.")
else:
    print("Invalid signature. Resume may have been tampered with.")
