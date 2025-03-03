##
## CELIAN SIAMPIRAVE, 2025
## CountryGuesser
## File description:
## country_guesser
##

from colorama import Fore

countries = {
    "afghanistan", "albanie", "algérie", "andorre", "angola", "antigua-et-barbuda",
    "argentine", "arménie", "australie", "autriche", "azerbaïdjan", "bahamas", "bahreïn",
    "bangladesh", "barbade", "biélorussie", "belgique", "belize", "bénin", "bhoutan", "bolivie",
    "bosnie-herzégovine", "botswana", "brésil", "brunéi", "bulgarie", "burkina faso",
    "burundi", "cap-vert", "cambodge", "cameroun", "canada", "république centrafricaine",
    "tchad", "chili", "chine", "colombie", "comores", "congo", "costa rica", "croatie",
    "cuba", "chypre", "tchéquie", "république démocratique du congo", "danemark", "djibouti",
    "dominique", "république dominicaine", "équateur", "égypte", "salvador", "guinée équatoriale",
    "érythrée", "estonie", "eswatini", "éthiopie", "fidji", "finlande", "france", "gabon",
    "gambie", "géorgie", "allemagne", "ghana", "grèce", "grenade", "guatemala", "guinée",
    "guinée-bissau", "guyana", "haïti", "honduras", "hongrie", "islande", "inde", "indonésie",
    "iran", "irak", "irlande", "israël", "italie", "côte d'ivoire", "jamaïque", "japon", "jordanie",
    "kazakhstan", "kenya", "kiribati", "koweït", "kirghizistan", "laos", "lettonie", "liban",
    "lesotho", "libéria", "libye", "liechtenstein", "lituanie", "luxembourg", "madagascar",
    "malawi", "malaisie", "maldives", "mali", "malte", "îles marshall", "mauritanie",
    "maurice", "mexique", "micronésie", "moldavie", "monaco", "mongolie", "monténégro",
    "maroc", "mozambique", "birmanie", "namibie", "nauru", "népal", "pays-bas",
    "nouvelle-zélande", "nicaragua", "niger", "nigéria", "corée du nord", "macédoine du nord",
    "norvège", "oman", "pakistan", "palaos", "palestine", "panama", "papouasie-nouvelle-guinée",
    "paraguay", "pérou", "philippines", "pologne", "portugal", "qatar", "roumanie", "russie",
    "rwanda", "saint-christophe-et-nièves", "sainte-lucie", "saint-vincent-et-les-grenadines",
    "samoa", "saint-marin", "sao tomé-et-principe", "arabie saoudite", "sénégal", "serbie",
    "seychelles", "sierra leone", "singapour", "slovaquie", "slovénie", "îles salomon",
    "somalie", "afrique du sud", "corée du sud", "soudan du sud", "espagne", "sri lanka",
    "soudan", "suriname", "suède", "suisse", "syrie", "tadjikistan", "tanzanie",
    "thaïlande", "timor oriental", "togo", "tonga", "trinité-et-tobago", "tunisie",
    "turquie", "turkménistan", "tuvalu", "ouganda", "ukraine", "émirats arabes unis",
    "royaume-uni", "états-unis", "uruguay", "ouzbékistan", "vanuatu", "vatican",
    "venezuela", "vietnam", "yémen", "zambie", "zimbabwe"
}


def play():
    guessed = set()

    print(Fore.WHITE + "Essayez de trouver les 196 pays du monde ! Tapez 'exit' pour quitter.")
    print("-Pour qu'un pays soit correct, vous devez le tapez en commençant par une majuscule-\n")

    while len(guessed) < 196:
        guess = input(Fore.MAGENTA + "Pays trouvés : {} /196. Entrez un pays : " .format(len(guessed)))

        guess_lower = guess.lower()
        if guess == "exit":
            print("Vous avez trouvé {} pays !" .format(len(guessed)))
            break
        if guess_lower in countries and guess_lower not in guessed:
            guessed.add(guess_lower)
            print(Fore.GREEN + "Correct ! {} restants." .format(196 - len(guessed)))
        elif guess_lower in guessed:
            print(Fore.LIGHTYELLOW_EX + "Ce pays a déjà été trouvé.")
        elif guess == "found":
            print(Fore.CYAN + str(guessed))
        else:
            print(Fore.RED + "Ceci n'est pas un pays. Essayez encore !")

play()
