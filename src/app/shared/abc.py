
def main():
    with open(f"src/app/shared/smoking_joe.txt", 'r') as f:
        frases = [frase[:len(frase)-1] for frase in f.readlines()]
        f.close()
        print(frases)
    pass

if __name__ == "__main__":
    main()