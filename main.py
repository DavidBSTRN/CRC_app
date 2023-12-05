import crc_functions as crc
import customtkinter as ctk

# FUNCTIONS
def isOkay(new_value):
    """Check enter just '0' and '1'"""
    if new_value == "":
        return True

    return all(c in '01' for c in new_value)

def get_poly():
    """Show gen.pol."""
    try:
        user_code = nk_enter.get()
        nk = []
        for i in user_code.split(","):
            nk.append(int(i))

        gen_poly = ' | '.join(crc.find_gen_poly(nk[0], nk[1]))

        gen_text.set(f"Gen. pol: {gen_poly}")
    except:
        gen_text.set("")

def encode_msg():
    """Show encode msg"""
    message = msg_enter.get()
    key = gen_enter.get()

    if len(key) != 0 and len(message) != 0:
        code_message = crc.encoder(message, key)

        bin_text.set(f"{code_message}")
        poly_msg.configure(text=f"{crc.bin_to_poly(code_message)}")
    else:
        bin_text.set(f"Incorrect input.")
        poly_msg.configure(text="")

def decode_msg():
    """Show decode msg or corrections"""
    message = msg_enter2.get()
    key = gen_enter2.get()

    if len(key) != 0 and len(message) != 0:
        if int(crc.mod_2(message, key)) == 0:
            decode_label.configure(text="Message is correct.")
            correct_text.set(f"{message}")
            poly_label.configure(text=f"{crc.bin_to_poly(message)}")
        else:
            correct_message = ' | '.join(crc.find_mistake(message, key))

            decode_label.configure(text="Message is incorrect.")
            correct_text.set(f"Correction: {correct_message}")
            poly_label.configure(text="")
    else:
        decode_label.configure(text="Incorrect input.")
        correct_text.set("")
        poly_label.configure(text="")

# set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# main
app = ctk.CTk()
app.title("CRC encode and decode")
app.resizable(False, False)

# check user input
validate_cmd = app.register(isOkay)

# tabview
tabview = ctk.CTkTabview(app)
tabview.pack()

# my tabs
encode_tab = tabview.add("Encode")
decode_tab = tabview.add("Decode")

# ENCODE
# entry 'n,k'
nk_enter = ctk.CTkEntry(encode_tab)
nk_enter.grid(row = 1, column = 0, padx = 10, pady = (10,0))

# "n,k' label
nk_label = ctk.CTkLabel(encode_tab, text = "Enter code: 'n,k'")
nk_label.grid(row = 0, column = 0, padx = 10, pady = (10,0))

# gen polynomials label
gen_text = ctk.StringVar()
gen_text.set("")
gen_label = ctk.CTkEntry(encode_tab, fg_color= "transparent", state = "readonly", border_color="gray13",
                        textvariable = gen_text, width = 220, justify = "center")
gen_label.grid(row = 1, column = 2, padx = 10, pady = (10,0))

# Gen button
gen_button = ctk.CTkButton(encode_tab, text = "Get gen.pol.", command = get_poly)
gen_button.grid(row = 1, column = 1, padx = 10, pady = (10,0))

# empty row
empty = ctk.CTkLabel(encode_tab, text = "")
empty.grid(row = 2, column = 0, padx = 10, pady = (10,0))

# entry msg label
entry_msg_label = ctk.CTkLabel(encode_tab, text = "Enter message")
entry_msg_label.grid(row = 3, column = 0, padx = 10, pady = (10,0))

# entry message
msg_enter = ctk.CTkEntry(encode_tab, validate = "key", validatecommand = (validate_cmd, '%P'))
msg_enter.grid(row = 4, column = 0, padx = 10, pady = (10,0))

# entry gan label
entry_gen_label = ctk.CTkLabel(encode_tab, text = "Enter gen.pol.")
entry_gen_label.grid(row = 5, column = 0, padx = 10, pady = (10,0))

# entry gen poly
gen_enter = ctk.CTkEntry(encode_tab, validate = "key", validatecommand = (validate_cmd, '%P'))
gen_enter.grid(row = 6, column = 0, padx = 10, pady = (10,0))

# Encode button
encode_button = ctk.CTkButton(encode_tab, text = "Encode", command = encode_msg)
encode_button.grid(row = 5, column = 1, padx = 10, pady = (10,0))

# Code message labels
bin_text = ctk.StringVar()
bin_text.set("")
bin_msg = ctk.CTkEntry(encode_tab, fg_color= "transparent", state = "readonly", border_color="gray13",
                        textvariable = bin_text, width = 220, justify = "center")
bin_msg.grid(row = 5, column = 2, padx = 10, pady = (10,0))

poly_msg = ctk.CTkLabel(encode_tab, text = "", anchor = "w")
poly_msg.grid(row = 6, column = 2, padx = 10, pady = (10,0))

# DECODE
# entre msg to decode
entry_msg_label2 = ctk.CTkLabel(decode_tab, text = "Enter message")
entry_msg_label2.grid(row = 0, column = 0, padx = 10, pady = (10,0))

# entry message
msg_enter2 = ctk.CTkEntry(decode_tab, validate = "key", validatecommand = (validate_cmd, '%P'))
msg_enter2.grid(row = 1, column = 0, padx = 10, pady = (10,0))

# gen2 label
entry_gen_label2 = ctk.CTkLabel(decode_tab, text = "Enter gen.pol.")
entry_gen_label2.grid(row = 2, column = 0, padx = 10, pady = (10,0))

# entry gen.poly.
gen_enter2 = ctk.CTkEntry(decode_tab, validate = "key", validatecommand = (validate_cmd, '%P'))
gen_enter2.grid(row = 3, column = 0, padx = 10, pady = (10,0))

# decode button
decode_button = ctk.CTkButton(decode_tab, text = "Decode", command = decode_msg)
decode_button.grid(row = 1, column = 1, padx = 10, pady = (10,0))

# Decode label
decode_label = ctk.CTkLabel(decode_tab, text = "", anchor = "w")
decode_label.grid(row = 1, column = 2, padx = 10, pady = (10,0))

correct_text = ctk.StringVar()
correct_text.set("")
correct_label = ctk.CTkEntry(decode_tab, fg_color= "transparent", state = "readonly", border_color="gray13",
                        textvariable = correct_text, width = 220, justify = "center")
correct_label.grid(row = 2, column = 2, padx = 10, pady = (10,0))

poly_label = ctk.CTkLabel(decode_tab, text = "", anchor = "w")
poly_label.grid(row = 3, column = 2, padx = 10, pady = (10,0))

app.mainloop()