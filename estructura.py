# Diccionari inicial de comandes
comandes = {
    "Anna": [("Llibre", 2, 10.0), ("Bolígraf", 5, 1.5)],
    "Joan": [("Carpeta", 3, 4.5)],
    "Marta": [("Ordinador", 1, 800.0), ("Ratolí", 2, 20.0)]
}

# Funcions

def calcula_cost_total(client):
    """Calcula el cost total de les comandes d'un client."""
    if client in comandes:
        return sum(quantitat * preu_unitari for _, quantitat, preu_unitari in comandes[client])
    else:
        return 0.0

def clients_amb_comandes_superiors_a_100():
    """Llista tots els clients amb comandes superiors a 100 euros."""
    return [client for client in comandes if calcula_cost_total(client) > 100]

def imprimeix_comandes_client(client):
    """Imprimeix les comandes detallades d'un client especificat."""
    if client in comandes:
        print(f"Comandes de {client}:")
        for nom_producte, quantitat, preu_unitari in comandes[client]:
            print(f"- {nom_producte}: {quantitat} unitats a {preu_unitari} €/unitat")
    else:
        print(f"El client '{client}' no té comandes registrades.")

# Menú
while True:
    print("\nMenú de la botiga:")
    print("1. Mostrar el cost total de cada client")
    print("2. Llistar clients amb comandes superiors a 100 euros")
    print("3. Mostrar les comandes d'un client determinat")
    print("4. Sortir")

    opcio = input("Selecciona una opció (1-4): ")

    if opcio == "1":
        print("\nCost total de cada client:")
        for client in comandes:
            cost = calcula_cost_total(client)
            print(f"- {client}: {cost:.2f} €")

    elif opcio == "2":
        print("\nClients amb comandes superiors a 100 euros:")
        clients = clients_amb_comandes_superiors_a_100()
        if clients:
            for client in clients:
                print(f"- {client}")
        else:
            print("No hi ha clients amb comandes superiors a 100 euros.")

    elif opcio == "3":
        nom_client = input("Introdueix el nom del client: ")
        print()
        imprimeix_comandes_client(nom_client)

    elif opcio == "4":
        print("Sortint del programa. Adéu!")
        break

    else:
        print("Opcio invàlida. Si us plau, selecciona una opció entre 1 i 4.")
