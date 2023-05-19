import sqlite3 

conn =sqlite3.connect('test.db')
cur = conn.cursor()
conn.commit()

"""def create_depensess():
    req="CREATE TABLE depense(id integer primary key, loyer numeric, manger numeric, transport numeric)"
    cur.execute(req)
    conn.commit()
create_depensess()

def create_revenus():
    req="CREATE TABLE revenus(id integer primary key, salaire numeric, business varchar)"
    cur.execute(req)
    conn.commit()
create_revenus()"""

def ajouter_depensess():
    loyer = int(input("Veuillez donner la dépense du loyer : "))
    manger = int(input("Veuillez donner la dépense du manger : "))
    transport = int(input("Veuillez donner la dépense du transport : "))
    req="INSERT INTO depense(loyer, manger, transport) values(?, ?, ?)"
    cur.execute(req,(loyer, manger, transport))
    conn.commit()
ajouter_depensess()

#Inserer pour revenus
salaire = int(input("Veuillez entrer votre salaire : "))
business = int(input("Veuillez indiquer votre revenu business : "))
def ajouter_revenus():
    req="INSERT INTO revenus(salaire, business) values(?, ?)"
    cur.execute(req,(salaire, business))
    conn.commit()
ajouter_revenus()

#execution du depense
def somme_depensess():
    rows = cur.execute("SELECT * FROM depense").fetchall()
    return rows 
depenses = somme_depensess()

#initialisation du montant dépenser
montant_depense = 0
for depense in depenses:
    montant_depense += depense[1]
    
#definition du somme revenus
def somme_revenus():
    rows = cur.execute("SELECT * FROM revenus").fetchall()
    return rows
somme_revenus_resultat = somme_revenus()
revenu_total = somme_revenus_resultat[0][0]
ecart = revenu_total - montant_depense

conn.commit()