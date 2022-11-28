# Public Private Keys
Extremely basic implementation of the Public and Private key principles using Python-RSA and PySimpleGUI.

## Dependencies

- [PysimpleGUI](https://www.pysimplegui.org/en/latest/)
- [Python-RSA](https://stuvel.eu/software/rsa/)
- [NumPy](https://numpy.org/)
- [OpenCV](https://docs.opencv.org/4.x/index.html)

## Get Started

First download this folder. Afterwards get the necessary libraries (Python-RSA and PySimpleGUI) by running the following command.
```
pip install -r requirements.txt
```

Once done with that, you can generate your public and private keys by running the script of `generate_keys.py` followed by the name of the user. The existing users are 'Aki' and 'Denji'.
```
python3 generate_keys.py Aki
```

Now you can run the app with the PySimpleGUI interface.
```python3
python3 app.py
```
## App

![App Image](https://github.com/DancingIguana/EncryptionAlgorithms/blob/main/PublicPrivateKeys/images/app_img.png)
