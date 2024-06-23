# import tkinter as tk
# from tkinter import ttk

# class EnigmaMachine:
#     def __init__(self, rotors, reflector, plugboard=None):
#         self.rotors = rotors
#         self.reflector = reflector
#         self.plugboard = plugboard if plugboard else {}
#         self.rotor_positions = [0, 0, 0]

#     def set_rotor_positions(self, positions):
#         self.rotor_positions = positions

#     def encipher(self, text):
#         result = []
#         for char in text:
#             if char.isalpha():
#                 result.append(self.encipher_character(char.upper()))
#         return ''.join(result)

#     def encipher_character(self, char):
#         char = self.plugboard_swap(char)
#         char = self.forward_through_rotors(char)
#         char = self.reflector[char]
#         char = self.backward_through_rotors(char)
#         char = self.plugboard_swap(char)
#         self.step_rotors()
#         return char

#     def plugboard_swap(self, char):
#         return self.plugboard.get(char, char)

#     def forward_through_rotors(self, char):
#         for i, rotor in enumerate(self.rotors):
#             offset = self.rotor_positions[i]
#             index = (ord(char) - ord('A') + offset) % 26
#             char = rotor[index]
#         return char

#     def backward_through_rotors(self, char):
#         for i in range(len(self.rotors)-1, -1, -1):
#             rotor = self.rotors[i]
#             offset = self.rotor_positions[i]
#             index = rotor.index(char)
#             char = chr((index - offset) % 26 + ord('A'))
#         return char

#     def step_rotors(self):
#         self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
#         if self.rotor_positions[0] == 0:
#             self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
#             if self.rotor_positions[1] == 0:
#                 self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26

#     def reset_rotors(self):
#         self.rotor_positions = [0, 0, 0]

#     def encrypt(self, plaintext):
#         self.reset_rotors()
#         return self.encipher(plaintext)

#     def decrypt(self, ciphertext):
#         self.reset_rotors()
#         return self.encipher(ciphertext)


# def main():
#     rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
#     rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
#     rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
#     reflector = {
#         'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 
#         'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 
#         'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 
#         'Y': 'A', 'Z': 'T'
#     }
#     plugboard = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'} 

#     enigma = EnigmaMachine([rotor_1, rotor_2, rotor_3], reflector, plugboard)

#     def convert_text(event=None):
#         text = entry.get()
#         action = action_var.get()
#         if custom_rotors_var.get():
#             positions = [int(rotor_1_pos.get()), int(rotor_2_pos.get()), int(rotor_3_pos.get())]
#             enigma.set_rotor_positions(positions)
#         else:
#             enigma.reset_rotors()

#         if action == 'Encrypt':
#             result = enigma.encrypt(text)
#         else:
#             result = enigma.decrypt(text)
#         result_var.set(result)

#     def toggle_rotor_entries():
#         state = 'normal' if custom_rotors_var.get() else 'disabled'
#         rotor_1_pos_entry.configure(state=state)
#         rotor_2_pos_entry.configure(state=state)
#         rotor_3_pos_entry.configure(state=state)

#     root = tk.Tk()
#     root.title("Enigma Machine")
#     root.geometry("400x300")

#     frame = tk.Frame(root)
#     frame.pack(expand=True)

#     action_var = tk.StringVar(value="Encrypt")
#     result_var = tk.StringVar()
#     custom_rotors_var = tk.BooleanVar()

#     tk.Label(frame, text="Action:").pack(anchor=tk.CENTER)
#     action_menu = ttk.Combobox(frame, textvariable=action_var, values=["Encrypt", "Decrypt"])
#     action_menu.pack(anchor=tk.CENTER)

#     def open_action_menu(event):
#         action_menu.event_generate('<Down>')

#     action_menu.bind('<Button-1>', open_action_menu)

#     tk.Label(frame, text="Text:").pack(anchor=tk.CENTER)
#     entry = tk.Entry(frame, width=50)
#     entry.pack(anchor=tk.CENTER)
#     entry.bind('<Return>', convert_text)

