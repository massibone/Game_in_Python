import pygame
import os
import random

# Inizializzazione di Pygame
pygame.init()

# Definizione dei colori
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

# Definizione delle dimensioni della finestra di gioco
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definizione delle dimensioni delle carte
CARD_WIDTH = 50
CARD_HEIGHT = 70

# Definizione del percorso della cartella delle carte
percorso_carte = "cards"

# Caricamento dei nomi delle carte dalla cartella
nomi_carte = [nome_file for nome_file in os.listdir(percorso_carte) if nome_file.endswith(".png")]
#print(nomi_carte)
# Caricamento delle immagini delle carte
card_images = {nome_carta: pygame.image.load(os.path.join(percorso_carte, nome_carta)) for nome_carta in nomi_carte}
#print(card_images)

# Creazione della finestra di gioco
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Burraco")

# Classe per rappresentare una carta
class Carta:
    def __init__(self, nome_immagine):
        self.image = card_images[nome_immagine]

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
print(Carta)

# Funzione per creare un mazzo di carte
def crea_mazzo():
    mazzo = []
    semi = ['clubs', 'diamonds', 'hearts', 'spades']
    valori = ['A', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K']
    
    for seme in semi:
        for valore in valori:
            nome_carta = f"card_{seme.lower()}_{valore}.png"
            carta = Carta(nome_carta)
            mazzo.append(carta)
    
    return mazzo

# Funzione per mescolare il mazzo di carte
def mischia_mazzo(mazzo):
    random.shuffle(mazzo)

# Funzione per distribuire le carte ai giocatori
def distribuisci_carte(mazzo, giocatori):
    """
    Distribuisce le carte ai giocatori dal mazzo.

    Parametri:
    - mazzo: lista delle carte da cui distribuire
    - giocatori: lista dei giocatori a cui distribuire le carte
    """
    for _ in range(11):
        for giocatore in giocatori:
            giocatore.aggiungi_carta(mazzo.pop())

# Classe per rappresentare un giocatore
class Giocatore:
    def __init__(self, x, y):
        """
        Inizializza un giocatore con la posizione della mano.

        Parametri:
        - x: coordinata x della mano del giocatore
        - y: coordinata y della mano del giocatore
        """
        self.x = x
        self.y = y
        self.mano = []

    def aggiungi_carta(self, carta):
        """
        Aggiunge una carta alla mano del giocatore.

        Parametri:
        - carta: carta da aggiungere alla mano del giocatore
        """
        self.mano.append(carta)

    def draw(self, screen):
        """
        Disegna la mano del giocatore sullo schermo.

        Parametri:
        - screen: oggetto Surface su cui disegnare la mano del giocatore
        """
        for i, carta in enumerate(self.mano):
            carta.draw(screen, self.x + i * (CARD_WIDTH + 10), self.y)


# Funzione per il loop del gioco
def main():
    clock = pygame.time.Clock()

    # Creazione dei giocatori
    giocatori = [Giocatore(50, 450), Giocatore(50, 50)]

    # Creazione e mescolamento del mazzo
    mazzo = crea_mazzo()
    mischia_mazzo(mazzo)

    # Distribuzione delle carte ai giocatori
    distribuisci_carte(mazzo, giocatori)

    # Loop principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Disegno delle carte dei giocatori
        for giocatore in giocatori:
            giocatore.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
from collections import Counter

def trova_combinazioni_valide(mano):
    # Conteggio delle carte per valore
    conteggio_carte = Counter(mano)
    
    # Inizializzazione liste per tris e scale
    tris = []
    scale = []
    
    # Funzione per trovare tris minimi
    def trova_tris(conteggio_carte):
        return [valore for valore, conteggio in conteggio_carte.items() if conteggio >= 3]
    
    # Funzione per trovare scale
    def trova_scale(conteggio_carte):
        valori = sorted(conteggio_carte.keys(), key=lambda x: int(x) if x.isdigit() else 0)
        scale = []
        for valore in valori:
            if valore.isdigit():
                valore_int = int(valore)
                if str(valore_int + 1) in valori and str(valore_int + 2) in valori:
                    scale.append([str(valore_int), str(valore_int + 1), str(valore_int + 2)])
        return scale
    
    # Trova tris e scale
    tris = trova_tris(conteggio_carte)
    scale = trova_scale(conteggio_carte)
    
    # Restituisce tris e scale trovate
    return tris, scale

# Funzione per aggiungere jolly a combinazioni
def aggiungi_jolly(combinazioni, jolly):
    combinazioni_con_jolly = []
    for combinazione in combinazioni:
        # Trova quante carte jolly sono necessarie per completare la combinazione
        carte_mancanti = 3 - len(combinazione)
        if jolly >= carte_mancanti:
            combinazione_con_jolly = combinazione + ['jolly'] * carte_mancanti
            combinazioni_con_jolly.append(combinazione_con_jolly)
            jolly -= carte_mancanti
    return combinazioni_con_jolly

# Esempio di utilizzo
mano_giocatore = ['2', '3', '4', '5', '6', '7', 'Asso', 'Asso', 'Asso', 'Re', 'Re', 'Re']
jolly_disponibili = 2  # Numero di jolly disponibili nella mano del giocatore

tris, scale = trova_combinazioni_valide(mano_giocatore)
scale_con_jolly = aggiungi_jolly(scale, jolly_disponibili)

print("Tris trovati:", tris)
print("Scale trovate:", scale_con_jolly)

if __name__ == "__main__":
    main()
