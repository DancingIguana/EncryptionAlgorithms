import json
import cipher_decipher
import utilities


with open("message.txt","r") as f:
    lines = f.read().splitlines()


text = lines[0]
print(repr(text))
with open("cipher_pipeline.json","r") as f:
    cipher_pipeline = json.load(f)

#text = data["rawText"]
#cipher_pipeline = data["cipherPipeline"]

results = {}

clean_text = utilities.normalize(s=text)
results["cleanText"] = clean_text


# Encrypt
ciphered_text = cipher_decipher.cipher(
    text=clean_text,
    operation_keys_list=cipher_pipeline
    )

results["cipheredText"] = ciphered_text


# Decrypt
deciphered_text = cipher_decipher.decipher(
    ciphered_text=ciphered_text,
    operation_keys_list=reversed(cipher_pipeline)
)

results["decipheredText"] = deciphered_text

# Store results of operation
successful_operation = deciphered_text == clean_text
results["successfulOperation"] = successful_operation
with open("./results.json","w") as f:
    json.dump(results,f,indent=6)


print(f"Original text: {text}")
print(f"Cleaned text: {clean_text}")
print(f"Encrypted text: {ciphered_text}")
print(f"Decrypted text: {deciphered_text}")
if successful_operation:
    print("The encryption and decryption were successful")
else:
    print("The encryption and decryption were not successful")

with open("encryptedMessage.txt", "w") as f:
	f.write(ciphered_text)
