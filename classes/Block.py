from classes.Wallet import Wallet
from typing import IO
from classes.Chain import Chain
import hashlib
import json

class Block:
    taille : any
    nom : 00
    parent : 00
    base_hash : any
    hash : any
    parent_hash : any
    transactions : any
    "Element de la blockchain"

def check_hash():
 if hashlib.sha256(Block.base_hash).hexdigest() == Block.hash:
    print("Le Hash est valide")

def add_transaction(expediteur,destinataire,valeur):
    if expediteur == destinataire:
        print("Transaction refusee, l'expéditeur ne peux pas etre le destinataire")
    else:
        Block.transactions = ("Bloc Parent :" + Block.parent + " Expéditeur :" + expediteur + " Destinataire :" + destinataire + " Montant :" + valeur)
        Chain.last_transaction_number +1


def get_transaction():
   if ('./Contest Blockchain\content\blocs' + Block.hash + '.json') != 0:
       x = open('./Contest Blockchain\content\wallets' + Wallet.unique_id + '.json')
    except IOError:
        print("File not accessible")
        finally:
        x.close()

def get_weight():
    weight = Block.taille
    print(weight)

def save():
Block_data = {
  "hash": Block.hash
  }
  save('./Contest Blockchain\content\blocs','bloc',Block_data)

def load():
     filePath = ('./' + 'Contest Blockchain\content\blocs' + '/' + Block.hash + '.json')
     with open(filePath, 'w') as fp:
     f = open(Block.hash + '.json')
     data = json.load(f)
     for i in data['Block_data']:
     print(i)
     f.close