#     custom_rotors_check = tk.Checkbutton(frame, text="Custom Rotor Positions", variable=custom_rotors_var, command=toggle_rotor_entries)
#     custom_rotors_check.pack(anchor=tk.CENTER)

#     rotor_frame = tk.Frame(frame)
#     rotor_frame.pack(anchor=tk.CENTER)

#     tk.Label(rotor_frame, text="Rotor 1 Position:").grid(row=0, column=0, sticky=tk.E)
#     rotor_1_pos = tk.StringVar(value="0")
#     rotor_1_pos_entry = tk.Entry(rotor_frame, textvariable=rotor_1_pos, width=5, state='disabled')
#     rotor_1_pos_entry.grid(row=0, column=1)

#     tk.Label(rotor_frame, text="Rotor 2 Position:").grid(row=1, column=0, sticky=tk.E)
#     rotor_2_pos = tk.StringVar(value="0")
#     rotor_2_pos_entry = tk.Entry(rotor_frame, textvariable=rotor_2_pos, width=5, state='disabled')
#     rotor_2_pos_entry.grid(row=1, column=1)

#     tk.Label(rotor_frame, text="Rotor 3 Position:").grid(row=2, column=0, sticky=tk.E)
#     rotor_3_pos = tk.StringVar(value="0")
#     rotor_3_pos_entry = tk.Entry(rotor_frame, textvariable=rotor_3_pos, width=5, state='disabled')
#     rotor_3_pos_entry.grid(row=2, column=1)

#     convert_button = tk.Button(frame, text="Convert", command=convert_text)
#     convert_button.pack(anchor=tk.CENTER, pady=10)

#     tk.Label(frame, text="Result:").pack(anchor=tk.CENTER)
#     result_entry = tk.Entry(frame, textvariable=result_var, width=50, state='readonly')
#     result_entry.pack(anchor=tk.CENTER)

#     root.mainloop()

# if __name__ == "__main__":
#     main()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard=None):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard if plugboard else {}
        self.rotor_positions = [0, 0, 0]

    def set_rotor_positions(self, positions):
        self.rotor_positions = positions

    def encipher(self, text):
        result = []
        for char in text:
            if char.isalpha() or char.isdigit():
                result.append(self.encipher_character(char))
            else:
                result.append(char)
        return ''.join(result)

    def encipher_character(self, char):
        is_upper = char.isupper()
        char = char.upper()

        char = self.plugboard_swap(char)
        if char.isdigit():
            char = self.encipher_digit(char)
        else:
            char = self.encipher_letter(char)
        char = self.plugboard_swap(char)

        self.step_rotors()

        return char if is_upper else char.lower()

    def encipher_digit(self, digit):
        digit_index = ord(digit) - ord('0') + 26
        char = chr(digit_index + ord('A'))
        char = self.forward_through_rotors(char)
        char = self.reflector[char]
        char = self.backward_through_rotors(char)
        digit_index = ord(char) - ord('A') - 26
        return chr(digit_index + ord('0'))

    def encipher_letter(self, char):
        char = self.forward_through_rotors(char)
        char = self.reflector[char]
        char = self.backward_through_rotors(char)
        return char

    def plugboard_swap(self, char):
        return self.plugboard.get(char, char)

    def forward_through_rotors(self, char):
        for i, rotor in enumerate(self.rotors):
            offset = self.rotor_positions[i]
            index = (ord(char) - ord('A') + offset) % 26
            char = rotor[index]
        return char

    def backward_through_rotors(self, char):
        for i in range(len(self.rotors)-1, -1, -1):
            rotor = self.rotors[i]
            offset = self.rotor_positions[i]
            index = rotor.index(char)
            char = chr((index - offset) % 26 + ord('A'))
        return char

    def step_rotors(self):
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
        if self.rotor_positions[0] == 0:
            self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
            if self.rotor_positions[1] == 0:
                self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26

    def reset_rotors(self):
        self.rotor_positions = [0, 0, 0]

    def encrypt(self, plaintext):
        self.reset_rotors()
        return self.encipher(plaintext)

    def decrypt(self, ciphertext):
        self.reset_rotors()
        return self.encipher(ciphertext)


