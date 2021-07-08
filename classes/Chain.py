from classes.Block import Block, get_transaction
import hashlib
import random
import string

class Chain:
    blocks : any
    last_transaction_number : 0
    "Ensemble de la chaine"

def generate_hash():
    letter_chain = string.ascii_letters
    random_chain = (random.choice(letter_chain) for i in range(random))
    hash = hashlib.sha256(random_chain.encode()).hexdigest()
    return hash

def verify_hash():
    if (('./Contest Blockchain\content\blocs' + hash + '.json') != 0) and (hash.startswith('0000')):
     print("Un hash valide a été trouvé")

def add_block():
    hash = Block.hash
    from Block import save()

def add_transaction():
    hash = Block.hash
    from Block import add_transaction()

def new_transaction(expediteur, destinataire, montant):
    transaction = {
        'expediteur': expediteur,
        'destinataire': destinataire,
        'montant': montant
    }
    from Block import add_transaction():

def find_transaction():
    print('Entrer le numero de transaction du bloc')
    x = input()
    get_transaction(x == Block.hash)
    return Block

def get_last_transaction_number():
    last_transaction = Chain.last_transaction_number #Incrémentation du numéro de transaction directement a la création du bloc dans l'objet Chain
    print(last_transaction)

    
