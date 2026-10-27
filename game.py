import streamlit as st
import time
from streamlit_autorefresh import st_autorefresh

# --- EWIGEN TROPHÄENSCHRANK INITIALISIEREN (KORREKTUR) ---
# Diese Variablen prüfen wir einzeln, damit sie NIEMALS überschrieben werden
if "trophäe_einfach" not in st.session_state:
    st.session_state.trophäe_einfach = False
if "trophäe_mittel" not in st.session_state:
    st.session_state.trophäe_mittel = False
if "trophäe_schwer" not in st.session_state:
    st.session_state.trophäe_schwer = False
if "trophäe_ultra" not in st.session_state:
    st.session_state.trophäe_ultra = False
if "kekstrophäe_freigeschaltet" not in st.session_state:
    st.session_state.kekstrophäe_freigeschaltet = False

# --- NORMALEN SPIELSTAND INITIALISIEREN ---
if "Geld" not in st.session_state:
    st.session_state.Geld = 0.0
    st.session_state.geldProKlick = 1.0
    st.session_state.upgradeKosten = 10
    st.session_state.klickMultiplikator = 1.0
    st.session_state.multiKosten = 50
    st.session_state.anzahlAutoclicker = 0
    st.session_state.autoclickerKosten = 1000
    
    # Variablen für das Tempo-Upgrade
    st.session_state.autoclickerZeit = 1.0
    st.session_state.tempoUpgradeKosten = 500
    st.session_state.anzahlTempoUpgrades = 0
    
    # Schwierigkeit-Speicher
    st.session_state.schwierigkeit_gewaehlt = False
    st.session_state.ziel_summe = 1000000
    st.session_state.modus_name = "Mittel"
    
    st.session_state.letztes_update = time.time()

# --- 1. HAUPTMENÜ ---
if not st.session_state.schwierigkeit_gewaehlt:
    st.title("Willkommen bei Money Clicker")
    
    st.markdown("### Schwierigkeit wählen")
    st.write("Wähle einen Modus, um das Spiel zu starten:")
    
    if st.button("Einfach (Ziel: 100.000 Geld)", use_container_width=True):
        st.session_state.ziel_summe = 100000
        st.session_state.modus_name = "Einfach"
        st.session_state.schwierigkeit_gewaehlt = True
        st.session_state.letztes_update = time.time()
        st.rerun()
        
    if st.button("Mittel (Ziel: 1.000.000 Geld)", use_container_width=True):
        st.session_state.ziel_summe = 1000000
        st.session_state.modus_name = "Mittel"
        st.session_state.schwierigkeit_gewaehlt = True
        st.session_state.letztes_update = time.time()
        st.rerun()
        
    if st.button("Schwer (Ziel: 1.000.000.000 Geld)", use_container_width=True):
        st.session_state.ziel_summe = 1000000000
        st.session_state.modus_name = "Schwer"
        st.session_state.schwierigkeit_gewaehlt = True
        st.session_state.letztes_update = time.time()
        st.rerun()
        
    st.write("---")
    code_eingabe = st.text_input("Geheimcode eingeben:", type="password")
    if code_eingabe == "Skyfall":
        st.success("ULTRA-SCHWER FREIGESCHALTET!")
        if st.button("Starte Ultra-Schwer (Ziel: 1.000.000.000.000 Geld)", use_container_width=True):
            st.session_state.ziel_summe = 1000000000000
            st.session_state.modus_name = "ULTRA-SCHWER"
            st.session_state.schwierigkeit_gewaehlt = True
            st.session_state.letztes_update = time.time()
            st.rerun()

    st.write("---")
    st.subheader("Rätsel-Herausforderung")
    st.write("Löse alle 3 Rätsel für die Keks-Trophäe!")
    
    antwort1 = st.text_input("Wie heißt der Zug eines schwarzen Bauern welcher einen weißen Bauern schlägt, wenn dieser von der Grundreihe auf dieselbe Reihe wie der schwarze Bauer gezogen ist im Schach", key="r1")
    r1_richtig = antwort1.strip().lower() in ["en passant", "enpassant"]
    
    antwort2 = st.text_input("Wie lautet der Endtsand des Champions-League Finale 1999", key="r2")
    r2_richtig = antwort2.strip().lower() in ["2-1", "2:1"]
    
    antwort3 = st.text_input("Was ist das hier --> | (englischer Name)", key="r3")
    r3_richtig = antwort3.strip().lower() in ["pipe", "pipe symbol", "vertical bar"]
    
    if r1_richtig and r2_richtig and r3_richtig:
        if not st.session_state.kekstrophäe_freigeschaltet:
            st.session_state.kekstrophäe_freigeschaltet = True
            st.balloons()
            st.rerun()

    st.write("---")
    st.markdown("Trophäenschrank")
    st.write("Deine Meilensteine:")
    
    t_col1, t_col2, t_col3, t_col4, t_col5 = st.columns(5)
    
    with t_col1:
        if st.session_state.kekstrophäe_freigeschaltet:
            st.info("🍪 **Rätsel-Keks**\n*(Rätsel gelöst)*")
        else:
            st.text("🔒 🍪 (Rätsel)")
            
    with t_col2:
        if st.session_state.trophäe_einfach:
            st.success("🥉 **Bronze-Pokal**\n*(Einfach)*")
        else:
            st.text("🔒 🥉 (Einfach)")
            
    with t_col3:
        if st.session_state.trophäe_mittel:
            st.warning("🥈 **Silber-Pokal**\n*(Mittel)*")
        else:
            st.text("🔒 🥈 (Mittel)")
            
    with t_col4:
        if st.session_state.trophäe_schwer:
            st.error("🥇 ⭐ **Gold-Pokal**\n*(Schwer)*")
        else:
            st.text("🔒 🥇 (Schwer)")
            
    with t_col5:
        if st.session_state.trophäe_ultra:
            st.info("👑 **ULTRA-KRONE**\n*(Ultra-Schwer)*")
        else:
            st.text("🔒 👑 (Ultra)")
            
    st.stop()

