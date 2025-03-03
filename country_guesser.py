##
## CELIAN SIAMPIRAVE, 2025
## CountryGuesser
## File description:
## country_guesser
##

from colorama import Fore


countries = {
    "Afghanistan", "Albanie", "Algérie", "Andorre", "Angola", "Antigua-et-Barbuda",
    "Argentine", "Arménie", "Australie", "Autriche", "Azerbaïdjan", "Bahamas", "Bahreïn",
    "Bangladesh", "Barbade", "Biélorussie", "Belgique", "Belize", "Bénin", "Bhoutan", "Bolivie",
    "Bosnie-Herzégovine", "Botswana", "Brésil", "Brunéi", "Bulgarie", "Burkina Faso",
    "Burundi", "Cap-Vert", "Cambodge", "Cameroun", "Canada", "République centrafricaine",
    "Tchad", "Chili", "Chine", "Colombie", "Comores", "Congo", "Costa Rica", "Croatie",
    "Cuba", "Chypre", "Tchéquie", "République démocratique du Congo", "Danemark", "Djibouti",
    "Dominique", "République dominicaine", "Équateur", "Égypte", "Salvador", "Guinée équatoriale",
    "Érythrée", "Estonie", "Eswatini", "Éthiopie", "Fidji", "Finlande", "France", "Gabon",
    "Gambie", "Géorgie", "Allemagne", "Ghana", "Grèce", "Grenade", "Guatemala", "Guinée",
    "Guinée-Bissau", "Guyana", "Haïti", "Honduras", "Hongrie", "Islande", "Inde", "Indonésie",
    "Iran", "Irak", "Irlande", "Israël", "Italie", "Côte d'Ivoire", "Jamaïque", "Japon", "Jordanie",
    "Kazakhstan", "Kenya", "Kiribati", "Koweït", "Kirghizistan", "Laos", "Lettonie", "Liban",
    "Lesotho", "Libéria", "Libye", "Liechtenstein", "Lituanie", "Luxembourg", "Madagascar",
    "Malawi", "Malaisie", "Maldives", "Mali", "Malte", "Îles Marshall", "Mauritanie",
    "Maurice", "Mexique", "Micronésie", "Moldavie", "Monaco", "Mongolie", "Monténégro",
    "Maroc", "Mozambique", "Birmanie", "Namibie", "Nauru", "Népal", "Pays-Bas",
    "Nouvelle-Zélande", "Nicaragua", "Niger", "Nigéria", "Corée du Nord", "Macédoine du Nord",
    "Norvège", "Oman", "Pakistan", "Palaos", "Palestine", "Panama", "Papouasie-Nouvelle-Guinée",
    "Paraguay", "Pérou", "Philippines", "Pologne", "Portugal", "Qatar", "Roumanie", "Russie",
    "Rwanda", "Saint-Christophe-et-Niévès", "Sainte-Lucie", "Saint-Vincent-et-les-Grenadines",
    "Samoa", "Saint-Marin", "Sao Tomé-et-Principe", "Arabie Saoudite", "Sénégal", "Serbie",
    "Seychelles", "Sierra Leone", "Singapour", "Slovaquie", "Slovénie", "Îles Salomon",
    "Somalie", "Afrique du Sud", "Corée du Sud", "Soudan du Sud", "Espagne", "Sri Lanka",
    "Soudan", "Suriname", "Suède", "Suisse", "Syrie", "Tadjikistan", "Tanzanie",
    "Thaïlande", "Timor oriental", "Togo", "Tonga", "Trinité-et-Tobago", "Tunisie",
    "Turquie", "Turkménistan", "Tuvalu", "Ouganda", "Ukraine", "Émirats arabes unis",
    "Royaume-Uni", "États-Unis", "Uruguay", "Ouzbékistan", "Vanuatu", "Vatican",
    "Venezuela", "Vietnam", "Yémen", "Zambie", "Zimbabwe"
}

def play():
    guessed = set()

    print(Fore.WHITE + "Essayez de trouver les 196 pays du monde ! Tapez 'exit' pour quitter.")
    print("-Pour qu'un pays soit correct, vous devez le tapez en commençant par une majuscule-\n")

    while len(guessed) < 196:
        guess = input(Fore.BLACK + "Pays trouvés : {} /196. Entrez un pays : " .format(len(guessed)))
        if guess == "exit":
            break
        if guess in countries and guess not in guessed:
            guessed.add(guess)
            print(Fore.GREEN + "Correct ! {} restants." .format(196 - len(guessed)))
        elif guess in guessed:
            print(Fore.LIGHTYELLOW_EX + "Ce pays a déjà été trouvé.")
        elif guess == "found":
            print(Fore.CYAN + str(guessed))
        else:
            print(Fore.RED + "Ceci n'est pas un pays. Essayez encore !")

play()