import os

def main():
    base = input("Nom base (p. ex. Llistat 7.*): ").strip()
    if "*" not in base:
        print("El nom ha de contenir '*' per indicar on va el número.")
        return

    try:
        count = int(input("Quantes repeticions vols? ").strip())
    except ValueError:
        print("Introdueix un número vàlid.")
        return

    for i in range(1, count + 1):
        filename = base.replace("*", str(i))
        if not filename.endswith(".py"):
            filename += ".py"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Fitxer creat automàticament: {filename}\n")

        print(f"Creat {filename}")

if __name__ == "__main__":
    main()