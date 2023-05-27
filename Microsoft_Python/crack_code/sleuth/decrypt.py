def lasso_letter(letter, shift_amount):
    # Pre set values
    a_ascii = ord('a')
    alphabet_size = 26

    # getting true letter
    ascii_code = ord(letter.lower())
    true_number = a_ascii + (((ascii_code - a_ascii) + shift_amount) % alphabet_size)
    true_letter = chr(true_number)
    return true_letter

def lasso_word(word, shift_amount):
    true_meaning = ''
    for letter in word:
        true_meaning += lasso_letter(letter, shift_amount)
    return true_meaning

def lasso_message(secret_message):
    message = secret_message.strip()
    secret_lines = message.split("\n")
    decoded_message = ""
    separator = ''
    for element in secret_lines:
        clean_element = element.strip()
        parts = clean_element.split(':')
        word = parts[0]
        shift_amount = int(parts[1])
        line_decoded = lasso_word(word, shift_amount)
        decoded_message = decoded_message + separator + line_decoded
        separator = '\n'
    return decoded_message

def main():
    encoded_message = """
    Ncevy:13
    gpvsui:25
    ugflgkg:-18
    wjmmf:-1
    """
    print(lasso_message(encoded_message))

if __name__ == "__main__":
    main()