# --- GEWINNBEDINGUNG DEFINIEREN ---
if st.session_state.Geld >= st.session_state.ziel_summe:
    st.title("SIEG!")
    
    if st.session_state.modus_name == "Einfach":
        st.session_state.trophäe_einfach = True
    elif st.session_state.modus_name == "Mittel":
        st.session_state.trophäe_mittel = True
    elif st.session_state.modus_name == "Schwer":
        st.session_state.trophäe_schwer = True
    elif st.session_state.modus_name == "ULTRA-SCHWER":
        st.session_state.trophäe_ultra = True

    st.balloons()
    st.success(f"🎉 Herzlichen Glückwunsch! Du hast den Modus '{st.session_state.modus_name}' geschafft und eine neue Trophäe freigeschaltet!")
    
    if st.button("Zurück zum Hauptmenü", use_container_width=True):
        # KORREKTUR: Wir entfernen NUR noch das Geld und das Spielsystem aus dem Speicher,
        # die Trophäen lassen wir dank der neuen Logik oben völlig unberührt!
        if "Geld" in st.session_state:
            del st.session_state.Geld
        st.rerun()
    st.stop()

# --- DYNAMISCHE TIMER-AKTUALISIERUNG ---
intervall_ms = int(st.session_state.autoclickerZeit * 1000)
if intervall_ms < 50:
    intervall_ms = 50

st_autorefresh(interval=intervall_ms, key="autoclicker_timer")

# --- AUTOCLICKER BERECHNUNG ---
jetzt = time.time()
zeit_differenz = jetzt - st.session_state.letztes_update

if zeit_differenz >= st.session_state.autoclickerZeit:
    if st.session_state.anzahlAutoclicker > 0:
        durchlaeufe = int(zeit_differenz / st.session_state.autoclickerZeit)
        einkommen = durchlaeufe * st.session_state.anzahlAutoclicker * st.session_state.geldProKlick * st.session_state.klickMultiplikator
        st.session_state.Geld += einkommen
    st.session_state.letztes_update = jetzt

# --- DESIGN DER WEBSEITE ---
st.title("Money Clicker")

st.write(f"**Modus:** {st.session_state.modus_name} | **Tempo:** Alle {st.session_state.autoclickerZeit:.2f} Sek.")
st.write(f"**Ziel:** {st.session_state.ziel_summe:,} Geld")

aktueller_klickwert = st.session_state.geldProKlick * st.session_state.klickMultiplikator
st.metric(label="Dein Vermögen", value=f"{int(st.session_state.Geld)} Geld", delta=f"+{aktueller_klickwert:.1f} pro Klick")

if st.button("Geld", use_container_width=True):
    st.session_state.Geld += aktueller_klickwert
    st.session_state.letztes_update = time.time()
    st.rerun()

st.write("---")
st.subheader("Upgrades & Shop")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write(f"**Basis-Upgrade**")
    st.write(f"Kosten: {st.session_state.upgradeKosten}")
    if st.button(f"Kaufen (+1)", disabled=(st.session_state.Geld < st.session_state.upgradeKosten), key="basis"):
        st.session_state.Geld -= st.session_state.upgradeKosten
        st.session_state.geldProKlick += 1.0
        st.session_state.upgradeKosten = int(st.session_state.upgradeKosten * 1.5)
        st.rerun()

with col2:
    st.write(f"**Multiplikator**")
    st.write(f"Kosten: {st.session_state.multiKosten}")
    if st.button(f"Kaufen (x1.1)", disabled=(st.session_state.Geld < st.session_state.multiKosten), key="multi"):
        st.session_state.Geld -= st.session_state.multiKosten
        st.session_state.klickMultiplikator *= 1.1
        st.session_state.multiKosten = int(st.session_state.multiKosten * 1.8)
        st.rerun()

with col3:
    st.write(f"**Autoclicker**")
    st.write(f"Kosten: {st.session_state.autoclickerKosten}")
    st.write(f"Aktiv: {st.session_state.anzahlAutoclicker}")
    if st.button(f"Kaufen (+1)", disabled=(st.session_state.Geld < st.session_state.autoclickerKosten), key="auto"):
        st.session_state.Geld -= st.session_state.autoclickerKosten
        st.session_state.anzahlAutoclicker += 1
        st.session_state.autoclickerKosten = int(st.session_state.autoclickerKosten * 1.4)
        st.rerun()

with col4:
    st.write(f"**Autoclicker-Tempo**")
    st.write(f"Kosten: {st.session_state.tempoUpgradeKosten}")
    limit_erreicht = st.session_state.autoclickerZeit <= 0.05
    if st.button(f"Kaufen (-0.01s)", disabled=(st.session_state.Geld < st.session_state.tempoUpgradeKosten or limit_erreicht), key="tempo"):
        st.session_state.Geld -= st.session_state.tempoUpgradeKosten
        st.session_state.autoclickerZeit -= 0.01
        st.session_state.anzahlTempoUpgrades += 1
        st.session_state.tempoUpgradeKosten = int(st.session_state.tempoUpgradeKosten * 1.6)
        st.rerun()