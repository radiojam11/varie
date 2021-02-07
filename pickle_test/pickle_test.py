dizionario = {"kiave":"valore", "kiave2": 2}
import pickle
filename = "nome_del_file.p"
with open(filename, "wb") as f:
    pickle.dump(dizionario, f)
