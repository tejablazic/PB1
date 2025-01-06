from model import Stranka, Narocilo

def narocila_stranke():
    stranke = list(Stranka.vse_stranke())
    print('Izberi stranko')
    for i, stranka in enumerate(stranke, 1):
        print(f"{i} {stranka}")
    izbira = int(input("> ")) - 1 # - 1 ker smo začeli štet z 1
    izbrano_ime = stranke[izbira]
    narocila = Narocilo.narocila_stranke(izbrano_ime)
    for i, narocilo in enumerate(narocila, 1):
        print(f'{i} {narocilo.kolicina}')

def narocila_po_kolicini():
    raise NotImplementedError

def pozeni():
    while True:
        print(
            'Izberi možnost:',
            '1 Naročila stranke',
            '2 Naročila po količini:',
            '3 Zaključi', sep = '\n'
        )
        izbira = input('> ')
        if izbira == '1':
            narocila_stranke()
        elif izbira == '2':
            narocila_po_kolicini()
        elif izbira == '3':
            print('Nasvidenje!')
            break

pozeni()