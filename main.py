import crc_functions as crc
import customtkinter as ctk

# set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# main
app = ctk.CTk()
app.title("CRC encode and decode")
app.geometry("800x480")

# tabview
tabview = ctk.CTkTabview(app, width = 780, height = 460)
tabview.pack()

# my tabs
encode_tab = tabview.add("Encode")
decode_tab = tabview.add("Decode")

# FUNCTION
def get_poly():
    try:
        user_code = nk_enter.get()
        nk = []
        for i in user_code.split(","):
            nk.append(int(i))

        gen_poly = ' | '.join(crc.find_gen_poly(nk[0], nk[1]))

        gen_label.configure(text = f"Gen. pol: {gen_poly}")
        nk_label.configure(text="")
    except:
        gen_label.configure(text="")
        nk_label.configure(text = "Input the 'n,k'...(7,4)")

def encode_msg():
    message = msg_enter.get()
    key = gen_enter.get()

    code_message = crc.encoder(message, key)

    bin_msg.configure(text = f"{code_message}")
    poly_msg.configure(text = f"{crc.bin_to_poly(code_message)}")

def decode_msg():
    message = msg_enter2.get()
    key = gen_enter2.get()

    if int(crc.mod_2(message, key)) == 0:
        decode_label.configure(text = "Message is correct.")
        correct_label.configure(text = f"{message}")
        poly_label.configure(text = f"{crc.bin_to_poly(message)}")
    else:
        decode_label.configure(text="Message is incorrect.")
        correct_label.configure(text = f"Correct message: {crc.find_mistake(message, key)}")
        poly_label.configure(text=f"{crc.bin_to_poly(crc.find_mistake(message, key))}")

# ENCODE
# entry 'n,k'
nk_enter = ctk.CTkEntry(encode_tab, placeholder_text = "Code 'n,k'")
nk_enter.grid(row = 0, column = 0, padx = 10, pady = (10,0))

# "n,k' label
nk_label = ctk.CTkLabel(encode_tab, text = "")
nk_label.grid(row = 1, column = 0, padx = 10, pady = (10,0))

# gen polynomials label
gen_label = ctk.CTkLabel(encode_tab, text = "")
gen_label.grid(row = 0, column = 2, padx = 10, pady = (10,0))

# Gen button
gen_button = ctk.CTkButton(encode_tab, text = "Get gen.pol.", command = get_poly)
gen_button.grid(row = 0, column = 1, padx = 10, pady = (10,0))

# entry message
msg_enter = ctk.CTkEntry(encode_tab, placeholder_text = "Enter message")
msg_enter.grid(row = 2, column = 0, padx = 10, pady = (10,0))

# entry gen poly
gen_enter = ctk.CTkEntry(encode_tab, placeholder_text = "Enter gen.pol.")
gen_enter.grid(row = 3, column = 0, padx = 10, pady = (10,0))

# Encode button
encode_button = ctk.CTkButton(encode_tab, text = "Encode", command = encode_msg)
encode_button.grid(row = 2, column = 1, padx = 10, pady = (10,0))

# Code message labels
bin_msg = ctk.CTkLabel(encode_tab, text = "")
bin_msg.grid(row = 2, column = 2, padx = 10, pady = (10,0))

poly_msg = ctk.CTkLabel(encode_tab, text = "")
poly_msg.grid(row = 3, column = 2, padx = 10, pady = (10,0))

# DECODE
# entry message
msg_enter2 = ctk.CTkEntry(decode_tab, placeholder_text = "Enter message")
msg_enter2.grid(row = 0, column = 0, padx = 10, pady = (10,0))

# entry gen.poly.
gen_enter2 = ctk.CTkEntry(decode_tab, placeholder_text = "Enter gen.pol.")
gen_enter2.grid(row = 1, column = 0, padx = 10, pady = (10,0))

# decode button
decode_button = ctk.CTkButton(decode_tab, text = "Decode", command = decode_msg)
decode_button.grid(row = 0, column = 1, padx = 10, pady = (10,0))

# Decode label
decode_label = ctk.CTkLabel(decode_tab, text = "")
decode_label.grid(row = 0, column = 2, padx = 10, pady = (10,0))

correct_label = ctk.CTkLabel(decode_tab, text = "")
correct_label.grid(row = 1, column = 2, padx = 10, pady = (10,0))

poly_label = ctk.CTkLabel(decode_tab, text = "")
poly_label.grid(row = 2, column = 2, padx = 10, pady = (10,0))

app.mainloop()