def main():
    rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflector = {
        'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 
        'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 
        'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 
        'Y': 'A', 'Z': 'T', '0': '5', '1': '8', '2': '3', '3': '2', '4': '9', '5': '0', 
        '6': '7', '7': '6', '8': '1', '9': '4'
    }
    plugboard = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C', '1': '2', '2': '1'} 

    enigma = EnigmaMachine([rotor_1, rotor_2, rotor_3], reflector, plugboard)

    def convert_text(event=None):
        text = entry.get()
        action = action_var.get()
        if custom_rotors_var.get():
            positions = [int(rotor_1_pos.get()), int(rotor_2_pos.get()), int(rotor_3_pos.get())]
            enigma.set_rotor_positions(positions)
        else:
            enigma.reset_rotors()

        if action == 'Encrypt':
            result = enigma.encrypt(text)
        else:
            result = enigma.decrypt(text)
        result_var.set(result)

    def toggle_rotor_entries():
        state = 'normal' if custom_rotors_var.get() else 'disabled'
        rotor_1_pos_entry.configure(state=state)
        rotor_2_pos_entry.configure(state=state)
        rotor_3_pos_entry.configure(state=state)

    root = tk.Tk()
    root.iconbitmap("C:/Users/Jar Jar Banton/Documents/Python apps/PCboard3x_42195.ico")
    root.title("Enigma Machine")
    root.geometry("500x400")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    action_var = tk.StringVar(value="Encrypt")
    result_var = tk.StringVar()
    custom_rotors_var = tk.BooleanVar()

    tk.Label(frame, text="Action:").pack(anchor=tk.CENTER)
    action_menu = ttk.Combobox(frame, textvariable=action_var, values=["Encrypt", "Decrypt"])
    action_menu.pack(anchor=tk.CENTER)

    def open_action_menu(event):
        action_menu.event_generate('<Down>')

    action_menu.bind('<Button-1>', open_action_menu)

    tk.Label(frame, text="Text:").pack(anchor=tk.CENTER)
    entry = tk.Entry(frame, width=50)
    entry.pack(anchor=tk.CENTER)
    entry.bind('<Return>', convert_text)

    custom_rotors_check = tk.Checkbutton(frame, text="Custom Rotor Positions", variable=custom_rotors_var, command=toggle_rotor_entries)
    custom_rotors_check.pack(anchor=tk.CENTER)

    rotor_frame = tk.Frame(frame)
    rotor_frame.pack(anchor=tk.CENTER)

    tk.Label(rotor_frame, text="Rotor 1 Position:").grid(row=0, column=0, sticky=tk.E)
    rotor_1_pos = tk.StringVar(value="0")
    rotor_1_pos_entry = tk.Entry(rotor_frame, textvariable=rotor_1_pos, width=5, state='disabled')
    rotor_1_pos_entry.grid(row=0, column=1)

    tk.Label(rotor_frame, text="Rotor 2 Position:").grid(row=1, column=0, sticky=tk.E)
    rotor_2_pos = tk.StringVar(value="0")
    rotor_2_pos_entry = tk.Entry(rotor_frame, textvariable=rotor_2_pos, width=5, state='disabled')
    rotor_2_pos_entry.grid(row=1, column=1)

    tk.Label(rotor_frame, text="Rotor 3 Position:").grid(row=2, column=0, sticky=tk.E)
    rotor_3_pos = tk.StringVar(value="0")
    rotor_3_pos_entry = tk.Entry(rotor_frame, textvariable=rotor_3_pos, width=5, state='disabled')
    rotor_3_pos_entry.grid(row=2, column=1)

    convert_button = tk.Button(frame, text="Convert", command=convert_text)
    convert_button.pack(anchor=tk.CENTER, pady=10)

    tk.Label(frame, text="Result:").pack(anchor=tk.CENTER)
    result_entry = tk.Entry(frame, textvariable=result_var, width=50, state='readonly')
    result_entry.pack(anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()
