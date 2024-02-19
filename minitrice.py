#!/usr/bin/env python3

def main():
    print("Bienvenue dans minitrice!")
    
    while True:
        try:
            user_input = input("> ")
            
            if not user_input:
                break  # Sortir si la ligne est vide
            
            result = eval(user_input)
            print(result)
            
        except Exception as e:
            print(f"Erreur de calcul: {str(e)}")

    print("Fin des calculs :)")
    
if __name__ == "__main__":
    main()
