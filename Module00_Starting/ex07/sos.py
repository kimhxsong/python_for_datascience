import sys

morse_codes = {"A": ".-",
               "B": "-...",
               "C": "-.-.",
               "D": "-..",
               "E": ".",
               "F": "..-.",
               "G": "--.",
               "H": "....",
               "I": "..",
               "J": ".---",
               "K": "-.-",
               "L": ".-..",
               "M": "--",
               "N": "-.",
               "O": "---",
               "P": ".--.",
               "Q": "--.-",
               "R": ".-.",
               "S": "...",
               "T": "-",
               "U": "..-",
               "V": "...-",
               "W": ".--",
               "X": "-..-",
               "Y": "-.--",
               "Z": "--..",
               "0": "-----",
               "1": ".----",
               "2": "..---",
               "3": "...--",
               "4": "....-",
               "5": ".....",
               "6": "-....",
               "7": "--...",
               "8": "---..",
               "9": "----.",
               " ": " / "}

if __name__ == "__main__":
    merged_msg = " ".join(arg.upper() for arg in sys.argv[1:])
    try:
        encoded_msg = ""
        for ch in merged_msg:
            encoded_msg += morse_codes[ch]

        if encoded_msg == "":
            pass
        else:
            print(encoded_msg)

    except Exception:
        sys.stderr.write(f"AssertionError: the arguments are bad\n")
