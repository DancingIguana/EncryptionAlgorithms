import PySimpleGUI as sg



import cv2
import rsa
import numpy as np
import os
import subprocess

width = 250
height = 250

def are_keys_defined(users: list, key_dir = "./keys") -> bool:
    for key_type in ["public","private"]:
        for user in users:
            if not os.path.exists(f"{key_dir}/{user}/{key_type}.pem") or not os.path.exists(f"{key_dir}/{user}/{key_type}.txt"):
                return False
    
    return True

def create_process_str(msg,msg_encrypted,msg_decrypted,signature,verify_result):
    process_str = "Message from Aki to Denji details:\n"
    process_str += "#"*100
    process_str += f"\n\nAki wrote:\n\t{msg}"
    process_str += f"\n\nSignature with Aki's private key: {signature}"
    process_str += f"\n\n Encrypted message with Denji's public key: {msg_encrypted}\n"
    process_str += "#"*100
    process_str += f"\nDenji received:\n\t- Aki's encrypted message: {msg_encrypted}\n\t- Signature: {signature}"
    process_str += f"\n\n Denji decrypted the message with his private key and got: {msg_decrypted}"
    process_str += f"\n\n Denji verifies the signature with Aki's public key and sees the following message: {verify_result}"
    if verify_result == "Valid signature":
        process_str += "\n\nThe message was sent successfully with an adequate encryption and signature"
    else:
        process_str += "\n\nThe message wasn't verified adequately"
    return process_str
        

def load_image_gray(filename: str) -> np.array:
    """
    Given a filename, load the image in grayscale with cv2 and make sure
    that its width and height are even.
    Parameters:
    -------------------
    filename: the file path of the image
    Returns:
    -------------------
    the grayscale image matrix
    """
    if os.path.exists(filename):
        cv2_image = cv2.imread(filename)

        cv2_image = cv2.resize(cv2_image,(width, height))

        gray_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
        return gray_image

def array_to_data(image: np.array):
    """
    Given an image, get the image in bytes for displaying 
    in PySimpleGUI
    Parameters:
    --------------------
    image: the matrix of the image
    Returns:
    --------------------
    The bytes of the image
    """
    imgbytes = cv2.imencode(".png", image)[1].tobytes()
    return imgbytes

def make_window():
    """
    Creates the main window
    """
    sg.theme("Dark Blue 15")

    # First the window layout...2 columns
    image_left = sg.Column([
        [sg.Text("Aki", justification = "center")],
        [sg.Button("Public Key (A)"),sg.Button("Private Key (A)")],
        [sg.Frame('', [
            [
                sg.Graph(
                canvas_size = (width,height),
                key = "-AKI-",
                graph_bottom_left = (-width/2, -height/2),
                graph_top_right = (width/2, height/2))
            ]
        ])],
        

    ], element_justification = "center")

    image_right = sg.Column([

        [sg.Text("Denji", justification = "center")],
        [sg.Button("Public Key (B)"),sg.Button("Private Key (B)")],
        [sg.Frame('', [
            [
                sg.Graph(
                canvas_size = (width,height),
                key = "-DENJI-",
                graph_bottom_left = (-width/2, -height/2),
                graph_top_right = (width/2, height/2))
            ]
        ])],
        
    ], element_justification = "center")

    input_section_left = sg.Column([
        [sg.MLine(size=(41, 5), enter_submits=True, key='-QUERY-')],
        [sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True)]
    ], element_justification = "center")

    results_section_right = sg.Column([
        [sg.Button("Results", button_color=(sg.YELLOWS[0], sg.BLUES[0]), size = (41,1),bind_return_key=True)]
    ], element_justification = "center",)

    layout = [
        [image_left,image_right],
        [input_section_left,results_section_right]]

    return sg.Window("Public and Private Key basics", layout, finalize = True)
    


def main():
    A = "Aki"
    B = "Denji"
    assert(are_keys_defined([A,B])), "Please generate the keys for the users (Aki and Denji) through generate_keys"
    
    with open(f'./keys/{A}/public.pem', mode='rb') as f:
        keydata = f.read()
    a_pub = rsa.PublicKey.load_pkcs1(keydata)

    with open(f'./keys/{A}/private.pem', mode='rb') as f:
        keydata = f.read()
    a_priv = rsa.PrivateKey.load_pkcs1(keydata)

    with open(f'./keys/{B}/public.pem', mode='rb') as f:
        keydata = f.read()
    b_pub = rsa.PublicKey.load_pkcs1(keydata)

    with open(f'./keys/{B}/private.pem', mode='rb') as f:
        keydata = f.read()
    b_priv = rsa.PrivateKey.load_pkcs1(keydata)


    sg.theme("Dark Blue 3")
    img_A = load_image_gray("./images/aki_img_good.png")
    img_A_bytes = array_to_data(img_A)

    img_B = load_image_gray("./images/denji_img.png")
    img_B_bytes = array_to_data(img_B)

    window = make_window()
    
    graph_A = window["-AKI-"]
    graph_A.draw_image(data = img_A_bytes,location = (-width/2,height/2))

    graph_B = window["-DENJI-"]
    graph_B.draw_image(data = img_B_bytes,location = (-width/2,height/2))
    
    
    while True:
        event, values = window.read(timeout=10)
        # print(event, values)
        if event in ('Exit'):
            break
        
        if event == "Public Key (A)":
            subprocess.call(['open', f"./keys/{A}/public.txt"])
        
        if event == "Public Key (B)":
            subprocess.call(['open', f"./keys/{B}/public.txt"])

        if event == "Private Key (A)":
            subprocess.call(['open', f"./keys/{A}/private.txt"])

        if event == "Private Key (B)":
            subprocess.call(['open', f"./keys/{B}/private.txt"])

        if event == "SEND":
            # The user writes a message
            msg = values["-QUERY-"]
            
            # The message is encoded
            msg_encoded = msg.encode()

            # Generate hash from A and corresponding signature
            signature_A = rsa.sign(msg_encoded,a_priv, "SHA-1")
            
            # The message is encrypted for B to receive
            msg_encrypted = rsa.encrypt(msg_encoded, b_pub)

            # B receives the signature and message. First he decrypts the message
            msg_decrypted = rsa.decrypt(msg_encrypted, b_priv)

            # Now with the message he verifies the signature is from Alice
            verify_msg = "Valid signature"
            try:
                rsa.verify(msg_decrypted, signature_A, a_pub)
            except:
                verify_msg = "Invalid Signature"

            with open("./message_summary.txt","w") as f:
                f.write(create_process_str(msg,msg_encrypted,msg_decrypted,signature_A,verify_msg))

        if event == "Results" and os.path.exists("./message_summary.txt"):
            subprocess.call(["open","./message_summary.txt"])


    window.close()

main()