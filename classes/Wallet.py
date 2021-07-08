from typing import Any
import uuid
import json
class Wallet:
    unique_id: Any
    balance = 0.0
    history: Any
    "Portefeuille de l'utilisateur"

e1 = Wallet()
wallet_id = getattr(e1,'unique_id')
balance = getattr(e1,'balance')
history = getattr(e1,'history')

def generate_unique_id():
  Wallet.unique_id = uuid.uuid4()
  wallet_id = Wallet.unique_id
  print (Wallet.unique_id)
  x = open('./Contest Blockchain\content\wallets' + wallet_id + '.json')
  except IOError:
    print("File not accessible")
    finally:
    x.close()
 


def add_balance():
    print ("Veuillez entrer le montant a ajouter: ")
    montant = input()
    print ("Votre Wallet contient maintenant", Wallet.balance + montant,"$")

def sub_balance():
    print ("Veuillez entrer le montant a déduire: ")
    montant2 = input()
    print ("Votre Wallet contient maintenant", Wallet.balance - montant2,"$")

def send():
    pass

def save():
Wallet_data = {
  "id": wallet_id,
  "balance": balance,
  "history": history,
  }
  save('./','wallet_id',Wallet_data)

def load():
    filePath = ('./' + 'Contest Blockchain\content\wallets' + '/' + wallet_id + '.json')
    with open(filePath, 'w') as fp:
    f = open(wallet_id + '.json')
    data = json.load(f)
    for i in data['Wallet_data']:
    print(i)
    f.close

    