import hashlib

document = "Confidential report: The project status is on track for the deadline."
encoded_document = document.encode()
sha1_hash = hashlib.sha1()
sha1_hash.update(encoded_document)
message_digest = sha1_hash.hexdigest()

print("The resulting SHA-1 message digest is:")
print(message_digest)
