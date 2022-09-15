# EncryptionAlgorithms
Implementations of some encryption algorithms for  university course

## About the program
With this program you can choose from three possible encryption methods:
  - Shift cipher
  - Permutation cipher
  - Double transposition cipher
And apply them with any quantity, order, and keys to a plaintext to get the encrypted phrase. It's also possible to the decryption of the text.

In order to use these methods you must modify the `input.json` with the text to use (only using letters from a-z), and add a pipeline of the methods and encryption keys to use.

Check this example filling:

```json
{
"rawText": "hellothere",
      "cipherPipeline": [
            {
                  "method": "permutation",
                  "key": "dnasgzbqwejotimlfpvuxryhkc"
            },
            {
                  "method": "shift",
                  "key": 6
            },
            {
                  "method": "doubletransposition",
                  "key": [
                        [4,3,1,2,5],
                        [2,1]
                  ]
            },
            {
                  "method": "shift",
                  "key": 24
            }
        ]
```

By running the following command:
```bash
python3 main.py
```
the program will use the pipeline and text defined in `input.json` and return the results of the original, encrypted and decrypted text. This is displayed under the file of `results.json`.

###
