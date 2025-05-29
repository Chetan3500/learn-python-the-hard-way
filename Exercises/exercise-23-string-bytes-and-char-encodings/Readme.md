# String, Bytes and Character encoding

- String - collection of letter(s).
- Bytes - a sequence of 8 bits.
- Bits - 1 and 0.
- Character - aka letter.
- Encoding - converting characters (like letters, symbols, emojis) into bytes so a computer can store or process them.

The convention for Encoding text in python is caled "UTF-8", aka Unicode Transformation Format 8 bits. There are also UTF-16, UTF-32 and big5(Non-unicode for Traditional Chinese).

## Exercise

1. Download [language.txt](./language.txt) file.
2. Create ex23.py and write the following:
    ```py
    import sys

    script, input_encoding, error = sys.argv

    def main(language_file, encoding, errors):
        line = language_file.readline()
        if line:
            print_line(line, encoding, errors)
            return main(language_file, encoding, errors)

    def print_line(line, encoding, errors):
        next_lang = line.strip()
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<===>", cooked_string)

    languages = open("languages.txt", encoding="utf-8")

    main(languages, input_encoding, error)
    ```
3. Run script, `python ex23.py utf-8 strict`.
4. Output be:
    ```
    b'Afrikaans' <===> Afrikaans
    b'\xe1\x8a\xa0\xe1\x88\x9b\xe1\x88\xad\xe1\x8a\x9b' <===> አማርኛ
    b'\xd0\x90\xd2\xa7\xd1\x81\xd1\x88\xd3\x99\xd0\xb0' <===> Аҧсшәа
    b'\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xa9' <===> العربية
    b'Aragon\xc3\xa9s' <===> Aragonés
    b'Arpetan' <===> Arpetan
    b'Az\xc9\x99rbaycanca' <===> Azərbaycanca
    b'Bamanankan' <===> Bamanankan
    b'\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe' <===> বাংলা
    b'B\xc3\xa2n-l\xc3\xa2m-g\xc3\xba' <===> Bân-lâm-gú
    b'\xd0\x91\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f' <===> Беларуская
    ```

# Noted

If you have raw bytes, then you must use .decode() to get the string. Raw bytes have no convention to them. Remember the mnemonic DBES, which stands for Decode Bytes, Encode Strings. For more info check `pydoc3.x str.encode`, `pydoc3.x str.decode`, etc.

