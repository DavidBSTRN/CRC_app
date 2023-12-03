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
    pass

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


app.mainloop()

