import re

max_len = 20 

def rozdelenie1(text, max_len: int):
    
    words = re.findall(r'\S+', text)
    lines = []      #Inicializuje prázdny zoznam, do ktorého sa budú pridávať výsledné riadky.
    buffer = ""   #Pomocná premená, ktorá dočasne ukladá text jedného riadku, kým sa neuloží do lines.

    i = 0
    while i < len(words):
        word = words[i]

        if len(word) <= max_len:
            # 1 Prípad: Slovo sa zmestí do riadku
            if buffer:
                space_left = max_len - len(buffer) - 1
                if len(word) + 1 <= space_left:
                    buffer += ' ' + word
                    i += 1
                elif space_left >= 3:
                    buffer += ' ' + word[:space_left]
                    words[i] = word[space_left:]  
                    lines.append(buffer)
                    buffer = ""
                else:
                    lines.append(buffer)
                    buffer = ""
            else:
                if len(word) <= max_len:
                    buffer = word
                    i += 1
        else:
            # 2 Prípad: Slovo je dlhšie ako max_len
            if buffer:
                space_left = max_len - len(buffer) - 1
                if space_left >= 3:
                    buffer += ' ' + word[:space_left]
                    word = word[space_left:]
                lines.append(buffer)
                buffer = ""
            # Rozdelenie zvyšku dlhého slova
            while len(word) > max_len:
                lines.append(word[:max_len])
                word = word[max_len:]
            if word:
                buffer = word
            i += 1

    if buffer:
        lines.append(buffer)   # kontrola/ pridanie posledného riadku

    return lines

# Testovanie
text1 = "zodpovedná riešiteľka: prof. Ing. Zlatica Muchová"
text2 = "zodpovedná riešiteľkadfdfdfdffddf: prof. Ing. Zlatica Muchová"

result1 = rozdelenie1(text1, 20)
for line in result1:
    print(line)

print("")

result2 = rozdelenie1(text2, 20)
for line in result2:
    print(line)

