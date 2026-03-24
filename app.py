import streamlit as st

st.set_page_config(page_title="Assistente Legale", layout="wide")
st.title("⚖️ Assistente Legale Scuola (Docenti e ATA)")

# --- PASSWORD ---
pw = st.sidebar.text_input("Inserisci Password", type="password")

if pw == "Scuola2026":
    st.sidebar.success("✅ Accesso Autorizzato")
    
    # 1. CARICAMENTO ATTI
    st.header("📂 1. Carica gli Atti (Foto/PDF)")
    st.file_uploader("Trascina qui i documenti per riferimento", accept_multiple_files=True)
    
    st.divider()

    # 2. COMPILAZIONE
    st.header("✍️ 2. Scrivi la tua Difesa")
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome")
        profilo = st.selectbox("Tuo Profilo:", ["-- Seleziona --", "ATA - Collaboratore", "ATA - Assistente", "ATA - DSGA", "Docente"])
    with col2:
        scuola = st.text_input("Istituto Scolastico")
    
    fatti = st.text_area("Racconta i fatti e le tue ragioni:", height=200)

    # 3. GENERAZIONE TESTO (VISIBILE SUBITO)
    if st.button("✨ CLICCA QUI PER GENERARE IL TESTO"):
        if nome and fatti and profilo != "-- Seleziona --":
            st.success("✅ Ecco la tua bozza! Copia questo testo e incollalo in un file Word o in una mail:")
            
            testo_pronto = f"""
            AL DIRIGENTE SCOLASTICO DEL: {scuola}
            
            OGGETTO: Memoria difensiva ex art. 55-bis D.Lgs. 165/2001
            
            Il/La sottoscritto/a {nome}, profilo {profilo}, 
            in relazione alla contestazione ricevuta, espone quanto segue:
            
            DIFESA E FATTI:
            {fatti}
            
            CONCLUSIONI:
            Si richiede l'archiviazione del procedimento disciplinare.
            """
            # Questo crea il riquadro nero con il testo pronto
            st.code(testo_pronto, language="text")
            st.balloons()
        else:
            st.error("⚠️ Compila tutti i campi prima di cliccare!")
else:
    st.info("Inserisci la password 'Scuola2026' nella barra a sinistra.")
