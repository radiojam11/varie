import streamlit as st
import pandas as pd


def download_covid_csv():
    import requests
    resp = requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/legacy/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    with open("data/covid.csv", "w+") as fd:
        fd.write(resp.text)


if __name__ == "__main__":
    download_covid_csv()
    with open("data/covid.csv") as fd:
        df = pd.read_csv(fd)
    #cols = ['totale_positivi', 'terapia_intensiva', 'totale_casi']
    #cols = ['data','stato','ricoverati_con_sintomi','terapia_intensiva','totale_ospedalizzati','isolamento_domiciliare','totale_positivi','variazione_totale_positivi','nuovi_positivi','dimessi_guariti','deceduti','totale_casi','tamponi','casi_testati','note_it,note_en']
    cols =['tamponi', 'terapia_intensiva', ]
    df_chart = df.filter(items=cols)
    st.header("COVID-19 TRENDS")
    st.table(df_chart)
    CHART_TYPE = {"line": 0, "area": 1, "bar": 2}
    opts = list(CHART_TYPE.keys())
    chart_type = st.sidebar.selectbox("Select chart type", opts)
    chart = None
    if CHART_TYPE[chart_type] == 0:
        chart = st.line_chart
    elif CHART_TYPE[chart_type] == 1:
        chart = st.area_chart
    elif CHART_TYPE[chart_type] == 2:
        chart = st.bar_chart
    chart(df_chart)
