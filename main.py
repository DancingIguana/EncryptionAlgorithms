import json
import cipher_decipher
import utilities


with open("input.json","r") as f:
    data = json.load(f)

text = data["rawText"]
cipher_pipeline = data["cipherPipeline"]

results = data

clean_text = utilities.normalize(s=text)
data["cleanText"] = clean_text

ciphered_text = cipher_decipher.cipher(
    text=clean_text,
    operation_keys_list=cipher_pipeline
    )

data["cipheredText"] = ciphered_text

deciphered_text = cipher_decipher.decipher(
    ciphered_text=ciphered_text,
    operation_keys_list=reversed(cipher_pipeline)
)

data["decipheredText"] = deciphered_text

successful_operation = deciphered_text == clean_text
data["successfulOperation"] = successful_operation
del data["cipherPipeline"]
with open("./results.json","w") as f:
    json.dump(data,f,indent=6)


print(f"Original text: {text}")
print(f"Cleaned text: {clean_text}")
print(f"Encrypted text: {ciphered_text}")
print(f"Decrypted text: {deciphered_text}")
if successful_operation:
    print("The encryption and decryption were successful")
else:
    print("The encryption and decryption were not successful")


