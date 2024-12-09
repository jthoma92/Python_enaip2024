class Ristorante:
    """Class per modellare un ristorante con menu e ordini"""

    def __init__(self, nome, tipo_di_risto):
        self.nome = nome
        self.tipo_di_risto = tipo_di_risto
        self.menu = {}  #da definire qui per evitare problemi di mutabilità, e dati condivisi tra oggetti 
    
    def mostrare_nome(self):
        """Mostrare solo il nome del ristorante"""
        print(f"Il ristorante si chiama {self.nome}")

   # def tipo_di_ristorante(self):


risto1 = Ristorante("da john", "bbq steakhouse")

risto2 = Ristorante("da lin", "cinese")

risto1.menu["item1"] = "fish"
print(f"primo risto menu: {risto1.menu}")
print(f"secondo risto menu: {risto2.menu}")