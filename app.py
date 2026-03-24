import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Assistente Legale", layout="wide")
st.title("⚖️ Assistente Legale Scuola - Generatore di Testo")

# --- LOGIN ---
password = st.sidebar.text_input("Password", type="password")

if password == "Scuola2026":
    st.sidebar.success("Accesso OK")
    
    # 1. CARICAMENTO ATTI (Sempre visibile)
    st.header("📂 1. Carica Atti (Foto/PDF)")
    st.file_uploader("Trascina qui i documenti del procedimento", accept_multiple_files=True)
    
    st.divider()

    # 2. DATI
    st.header("✍️ 2. Compila la tua Difesa")
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome")
        profilo = st.selectbox("Profilo", ["ATA - Collaboratore", "ATA - Assistente", "ATA - DSGA", "Docente"])
    with col2:
        scuola = st.text_input("Istituto Scolastico")
        data_c = st.date_input("Data della contestazione")

    fatti = st.text_area("Scrivi qui la tua versione dei fatti:", height=200)

    # 3. RISULTATO A VIDEO (Niente più file esterni)
    if st.button("✨ GENERA TESTO DIFESA"):
        if nome and fatti and scuola:
            st.success("✅ Ecco la tua bozza pronta! Copia il testo qui sotto:")
            
            # Creazione del blocco di testo visibile
            testo_finale = f"""
            AL DIRIGENTE SCOLASTICO DEL: {scuola}
            UFFICIO PROCEDIMENTI DISCIPLINARI
            
            OGGETTO: Memoria difensiva ex art. 55-bis D.Lgs. 165/2001
            
            Il/La sottoscritto/a {nome}, in servizio presso codesto Istituto 
            con il profilo di {profilo}, in relazione alla contestazione 
            prot. del {data_c}, espone quanto segue:
            
            ESPOSIZIONE DEI FATTI:
            {fatti}
            
            CONCLUSIONI:
            Si richiede l'archiviazione del procedimento disciplinare.
            
            Data: {datetime.now().strftime("%d/%m/%Y")}
            Firma: ___________________________
            """
            
            # Mostra il testo in un riquadro pronto per il Copia/Incolla
            st.code(testo_finale, language="text")
            st.balloons()
        else:
            st.error("⚠️ Compila tutti i campi prima di generare!")

else:
    st.info("Inserisci la password 'Scuola2026' a sinistra.")
