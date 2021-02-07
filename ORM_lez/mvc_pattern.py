# modelli controller liste sono tre parti distinte di un framework
#leggere le dispense pdf
# model si occupa di lavorare col DB
# controller fa il viglie e gestisce le informazioni per trasformare e inviare alla lista
# la lista si occupa della visualizzaszione delle informazioni 
#che poi inviera' al browser per la visualizzazione
#disaccoppiamento trai componenti  - opgni componente si preoccupa del lavoro e comunica solo i risultati 
#al resto del framework
# la libreria bottle e' tutta in un file che si puo' anche scaricare e utilizzare cosi


from bottle import route, run

@route('/hello')
def hello():
    return "Hello World"

run(host='localhost', port=8099, debug=True)


