if __name__ == "__main__":
    from models import *
    
    player1_name = input("Inserisci il nome del primo giocatore:\n")
    player2_name = input("Inserisci il nome del secondo giocatore:\n")
    
    tris_game = Tris(player1_name, player2_name)
    
    should_end = False
    while not should_end:
        turn = input(f"E' il turno di {tris_game.playing_player.name}: ")
        if len(turn) != 2:
            print("Inserimento non valido. Ripetere.")
            continue
        nrow = int(turn[0])
        ncol = int(turn[1])
        res = tris_game.play_turn(nrow, ncol)
        print(tris_game.grid)
        if res is None:
            continue
        elif res == False:
            print("Inserimento non valido. Ripetere.")
        elif isinstance(res, Player):
            s1 = tris_game.player1.score
            s2 = tris_game.player2.score
            print(f"Ha vinto il giocatore: {res.name}! Punteggio: {s1} a {s2}")
            new_game = input("Vuoi giocare una nuova partita? [S] [N]\n")
            if new_game == "S":
                continue
            should_end = True
        else:
            print("La partita è finita in pareggio")
            should_end = True