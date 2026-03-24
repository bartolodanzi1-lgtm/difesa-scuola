import streamlit as st

# Configurazione minima
st.set_page_config(page_title="Assistente Legale", layout="centered")

st.title("⚖️ Assistente Legale Scuola")
st.write("Inserisci la password nella barra a sinistra per iniziare.")

# --- BARRA LATERALE ---
with st.sidebar:
    st.header("Accesso")
    password = st.text_input("Password Accesso", type="password")

# --- LOGICA PRINCIPALE ---
if password == "Scuola2026":
    st.success("✅ ACCESSO EFFETTUATO")
    
    # Sezione Caricamento (Semplificata)
    st.header("📂 1. Carica Atti")
    st.file_uploader("Trascina qui i tuoi documenti", type=['pdf', 'jpg', 'png'])
    
    st.divider()
    
    # Sezione Dati
    st.header("✍️ 2. Compila la Difesa")
    nome = st.text_input("Tuo Nome e Cognome")
    ruolo = st.selectbox("Tuo Profilo", ["ATA - Collaboratore", "ATA - Assistente", "ATA - DSGA", "Docente"])
    fatti = st.text_area("Racconta i fatti qui sotto:", height=200)

    # Tasto di generazione
    if st.button("✨ MOSTRA TESTO DIFESA"):
        if nome and fatti:
            st.info("Copia il testo qui sotto e incollalo dove desideri:")
            
            # Testo mostrato direttamente a video
            testo_da_copiare = f"""
            AL DIRIGENTE SCOLASTICO
            
            OGGETTO: Memoria difensiva ex art. 55-bis D.Lgs. 165/2001
            
            Il sottoscritto {nome}, in qualità di {ruolo}, 
            con riferimento alla contestazione ricevuta, dichiara quanto segue:
            
            {fatti}
            
            Si richiede l'archiviazione del procedimento.
            """
            
            st.text_area("TESTO PRONTO (Seleziona e Copia):", value=testo_da_copiare, height=300)
            st.balloons()
        else:
            st.warning("⚠️ Per favore, inserisci sia il Nome che i Fatti.")

elif password != "" and password != "Scuola2026":
    st.error("❌ Password errata!")
