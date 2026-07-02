#accept one character and check whether its vowel or consonent
def CheckVowelConsonent(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print("Vowel")
    else:
        print("Consonant")

def main():
    inputchar = input("Enter a character: ")
    CheckVowelConsonent(inputchar)      

if __name__ == "__main__":
    main()