import streamlit as st
from docx import Document
from io import BytesIO

st.set_page_config(page_title="Assistente Legale", layout="centered")
st.title("⚖️ Assistente Legale Scuola")

# --- LOGIN ---
pw = st.sidebar.text_input("Password", type="password")
if pw == "Scuola2026":
    st.sidebar.success("Accesso OK")

    # --- INPUT ---
    nome = st.text_input("Nome e Cognome")
    ruolo = st.selectbox("Profilo", ["ATA - Collaboratore", "ATA - Assistente", "Docente"])
    fatti = st.text_area("Tua difesa (scrivi qui i fatti)", height=200)

    # --- GENERAZIONE ---
    if st.button("PREPARA FILE WORD"):
        if nome and fatti:
            # Creiamo il documento
            doc = Document()
            doc.add_heading('MEMORIA DIFENSIVA', 0)
            doc.add_paragraph(f"Il sottoscritto {nome}, in qualità di {ruolo}, espone:")
            doc.add_paragraph(fatti)
            doc.add_paragraph("\nSi richiede l'archiviazione.")

            # Salvataggio speciale per evitare blocchi
            output = BytesIO()
            doc.save(output)
            output.seek(0)
            
            # MOSTRA IL TASTO DI SCARICAMENTO
            st.download_button(
                label="📥 CLICCA QUI PER SCARICARE IL FILE",
                data=output,
                file_name=f"Difesa_{nome}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("Inserisci Nome e Difesa!")
else:
    st.info("Inserisci la password a sinistra")
