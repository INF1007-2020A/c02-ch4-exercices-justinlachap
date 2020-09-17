import random

def is_even_len(string):
    if len(string)%2==0:
        return True
    else:
        return False


def get_num_char(string, char):
    counter = 0
    for i in string:
        if i==char:
            counter += 1
    return counter


def get_first_part_of_name(name):
    s = ''
    for i in name:
        if i == '-':
            break
        s+= i
    s=s.capitalize()
    return s


def get_random_sentence(animals, adjectives, fruits):
    animals_list = [str(i) for i in animals]
    adjectives_list = [str(i) for i in adjectives]
    fruits_list = [str(i) for i in fruits]
    return 'Aujourd’hui, j’ai vu un ' + random.choice(animals_list)+ ' s’emparer d’un panier '+ random.choice(adjectives)+ ' plein de '+random.choice(fruits)+'.'


if __name__ == "__main__":
    spam = "Bonjour!"
    if is_even_len(spam)==True:
        parity = 'pair'
    else:
        parity = "impair"
    print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

    eggs = "Hello, world!"
    print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

    parrot = "jean-marc"
    print('Bonjour ' + get_first_part_of_name(parrot))

    animals = ("chevreuil", "chien", "pigeon")
    adjectives = ("rouge", "officiel", "lourd")
    fruits = ("pommes", "kiwis", "bananes")
    print(get_random_sentence(animals, adjectives, fruits))
