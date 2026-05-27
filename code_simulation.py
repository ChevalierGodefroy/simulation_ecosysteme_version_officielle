# Importation des modules
import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from streamlit_scroll_to_top import scroll_to_here
from st_clickable_images import clickable_images
import math
from matplotlib.ticker import FixedLocator, FixedFormatter



# Défilement de la page
def declencher_scroll():
    st.session_state.do_scroll = True



# Structure du site
st.set_page_config(layout="wide")
st.markdown("""<style> section[data-testid="stSidebar"] {width: 250px !important} </style>""", unsafe_allow_html=True)

st.sidebar.markdown("""<style> section[data-testid="stSidebar"] div[data-testid="stRadio"] label div p {font-size: 20px !important; font-weight: 500} </style>""", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: center; font-size: 28px; margin-top: -40px; margin-bottom: -10px; color: #2fa147; '>Pages du site</h1>", unsafe_allow_html=True)
choix_page = st.sidebar.radio(label="", options=["Théorie", "Simulation"], on_change=declencher_scroll)

st.markdown("<h1 style='text-align: center; font-size: 40px; margin-top: -75px; margin-bottom: 20px; color: #38b553; '>Écosystème en action</h1>", unsafe_allow_html=True)



# Création de la simulation
if choix_page == "Simulation":


    # Défilement de la page
    if st.session_state.get('do_scroll', False):
        scroll_to_here(0, key="scroll_action")
        st.session_state.do_scroll = False


    # Création du menu de curseurs pour le graphique principal
    with st.container():
        row1_col1, row1_col2, row1_col3, row1_col4, row1_col5, row1_col6 = st.columns([3, 2, 2, 2, 2, 2], vertical_alignment="top")

        row1_col1.markdown("<h1 style='text-align: center; font-size: 18px; margin: 0px; '>Espèce</h1>", unsafe_allow_html=True)
        row1_col2.markdown("<h1 style='text-align: center; font-size: 18px; margin: 0px; '>Insectes</h1>", unsafe_allow_html=True)
        row1_col3.markdown("<h1 style='text-align: center; font-size: 18px; margin: 0px; '>Lézard</h1>", unsafe_allow_html=True)
        row1_col4.markdown("<h1 style='text-align: center; font-size: 18px; margin: 0px; '>Coati</h1>", unsafe_allow_html=True)
        row1_col5.markdown("<h1 style='text-align: center; font-size: 18px; margin: 0px; '>Boa</h1>", unsafe_allow_html=True)
        row1_col6.markdown("<h1 style='text-align: center; font-size: 18px; margin: 0px; '>Jaguar</h1>", unsafe_allow_html=True)

    with st.container():
        row2_col1, row2_col2, row2_col3, row2_col4, row2_col5, row2_col6 = st.columns([3, 2, 2, 2, 2, 2], vertical_alignment="top")

        row2_col1.markdown(""" <div style=' font-size: 14px; font-weight: normal; padding-top: 5px; margin: 0; line-height: 1; display: block; '> Quel est le nombre annuel de descendants de l'espèce ? </div> """, unsafe_allow_html=True)
        TP_E1 = row2_col2.slider("", 100, 300, #Solution : 250
                                 200, step=10, key="descendants 1", label_visibility="collapsed")
        TP_E2 = row2_col3.slider("", 10, 50, #Solution : 25
                                 45, step=1, key="descendants 2", label_visibility="collapsed")
        TP_E3 = row2_col4.slider("", 1, 10, #Solution : 3
                                 6, step=1, key="descendants 3", label_visibility="collapsed")
        TP_E4 = row2_col5.slider("", 1, 20, #Solution : 10
                                 3, step=1, key="descendants 4", label_visibility="collapsed")
        TP_E5 = row2_col6.slider("", 1, 5, #Solution : 1
                                 4, step=1, key="descendants 5", label_visibility="collapsed")

    with st.container():
        row3_col1, row3_col2, row3_col3, row3_col4, row3_col5, row3_col6 = st.columns([3, 2, 2, 2, 2, 2], vertical_alignment="top")

        row3_col1.markdown(""" <div style=' font-size: 14px; font-weight: normal; padding-top: 5px; margin-right: 40px; line-height: 1; display: block; '> Quelle est l'efficacité de prédation de l'espèce? </div> """, unsafe_allow_html=True)
        EP_E2 = row3_col3.slider("", 0.1, 1.0, #Solution : 0.5
                                 0.7, step=0.1, key="prédation 2", label_visibility="collapsed")
        EP_E3 = row3_col4.slider("", 0.1, 1.0, #Solution : 0.6
                                 0.4, step=0.1, key="prédation 3", label_visibility="collapsed")
        EP_E4 = row3_col5.slider("", 0.1, 1.0, #Solution : 0.9
                                 0.6, step=0.1, key="prédation 4", label_visibility="collapsed")
        EP_E5 = row3_col6.slider("", 0.1, 1.0, #Solution : 0.6
                                 0.8, step=0.1, key="prédation 5", label_visibility="collapsed")

    with st.container():
        row4_col1, row4_col2, row4_col3, row4_col4, row4_col5, row4_col6 = st.columns([3, 2, 2, 2, 2, 2], vertical_alignment="top")

        row4_col1.markdown(""" <div style=' font-size: 14px; font-weight: normal; padding-top: 5px; margin-right: 50px; line-height: 1; display: block; '> Quelle est l'efficacité de survie de l'espèce? </div> """, unsafe_allow_html=True)
        ES_E1 = row4_col2.slider("", 0.1, 1.0, #Solution : 0.4
                                 0.5, step=0.1, key="survie 1", label_visibility="collapsed")
        ES_E2 = row4_col3.slider("", 0.1, 1.0, #Solution : 0.3
                                 0.2, step=0.1, key="survie 2", label_visibility="collapsed")
        ES_E3 = row4_col4.slider("", 0.1, 1.0, #Solution : 0.5
                                 0.4, step=0.1, key="survie 3", label_visibility="collapsed")
        ES_E4 = row4_col5.slider("", 0.1, 1.0, #Solution : 0.1
                                 0.6, step=0.1, key="survie 4", label_visibility="collapsed")

    with st.container():
        row5_col1, row5_col2, row5_col3, row5_col4, row5_col5, row5_col6 = st.columns([3, 2, 2, 2, 2, 2], vertical_alignment="top")

        row5_col1.markdown(""" <div style=' font-size: 14px; font-weight: normal; padding-top: 5px; margin: 0; line-height: 1; display: block; '> Sans prédation, quelle serait l'espérance de vie de l'espèce ? </div> """, unsafe_allow_html=True)
        Long_E1 = row5_col2.slider("", 1, 10, #Solution : 2
                                   1, step=1, key="longévité 1", label_visibility="collapsed")
        Long_E2 = row5_col3.slider("", 1, 20, #Solution : 12
                                   3, step=1, key="longévité 2", label_visibility="collapsed")
        Long_E3 = row5_col4.slider("", 1, 30, #Solution : 17
                                   8, step=1, key="longévité 3", label_visibility="collapsed")
        Long_E4 = row5_col5.slider("", 1, 50, #Solution : 35
                                   12, step=1, key="longévité 4", label_visibility="collapsed")
        Long_E5 = row5_col6.slider("", 1, 50, #Solution : 25
                                   45, step=1, key="longévité 5", label_visibility="collapsed")

    # Panneau de sélection des 4 paramètres KER
    # with st.container():
    #     row6_col1, row6_col2, row6_col3, row6_col4, row6_col5, row6_col6 = st.columns([3, 2, 2, 2, 2, 2], vertical_alignment="top")
    #
    #     row6_col1.markdown(""" <div style=' font-size: 14px; font-weight: normal; padding-top: 12px; margin: 0; line-height: 1; display: block; '> Paramètre KER ajustable """, unsafe_allow_html=True)
    #     KER_E2 = row6_col3.slider("", 0.01, 10.0, 7.37, step=0.01, key="KER_E2", label_visibility="collapsed")
    #     KER_E2 = KER_E2 / 1_000_000_000_000
    #     KER_E3 = row6_col4.slider("", 0.01, 10.0, 1.51, step=0.01, key="KER_E3", label_visibility="collapsed")
    #     KER_E3 = KER_E3 / 100_000_000
    #     KER_E4 = row6_col5.slider("", 0.01, 10.0, 1.21, step=0.01, key="KER_E4", label_visibility="collapsed")
    #     KER_E4 = KER_E4 / 100_000_000
    #     KER_E5 = row6_col6.slider("", 0.01, 10.0, 0.98, step=0.01, key="KER_E5", label_visibility="collapsed")
    #     KER_E5 = KER_E5 / 100_000

    KER_E2 = 7.37 / 1_000_000_000_000
    KER_E3 = 1.51 / 100_000_000
    KER_E4 = 1.21 / 100_000_000
    KER_E5 = 0.98 / 100_000


    # Si jamais d'autres tests de mise en page sont nécessaires...
    # st.markdown("<h1 style='text-align: center; font-size: 40px; margin-top: -40px; margin-bottom: 20px; color: #38b553; '>--------------------</h1>", unsafe_allow_html=True)


    # Identification des variables

    # Fonction 1 (natalité_proie_de_base) :
    # CIPJPB = calories_ingérées_par_jour_proie_de_base
    # EA = efficacité_alimentaire
    # CMDP = coût_métabolique_du_parent
    # PPDB = population_proie_de_base
    # TP = taille_portée
    # CEPP = coût_énergétique_par_portée

    # Fonction 2 (natalité_et_compétition_proie_de_base) :
    # CDC = constante_de_compétition

    # Fonction 3 (décès_proie) :
    # KER = constante_efficacité_recherche
    # ES = efficacité_survie_proie
    # EP = efficacité_prédation_prédateur
    # PProie = population_proie
    # PPred = population_prédateur
    # TDDPPDT = temps_de_digestion_par_proie_du_type

    # Fonction 4 (natalité_prédateur_via_une_population_de_proies_précise) :
    # KER = constante_efficacité_recherche
    # PProie = population_proie
    # TDDPPDT = temps_de_digestion_par_proie_du_type
    # EPPDT = énergie_par_proie_du_type
    # EA = efficacité_alimentaire
    # CMDP = coût_métabolique_du_parent
    # PPred = population_prédateur
    # TP = taille_portée
    # CEPP = coût_énergétique_par_portée

    # Fonction 5 (mortalité_naturelle) :
    # Long = longévité
    # PEsp = population_espèce

    # Équations :
    # P = population
    # P_0 = population_initiale


    # Équations de l'écosystème
    def natalité_proie_de_base(CIPJPB, EA, CMDP, PProie, TP, CEPP):
        return 0.5*0.6*(CIPJPB * EA - CMDP) * PProie * TP / CEPP

    #def compétition_proie_de_base :
        return natalité * x / K

    def natalité_et_compétition_proie_de_base (CIPJPB, EA, CMDP, PPDB, TP, CEPP, CDC):
        # natalité - compétition = natalité - natalité * x / K = natalité * (1 - x / k)
        return natalité_proie_de_base(CIPJPB, EA, CMDP, PPDB, TP, CEPP) * (1 - PPDB / CDC)

    def décès_proie(KER, ES, EP, PProie, PPred, TDDPPDT):
        return (KER * (EP / ES) * PProie * PPred) / (1 + KER * (EP / ES) * TDDPPDT * PProie)


    def natalité_prédateur_via_une_population_de_proies_précise(KER, ES, EP, PProie, TDDPPDT, EPPDT, EA, CMDP, PPred, TP, CEPP):
        return 0.5 * 0.6 * (((KER * (EP / ES) * PProie) / (1 + KER * (EP / ES) * TDDPPDT * PProie)) * EPPDT * EA - CMDP) * PPred * TP / CEPP

    #def compétition_prédateur_via_une_population_de_proies_précise :
        return natalité * x / K

    def natalité_et_compétition_prédateur_via_une_population_de_proies_précise (KER, ES, EP, PProie, TDDPPDT, EPPDT, EA, CMDP, PPred, TP, CEPP, CDC):
        # natalité - compétition = natalité - natalité * x / K = natalité * (1 - x / k)
        return natalité_prédateur_via_une_population_de_proies_précise(KER, ES, EP, PProie, TDDPPDT, EPPDT, EA, CMDP, PPred, TP, CEPP) * (1 - PPred / CDC)

    def mortalité_naturelle(Long, PEsp):
        return (1 / Long) * PEsp


    # Identification des constantes
    P_E1_0 = 10_000_000_000  #population_initiale_espèce_n
    P_E2_0 = 50_000_000
    P_E3_0 = 100_000
    P_E4_0 = 8_000
    P_E5_0 = 20

    CIPJPB = 1.5  #calories_ingérées_par_jour_proie_de_base

    CDC_E1 = 20_000_000_000_000  #constante_de_compétition #non
    CDC_E2 = 1_000_000_000
    CDC_E3 = 2_000_000
    CDC_E4 = 60_000
    CDC_E5 = 40

    TDDPP_E2_E1 = 0.02   #temps_de_digestion_par_proie_quand_espèce_n_mange_espèce_m
    TDDPP_E3_E1 = 0.002
    TDDPP_E3_E2 = 0.07
    TDDPP_E4_E2 = 0.2
    TDDPP_E4_E3 = 4
    TDDPP_E5_E3 = 0.3
    TDDPP_E5_E4 = 0.4

    EPPDT_E1 = 5   #énergie_par_proie_du_type_espèce_n
    EPPDT_E2 = 200
    EPPDT_E3 = 8000
    EPPDT_E4 = 18000
    EPPDT_E5 = 120000

    EA_E1_Herbe = (1) * 0.4 # efficacité_alimentaire_quand_espèce_n_mange_espèce_m
    EA_E2_E1 = 0.9 * 0.8
    EA_E3_E1 = 0.8 * 0.7
    EA_E3_E2 = 0.85 * 0.8
    EA_E4_E2 = 1 * 0.85
    EA_E4_E3 = 1 * 0.8
    EA_E5_E3 = 0.8 * 0.9
    EA_E5_E4 = 0.8 * 0.9

    CMDP_E1 = 0.3  #coût_métabolique_du_parent_espèce_n
    CMDP_E2 = 5
    CMDP_E3 = 300
    CMDP_E4 = 60
    CMDP_E5 = 3500

    TPI_E1 = TP_E1 / 365  #taille_portée_instantanée_espèce_n
    TPI_E2 = TP_E2 / 365
    TPI_E3 = TP_E3 / 365
    TPI_E4 = TP_E4 / 365
    TPI_E5 = TP_E5 / 365

    CEPP_E1 = 12  #coût_énergétique_par_portée_espèce_n
    CEPP_E2 = 40
    CEPP_E3 = 4000
    CEPP_E4 = 5000
    CEPP_E5 = 80000

    LongJ_E1 = Long_E1 * 365  #longévité_jours_espèce_n
    LongJ_E2 = Long_E2 * 365
    LongJ_E3 = Long_E3 * 365
    LongJ_E4 = Long_E4 * 365
    LongJ_E5 = Long_E5 * 365


    # Système d'équations différentielles
    def système_équations(t, y):

        # Protection contre les valeurs négatives
        y_safe = np.maximum(y, 0)
        P_E1, P_E2, P_E3, P_E4, P_E5 = y_safe

        # Terme de natalité : 1.0 si pop >= 10, sinon 0.0
        peut_reproduire = (y_safe >= 10.0).astype(float)

        dP_E1dt = natalité_et_compétition_proie_de_base(CIPJPB, EA_E1_Herbe, CMDP_E1, P_E1, TPI_E1, CEPP_E1, CDC_E1)*peut_reproduire[0] - décès_proie (KER_E2, ES_E1, EP_E2, P_E1, P_E2, TDDPP_E2_E1) - décès_proie(KER_E3, ES_E1, EP_E3, P_E1, P_E3, TDDPP_E3_E1) - mortalité_naturelle(LongJ_E1, P_E1)
        dP_E2dt = natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E2, ES_E1, EP_E2, P_E1, TDDPP_E2_E1, EPPDT_E1, EA_E2_E1, CMDP_E2, P_E2, TPI_E2, CEPP_E2, CDC_E2)*peut_reproduire[1] - décès_proie(KER_E3, ES_E2, EP_E3, P_E2, P_E3, TDDPP_E3_E2) - décès_proie(KER_E4, ES_E2, EP_E4, P_E2, P_E4, TDDPP_E4_E2) - mortalité_naturelle(LongJ_E2, P_E2)
        dP_E3dt = (natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E3, ES_E1, EP_E3, P_E1, TDDPP_E3_E1, EPPDT_E1, EA_E3_E1, CMDP_E3, P_E3, TPI_E3, CEPP_E3, CDC_E3) + natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E3, ES_E2, EP_E3, P_E2, TDDPP_E3_E2, EPPDT_E2, EA_E3_E2, CMDP_E3, P_E3, TPI_E3, CEPP_E3, CDC_E3))*peut_reproduire[2] - décès_proie(KER_E4, ES_E3, EP_E4, P_E3, P_E4, TDDPP_E4_E3) - décès_proie(KER_E5, ES_E3, EP_E5, P_E3, P_E5, TDDPP_E5_E3) - mortalité_naturelle(LongJ_E3, P_E3)
        dP_E4dt = (natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E4, ES_E2, EP_E4, P_E2, TDDPP_E4_E2, EPPDT_E2, EA_E4_E2, CMDP_E4, P_E4, TPI_E4, CEPP_E4, CDC_E4) + natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E4, ES_E3, EP_E4, P_E3, TDDPP_E4_E3, EPPDT_E3, EA_E4_E3, CMDP_E4, P_E4, TPI_E4, CEPP_E4, CDC_E4))*peut_reproduire[3] - décès_proie(KER_E5, ES_E4, EP_E5, P_E4, P_E5, TDDPP_E5_E4) - mortalité_naturelle(LongJ_E4, P_E4)
        dP_E5dt = (natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E5, ES_E3, EP_E5, P_E3, TDDPP_E5_E3, EPPDT_E3, EA_E5_E3, CMDP_E5, P_E5, TPI_E5, CEPP_E5, CDC_E5) + natalité_et_compétition_prédateur_via_une_population_de_proies_précise(KER_E5, ES_E4, EP_E5, P_E4, TDDPP_E5_E4, EPPDT_E4, EA_E5_E4, CMDP_E5, P_E5, TPI_E5, CEPP_E5, CDC_E5))*peut_reproduire[4] - mortalité_naturelle(LongJ_E5, P_E5)

        dérivées = [dP_E1dt, dP_E2dt, dP_E3dt, dP_E4dt, dP_E5dt]

        # Coinçage des valeurs à 0 : sécurité contre les écarts mathématiques du solveur
        for i in range(len(dérivées)):
            if y[i] <= 0:
                dérivées[i] = 0

        return dérivées


    # Conditions initiales
    y0 = [P_E1_0, P_E2_0, P_E3_0, P_E4_0, P_E5_0]

    # Réglage du temps
    t_fin_graphique = 20 * 365
    t_fin_simulation = 200 * 365

    # Liste de points pour le graphique
    points_graphique = np.linspace(0, t_fin_graphique, 10000)

    # Liste de points à mémoriser pour la SIMULATION
    échelle_temps_simul = np.append(points_graphique, t_fin_simulation)

    # Durée totale de la simulation
    durée_simul = (0, t_fin_simulation)


    # Test diagnostique sur les taux de variation
    # with st.expander("🔍 **Test diagnostique** des taux initiaux (t=0)"):
    #
    #     noms_diag = ["Insectes", "Lézard", "Coati", "Boa", "Jaguar"]
    #     taux_initiaux = système_équations(0, y0)
    #     infos_initiales = []
    #
    #     for i in range(5):
    #         pop_actuelle = y0[i]
    #         taux = taux_initiaux[i]
    #
    #         pourcentage = (taux / pop_actuelle) * 100 if pop_actuelle > 0 else 0
    #
    #         infos_initiales.append({"Espèce": noms_diag[i], "Variation (individus/jour)": f"{taux:,.2f}", "Variation (%)": f"{pourcentage:+.2f} %"})
    #
    #     st.table(infos_initiales)


    # Résolution du système d'équations différentielles
    sol = solve_ivp(système_équations, durée_simul, y0, t_eval=échelle_temps_simul, method='RK45')



    # Calcul du flux énergétique
    t_jours = sol.t #.t est la variable horizontale de la boîte numérique de résultats et .y est la variable verticale
    resultat_population = sol.y
    nombre_de_pas = len(t_jours)

    # Création des arrays numpy vides
    energie_entrante = np.zeros((5, nombre_de_pas))
    energie_sortante = np.zeros((5, nombre_de_pas))

    flux_energetique_annuel = {"Herbe_E1": np.zeros(nombre_de_pas), "E1_E2": np.zeros(nombre_de_pas), "E1_E3": np.zeros(nombre_de_pas), "E2_E3": np.zeros(nombre_de_pas), "E2_E4": np.zeros(nombre_de_pas), "E3_E4": np.zeros(nombre_de_pas), "E3_E5": np.zeros(nombre_de_pas), "E4_E5": np.zeros(nombre_de_pas)}

    for i in range(nombre_de_pas): # Tableau avec calories annuelles pour les 5 espèces (x) pour toutes les années (y)

        # Population pour 1 année pour 1 espèce, dans une liste pour les 5 espèces
        p = resultat_population[:, i]

        # Énergie espèce 1 (insectes)
        Herbe_E1 = CIPJPB * p[0]
        flux_energetique_annuel["Herbe_E1"][i] = Herbe_E1
        # Entrant : Environnement
        energie_entrante[0, i] = Herbe_E1 * EA_E1_Herbe
        # Sortant : métabolisme + prédation E2 + prédation E3 + mort naturelle
        energie_sortante[0, i] = (CMDP_E1 * p[0]) + (décès_proie(KER_E2, ES_E1, EP_E2, p[0], p[1], TDDPP_E2_E1) + décès_proie(KER_E3, ES_E1, EP_E3, p[0],p[2], TDDPP_E3_E1) + ( 1 / LongJ_E1) * p[0]) * EPPDT_E1

        # Énergie espèce 2 (lézard)
        E1_E2 = décès_proie(KER_E2, ES_E1, EP_E2, p[0], p[1], TDDPP_E2_E1) * EPPDT_E1
        flux_energetique_annuel["E1_E2"][i] = E1_E2
        # Entrant : prédation E1
        energie_entrante[1, i] = E1_E2 * EA_E2_E1
        # Sortant : métabolisme + prédation E3 + prédation E4 + mort naturelle
        energie_sortante[1, i] = (CMDP_E2 * p[1]) + (décès_proie(KER_E3, ES_E2, EP_E3, p[1], p[2], TDDPP_E3_E2) + décès_proie(KER_E4, ES_E2, EP_E4, p[1],p[3], TDDPP_E4_E2) + (1 / LongJ_E2) * p[1]) * EPPDT_E2

        # Énergie espèce 3 (coati)
        E1_E3 = décès_proie(KER_E3, ES_E1, EP_E3, p[0], p[2], TDDPP_E3_E1) * EPPDT_E1
        flux_energetique_annuel["E1_E3"][i] = E1_E3
        E2_E3 = décès_proie(KER_E3, ES_E2, EP_E3, p[1], p[2], TDDPP_E3_E2) * EPPDT_E2
        flux_energetique_annuel["E2_E3"][i] = E2_E3
        # Entrant : prédation E2 + prédation E1
        energie_entrante[2, i] = (E1_E3 * EA_E3_E1 + E2_E3 * EA_E3_E2)
        # Sortant : métabolisme + prédation E4 + prédation E5 + mort naturelle
        energie_sortante[2, i] = (CMDP_E3 * p[2]) + (décès_proie(KER_E4, ES_E3, EP_E4, p[2], p[3], TDDPP_E4_E3) + décès_proie(KER_E5, ES_E3, EP_E5, p[2],p[4], TDDPP_E5_E3) + (1 / LongJ_E3) * p[2]) * EPPDT_E3

        # Énergie espèce 4 (boa)
        E2_E4 = décès_proie(KER_E4, ES_E2, EP_E4, p[1], p[3], TDDPP_E4_E2) * EPPDT_E2
        flux_energetique_annuel["E2_E4"][i] = E2_E4
        E3_E4 = décès_proie(KER_E4, ES_E3, EP_E4, p[2], p[3], TDDPP_E4_E3) * EPPDT_E3
        flux_energetique_annuel["E3_E4"][i] = E3_E4
        # Entrant : prédation E2 + prédation E3
        energie_entrante[3, i] = (E2_E4 * EA_E4_E2 + E3_E4 * EA_E4_E3)
        # Sortant : métabolisme + prédation E5 + mort naturelle
        energie_sortante[3, i] = (CMDP_E4 * p[3]) + (décès_proie(KER_E5, ES_E4, EP_E5, p[3], p[4], TDDPP_E5_E4) + (1 / LongJ_E4) * p[3]) * EPPDT_E4

        # Énergie espèce 5 (jaguar)
        E3_E5 = décès_proie(KER_E5, ES_E3, EP_E5, p[2], p[4], TDDPP_E5_E3) * EPPDT_E3
        flux_energetique_annuel["E3_E5"][i] = E3_E5
        E4_E5 = décès_proie(KER_E5, ES_E4, EP_E5, p[3], p[4], TDDPP_E5_E4) * EPPDT_E4
        flux_energetique_annuel["E4_E5"][i] = E4_E5
        # Entrant : prédation E3 + prédation E4
        energie_entrante[4, i] = (E3_E5 * EA_E5_E3 + E4_E5 * EA_E5_E4)
        # sortant : métabolisme + mort naturelle
        energie_sortante[4, i] = (CMDP_E5 * p[4]) + (1 / LongJ_E5) * p[4] * EPPDT_E5



    # Préparation de la mise en page
    placeholder_graphique = st.container()


    # Slider année
    col1, col2, col3 = st.columns([1.35,5,0.2])
    with col1:
        st.markdown(""" <div style=' font-size: 14px; font-weight: normal; margin-top: -5px '> Sélectionnez l'année<br>à analyser.</div> """, unsafe_allow_html=True)
    with col2:
        annee_selectionnee = st.slider("", 1, 20, 10, label_visibility="collapsed")

    # Préparation des masques
    jour_debut = (annee_selectionnee - 1) * 365
    jour_fin = annee_selectionnee * 365
    jour_debut_precedent = (annee_selectionnee - 2) * 365
    masque = (sol.t >= jour_debut) & (sol.t <= jour_fin)
    temps_tranche = sol.t[masque]
    # Masque précédent pour la comparaison
    masque_precedent = (sol.t >= jour_debut_precedent) & (sol.t <= jour_debut) if annee_selectionnee > 1 else None
    temps_tranche_precedente = sol.t[masque_precedent] if annee_selectionnee > 1 else None


    # Préparation des données pour le tableau diagnostique
    infos_flux = []
    noms_especes = ["Insectes", "Lézard", "Coati", "Boa", "Jaguar"]



    for i in range(5):
        # Calcul du flux
        flux_net_array = energie_entrante[i][masque] - energie_sortante[i][masque]
        # Intégrer pour le total
        energie_nette_totale = np.trapezoid(flux_net_array, x=temps_tranche)

        #Début du test diagnostique

        # Variation de la population
        changement_population = sol.y[i][masque][-1] - sol.y[i][masque][0] if any(masque) else 0

        # Préparation du tableau diagnostique
        suffixe_individu = "individu" if abs(changement_population) <= 1 else "individus"
        infos_flux.append({"Espèce": noms_especes[i], "Bilan énergétique annuel (kcal)": f"{energie_nette_totale:,.0f}", "Variation de la population": f"{changement_population:+,.0f} {suffixe_individu}", "Statut": "📈 Croissance" if changement_population > 0 else "📉 Décroissance"})

    # Affichage du test diagnostique
    with st.expander(f"**Vue d'ensemble des résultats de l'année**"):
        st.table(infos_flux)



    #Préparation de l'espace pour le graphique principal
    with placeholder_graphique:
        col1, col2 = st.columns([1, 10])

        with col1:
            # Images des animaux
            st.markdown("""<div style="display: flex; justify-content: center; margin-top: 60px; "> <img src="https://i.postimg.cc/SsVf3Ldz/cropped-circle-image-(11).png" width="70"> </div> """, unsafe_allow_html=True)
            st.markdown("""<div style="display: flex; justify-content: center; margin-top: 25px; "> <img src="https://i.postimg.cc/qqFsK0NM/cropped_circle_image_(8).png" width="70"> </div> """, unsafe_allow_html=True)
            st.markdown("""<div style="display: flex; justify-content: center; margin-top: 25px; "> <img src="https://i.postimg.cc/TwRhDqR5/cropped-circle-image-(3).png" width="70"> </div> """, unsafe_allow_html=True)
            st.markdown("""<div style="display: flex; justify-content: center; margin-top: 25px; "> <img src="https://i.postimg.cc/XJxLfq3s/cropped-circle-image-(2).png" width="70"> </div> """, unsafe_allow_html=True)
            st.markdown("""<div style="display: flex; justify-content: center; margin-top: 25px; "> <img src="https://i.postimg.cc/g26zX6d4/cropped-circle-image-(1).png" width="70"> </div> """, unsafe_allow_html=True)

        with col2:
            #Zone du graphique
            figure_1, axe_1 = plt.subplots(figsize=(10, 6))

            masque_20_ans = sol.t <= (20 * 365)
            temps_20_ans = sol.t[masque_20_ans] / 365
            données_20_ans = sol.y[:, masque_20_ans]

            # Astuce pour contourner le 0 logarithmique : ajouter une constante epsilon à chaque valeur en y.
            epsilon = 0.1
            données_visuelles = données_20_ans + epsilon

            #Création des 5 courbes
            for rang_courbe in range(5):
                axe_1.plot(temps_20_ans, données_visuelles[rang_courbe], label=f"Espèce {rang_courbe + 1}")

            # AXE DES Y

            # Configuration de l'axe des y (type et plages de données)
            axe_1.set_yscale("log")
            max_global = np.max(données_20_ans)
            n_max = math.ceil(math.log10(max_global)) if max_global > 1 else 1
            limite_haute = 10 ** n_max

            # Graduations majeures (0, 10^0, 10^1...)
            position_grads_majeures = [epsilon] + [10 ** i for i in range(n_max + 1)]
            etiquettes_grads_majeures = ["0"] + [f"$10^{{{i}}}$" for i in range(n_max + 1)]

            # Graduations mineures
            position_grads_mineures = []
            for exp in range(-1, n_max):
                for sub in range(2, 10):
                    val = sub * (10 ** exp)
                    # On empêche l'apparition de données sous la limite inférieure
                    if val > epsilon:
                        position_grads_mineures.append(val)

            # Impression des graduations
            axe_1.yaxis.set_major_locator(FixedLocator(position_grads_majeures))
            axe_1.yaxis.set_major_formatter(FixedFormatter(etiquettes_grads_majeures))
            axe_1.yaxis.set_minor_locator(FixedLocator(position_grads_mineures))

            # AXE DES X
            axe_1.xaxis.set_major_locator(FixedLocator(np.arange(0, 21, 2)))
            axe_1.set_xlabel("Temps (années)")

            # Ajustement du quadrillage et des graduations
            axe_1.grid(False)
            axe_1.tick_params(axis='y', which='both', left=True, labelleft=True, direction='out')

            # Marges du graphique
            axe_1.set_xlim(-0.8, 20.8)
            axe_1.set_ylim(10 ** -1.3, 10 ** (n_max + 0.2))

            # Bande de l'année sélectionnée
            debut_annee = (annee_selectionnee - 1)
            fin_annee = annee_selectionnee
            axe_1.axvline(x=debut_annee, color='red', linestyle='-', alpha=0.7)
            axe_1.axvline(x=fin_annee, color='red', linestyle='-', alpha=0.7)

            # Ligne du seuil d'extinction
            axe_1.axhline(y=10 + epsilon, color='black', linestyle='--', linewidth='1')
            axe_1.text(10, 10 + epsilon, "Seuil d'extinction", ha="center", va="center",bbox=dict(facecolor='#54d765', edgecolor='#198631', boxstyle='round,pad=0.3'))
            axe_1.axvspan(debut_annee, fin_annee, color='#f72a57', alpha=0.1)

            st.pyplot(figure_1)



    st.write("---")
    st.markdown("<h1 style='text-align: center; font-size: 30px; margin-top: -10px; margin-bottom: 20px; color: #1637f2; '>Analyse annuelle détaillée</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; font-size: 25px; margin-bottom: 20px; color: #56adf5; '>Variation des flux caloriques</h1>", unsafe_allow_html=True)

    # Création d'une grille 6x2 pour pouvoir centrer les graphiques du bas : 2,2,2 en haut et (1),2,2,(1) en bas
    cinq_graphiques_energie = plt.figure(figsize=(10, 6))
    cases_grille = cinq_graphiques_energie.add_gridspec(2, 6)

    axes = []
    # Ligne du haut
    axes.append(cinq_graphiques_energie.add_subplot(cases_grille[0, 0:2]))
    axes.append(cinq_graphiques_energie.add_subplot(cases_grille[0, 2:4]))
    axes.append(cinq_graphiques_energie.add_subplot(cases_grille[0, 4:6]))
    # Ligne du bas
    axes.append(cinq_graphiques_energie.add_subplot(cases_grille[1, 1:3]))
    axes.append(cinq_graphiques_energie.add_subplot(cases_grille[1, 3:5]))

    noms_especes = ["Insectes", "Lézard", "Coati", "Boa", "Jaguar"]
    couleurs_lignes = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    for i in range(5):
        bilan_energie = energie_entrante[i] - energie_sortante[i]
        ax = axes[i]

        ax.plot(t_jours / 365, bilan_energie, color=couleurs_lignes[i], lw=1.5)
        ax.fill_between(t_jours / 365, bilan_energie, 0, where=(bilan_energie >= 0), color='#3ab546', alpha=0.3)
        ax.fill_between(t_jours / 365, bilan_energie, 0, where=(bilan_energie < 0), color='#e03d55', alpha=0.3)

        ax.set_xlim(debut_annee, fin_annee)

        # Adaptation de l'échelle en Y
        masque_visuel = (t_jours / 365 >= debut_annee) & (t_jours / 365 <= fin_annee)
        donnees_visibles = bilan_energie[masque_visuel]

        if len(donnees_visibles) > 0:
            v_min, v_max = np.min(donnees_visibles), np.max(donnees_visibles)
            marge = (v_max - v_min) * 0.1 if v_max != v_min else abs(v_max) * 0.1 if v_max != 0 else 1.0
            ax.set_ylim(v_min - marge, v_max + marge)

        # Augmentation de la visibilité de l'échelle
        ax.yaxis.get_offset_text().set_color('#56adf5')
        ax.yaxis.get_offset_text().set_weight('bold')

        ax.set_title(f"Flux net : {noms_especes[i].lower()}", fontsize=10)
        ax.set_xlabel("Plage annuelle", fontsize=8)
        ax.set_ylabel("kcal/jour", fontsize=8)
        ax.axhline(0, color='black', lw=0.8, ls='--')
        ax.grid(alpha=0.3)

    plt.tight_layout()
    st.pyplot(cinq_graphiques_energie)

    #Schéma du bilan énergétique

    st.markdown("<h1 style='text-align: center; font-size: 25px; margin-top: 20px; margin-bottom: -10px; color: #56adf5; '>Bilan énergétique annuel</h1>", unsafe_allow_html=True)

    # Préparation des rectangles colorés pour le texte
    def texte_superposable(text, top, left, type_couleur="vert", width="auto", energie_annee_actuelle=0, energie_annee_precedente=0):
        if type_couleur == "gris":
            couleur = "#b0b0b0"
        else:
            couleur = "#3dd16c" if energie_annee_actuelle > energie_annee_precedente else "#f51d50"

        st.markdown(f""" <div style=" position: absolute; top: {top}px; left: {left}px; transform: translate(-50%, -50%); z-index: 1000; background-color: {couleur}; color: white; text-align: center; font-size: 10px; padding: 10px 10px; border-radius: 8px; font-family: sans-serif; font-weight: bold; width: {width}; white-space: nowrap; "> {text} </div> """, unsafe_allow_html=True)

    st.markdown("""<div style="display: flex; justify-content: center; margin-bottom: 80px"> <img src="https://i.postimg.cc/ZKJZkP1Q/Echanges-energetiques.png" > </div>""", unsafe_allow_html=True)

    # Création d'un dictionnaire qui prend les noms des transferts écosystémiques et calcul les flux de l'année actuelle
    flux_annee_actuelle = {etiquette: np.trapezoid(val[masque], x=temps_tranche) for etiquette, val in flux_energetique_annuel.items()}

    # Création d'un dictionnaire qui prend les noms des transferts écosystémiques et calcul les flux de l'année précédente
    if annee_selectionnee != 1:
        flux_annee_precedente = {etiquette: np.trapezoid(val[masque_precedent], x=temps_tranche_precedente) for etiquette, val in flux_energetique_annuel.items()}
    else:
        flux_annee_precedente = {}

    configuration_bulles = [
        (-370, 175, "Herbe_E1", EA_E1_Herbe),
        (-386, 345, "E1_E2", EA_E2_E1),
        (-255, 430, "E1_E3", EA_E3_E1),
        (-418, 510, "E2_E3", EA_E3_E2),
        (-576, 597, "E2_E4", EA_E4_E2),
        (-450, 680, "E3_E4", EA_E4_E3),
        (-318, 764, "E3_E5", EA_E5_E3),
        (-482, 845, "E4_E5", EA_E5_E4)]

    for top, left, etiquette, eff_alim in configuration_bulles:
        val_actuelle = flux_annee_actuelle[etiquette]
        val_precedente = flux_annee_precedente.get(etiquette, 0)
        type_couleur = "gris" if annee_selectionnee == 1 else ""

        texte_superposable(f"{val_actuelle:,.0f} kcal ⋅ {eff_alim:g}<br>= {val_actuelle * eff_alim:,.0f} kcal", top=top, left=left, type_couleur=type_couleur, energie_annee_actuelle = val_actuelle, energie_annee_precedente = val_precedente)



    with st.sidebar:

        # Bouton de validation
        st.markdown("<h1 style='text-align: center; font-size: 20px; margin-top: 10px; color: #2fa147; '>Valider la viabilité</h1>", unsafe_allow_html=True)
        activation_bouton_verif_simul = clickable_images(["https://i.postimg.cc/QxNJ19t2/Bouton-simulateur-ecosysteme.png"], div_style={"display": "flex", "justify-content": "center"}, img_style={"width": "80px"},)

        if 'ballons_deja_affiches' not in st.session_state:
            st.session_state.ballons_deja_affiches = False

        if activation_bouton_verif_simul == 0 :

            #Valeur des populations après 200 ans
            populations_finales = sol.y[:, -1]

            # Succès de l'utilisateur
            if all(populations_finales > 10):
                st.sidebar.success("🏆 **Succès !**\n\nAprès 200 ans, les 5 espèces ont survécu et l'écosystème est en pleine santé ! 🌷")
                if st.session_state.ballons_deja_affiches == False:
                    for i in range(2):
                        st.balloons()
                    st.session_state.ballons_deja_affiches = True

            # Échec de l'utilisateur
            else:

                liste_especes_eteintes = [i for i, population in enumerate(populations_finales) if population < 5]
                nb_especes_eteintes = len(liste_especes_eteintes)

                if nb_especes_eteintes == 1 :
                    st.error("❌ **Échec...**\n\nL'écosystème n'est pas pérenne. Après 200 ans, il y a eu une extinction. 🦖")
                else:
                    st.error(f"❌ **Échec...**\n\nL'écosystème n'est pas pérenne. Après 200 ans, il y a eu {nb_especes_eteintes} extinctions. 🦖")

                noms = ["Insectes", "Lézard", "Coati", "Boa", "Jaguar"]

                for num_espece, population in enumerate(populations_finales):
                    if population < 10:
                        st.markdown(f"<span style='font-size: 15.5px;'>❌ L'espèce **{noms[num_espece]}** s'est éteinte.</span>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<span style='font-size: 15.5px;'>✅ L'espèce **{noms[num_espece]}** a survécu.</span>", unsafe_allow_html=True)

                st.session_state.ballons_deja_affiches = False


# if choix_page == "Théorie"
else:
    if st.session_state.get('do_scroll', False):
        scroll_to_here(0, key="scroll_action")
        st.session_state.do_scroll = False

    st.markdown("<h1 style='text-align: left; font-size: 18px; font-weight: normal; margin-top: 20px; margin-bottom: 20px'><i>Site réalisé par Etienne Baribeault et Vincent Dion</i></h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; font-size: 20px; color: #1b9dde; '>Avant-propos</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: justify; font-size: 18px; font-weight: normal; line-height: 1.5; margin-bottom: 40px'>"
                "Les populations d’un écosystème s’organisent en un réseau trophique, "
                "c’est-à-dire un ensemble de chaînes alimentaires (relations de prédation linéaires) qui s’entrecroisent. La prédation amène un transfert énergétique "
                "qui est limité par l’efficacité d’ingestion, l’efficacité de digestion et l’efficacité écologique (qui se penche sur les pertes d’énergie entraînées "
                "par la respiration cellulaire) du prédateur. Des transferts énergétiques soutenus et proportionnels à la population d’une espèce sont nécessaires "
                "pour assurer sa survie et sa prolifération. La prédation est influencée par une immense gamme de facteurs, dont plusieurs seront abordés lors de la "
                "présentation du site, facteurs pouvant être exploités mathématiquement pour avoir une idée de l’état d’une population et de son avenir. Il serait cependant "
                "irréaliste de chercher à produire un modèle mathématique exact, puisqu’un écosystème est régi par des phénomènes difficilement prévisibles à long terme, "
                "voire aléatoires, comme la météo, les maladies, le comportement, l’irrégularité relative de la reproduction, etc."
                "</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; font-size: 20px; color: #1b9dde; '>Présentation du site</h1>", unsafe_allow_html=True)

    #Définir un style
    st.markdown("""<style>.custom-text {text-align: justify; font-size: 18px; font-weight: normal; line-height: 1.5}</style>""", unsafe_allow_html=True)

    # Exemples d'intégration de LaTeX
    # st.markdown('<span class="custom-text">Polynôme :</span> $N_a = \\frac{aNT}{1 + aNT_h}$', unsafe_allow_html=True)
    # st.markdown("Voici un polynôme : $2x^3 - 4x^2 + 5$. Par contre, ceci est une équation logarithmique : $ f'(x) = 3 \cdot ln(3x + 2)$.")
    # st.markdown('<span class="custom-text">Polynôme :</span> $N_a = \\frac{aNT}{1 + aNT_h}$', unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Afin de modéliser mathématiquement l’évolution d’une population, nous nous sommes inspirés du modèle de Lotka-Volterra, '
                'qui évalue l’évolution des populations d’un couple prédateur-proie à l’aide de deux équations :<br><br>'
                '$\\frac{dx}{dt}=\\alpha x-\\beta xy$<br><br>'
                '$\\frac{dy}{dt}=\\delta xy-\\gamma y$<br><br>'
                '$x$ représente la population de proies ;<br>'
                '$y$, la population de prédateurs ;<br>'
                '$\\alpha$, le taux de croissance maximal de la population de proies ;<br>'
                '$\\beta$, le taux de mortalité des proies causé par les prédateurs ;<br>'
                '$\\delta$, le taux de croissance maximal des prédateurs assuré par la consommation de proies ;<br>'
                '$\\gamma$, le taux de mortalité des prédateurs.<br><br><br></span>',
                unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Nous avons également incorporé dans nos équations le modèle de Holling de type II, qui étudie le nombre '
        'de proies consommées par un prédateur dans un intervalle de temps donné d’après une limite basée sur une efficacité de traitement des prises :<br><br>'
        '$N_a=\\frac{aNT}{1+aNT_h} $<br><br>'
        '$N_a$ représente le nombre de proies consommées par un prédateur ;<br>'
        '$a$, l’efficacité d’attaque ;<br>'
        '$N$, le nombre de proies disponibles ;<br>'
        '$T$, la durée de l’étude ;<br>'
        '$T_h$, le temps de manipulation par proie (recherche, capture, ingestion, digestion).<br><br><br></span>',
        unsafe_allow_html=True)

    st.markdown('<div class="custom-text">Afin de préciser les constantes des deux modèles, nous avons incorporé des paramètres mesurables comme le nombre de calories '
        'par proie, le coût de production d’une portée et la taille de cette dernière. Nous avons également généralisé le terme de longévité de l’équation de Lotka-Volterra '
        'auprès de toutes les espèces de l’écosystème, et avons ajouté un terme de compétition entre les membres d’une même espèce pour tenir compte de la limitation de l’espace '
        'et des ressources dans un milieu naturel. C’est ainsi que nous avons cerné les différents termes à inclure dans les équations différentielles représentant la variation '
        'de la population de chacune des espèces selon le temps.<br><br><br></div>',
        unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Terme de natalité de la proie à la base de l’écosystème :<br><br>'
        '$\\frac{0{,}5\\cdot0{,}6\\cdot\\left(C_{PJ}\\cdot E_A-C_{MP}\\right)\\cdot T_P\\cdot P_{Proie}}{C_{EP}}$<br><br>'
        '$0{,}5$ représente la proportion de femelles ;<br>'
        '$0{,}6$, la proportion de femelles pouvant mettre bas ;<br>'
        '$C_{PJ}$, le nombre de calories ingérées par jour par la proie de base ;<br>'
        '$E_A$, l’efficacité alimentaire ;<br>'
        '$C_{MP}$, le coût métabolique du parent ;<br>'
        '$T_P$, la taille d’une portée ;<br>'
        '$P_{Proie}$, la taille de la population de proies;<br>'
        '$C_{EP}$, le coût énergétique pour la production d’une portée.<br><br><br></span>',
        unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Terme de compétition d’une espèce :<br><br>'
                '$\\frac{T_N \\cdot P}{P_{Max}}$<br><br>'
                '$T_N$ représente le terme de natalité de la proie ;<br>'
                '$P$, la taille de la population ;<br>'
                '$P_{Max}$, la population maximale que l’écosystème peut soutenir.<br><br><br></span>',
                unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Terme de décès d’une proie par un prédateur spécifique :<br><br>'
                '$\\frac{K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right) \\cdot P_{Proie} \\cdot P_{Pred}}{1 + K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right) \\cdot T_h \\cdot P_{Proie}}$<br><br>'
                '$K_{ER}$ représente la constante d’efficacité de recherche ;<br>'
                '$E_P$, l’efficacité de prédation du prédateur ;<br>'
                '$E_S$, l’efficacité de survie de la proie ;<br>'
                '$P_{Proie}$, la taille de la population de proies ;<br>'
                '$P_{Pred}$, la taille de la population de prédateurs ;<br>'
                '$T_h$, le temps de manipulation par proie.<br><br>'
                '<i>On reconnaît l’inspiration du modèle de Holling de type II ($\\frac{aN}{1 + aNT_h} \\cdot P_{Pred}$), '
                'avec un $a$ (l’efficacité d’attaque) équivalent à $K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right)$ '
                'et un $N$ (le nombre de proies disponibles) remplacé par $P_{Proie}$.</i><br><br><br></span>',
                unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Terme de natalité d’un prédateur grâce à une population de proies précise :<br><br>'
        '$\\frac{0{,}5 \\cdot 0{,}6 \\cdot \\left(\\frac{K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right) \\cdot P_{Proie} \\cdot P_{Pred}}{1 + K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right) \\cdot T_h \\cdot P_{Proie}} \\cdot E_{Proie} \\cdot E_A - C_{MP}\\right) \\cdot T_P \\cdot P_{Pred}}{C_{EP}}$<br><br>'
        'Cette équation correspond à celle de la natalité des proies ($\\frac{0{,}5 \\cdot 0{,}6 \\cdot (C_{PJ} \\cdot E_A - C_{MP}) \\cdot T_P \\cdot P_{Proie}}{C_{EP}}$), '
        'où le nombre de calories ingérées par jour<br>($C_{PJ}$) est exprimé comme fonction du nombre de proies, '
        'en multipliant le nombre de proies tuées ($\\frac{K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right) \\cdot P_{Proie} \\cdot P_{Pred}}{1 + K_{ER} \\cdot \\left(\\frac{E_P}{E_S}\\right) \\cdot T_h \\cdot P_{Proie}}$) '
        'par l’énergie contenue dans chaque proie ($E_{Proie}$).<br><br><br></span>',
        unsafe_allow_html=True)

    st.markdown('<span class="custom-text">Terme de mortalité naturelle :<br><br>'
                '$\\frac{P}{L}$<br><br>'
                '$P$ représente la population de l’espèce ;<br>'
                '$L$, sa longévité dans les conditions optimales.<br><br><br>',
                unsafe_allow_html=True)

    st.markdown('<span class="custom-text">En combinant ces équations, on obtient le taux de variation de la population d’une espèce de l’écosystème. '
                'Illustrons ceci avec une espèce 2 ($E_2$) consommant une espèce 1 ($E_1$) et se faisant manger par les espèces 3 ($E_3$) et 4 ($E_4$) :<br><br>'
                '$\\frac{dE_2}{dt} = \\text{Terme de natalité } E_2 \\text{ par } E_1 - \\text{Terme de compétition } E_2 - '
                '\\text{Terme de décès } E_2 \\text{ par } E_3$<br>$- \\text{ Terme de décès } E_2 \\text{ par } E_4 - '
                '\\text{Terme de mortalité naturelle } E_2$<br><br><br></span>',
                unsafe_allow_html=True)

    st.markdown('<div class="custom-text">En faisant de même pour toutes les espèces, on crée un système d’équations différentielles qui relie l’évolution de toutes les '
        'populations d’un écosystème à travers le temps. Cependant, pour déterminer comment plusieurs espèces interagissent dans un environnement donné, il importe bien sûr de '
        'sélectionner un réseau trophique ! Celui pour lequel nous avons opté rassemble des insectes herbivores, des lézards, des coatis, des boas et des jaguars :</div>',
        unsafe_allow_html=True)

    st.markdown("""<div style="display: flex; justify-content: center; "> <img src="https://i.postimg.cc/vBW0GWVf/Schema-animaux.png" width="500"> </div> """, unsafe_allow_html=True)

    st.markdown('<div class="custom-text">Au niveau de la page de simulation, la portion supérieure sera consacrée au graphique du nombre d’individus de chaque espèce selon '
        'le temps. Ce graphique provient de la résolution algorithmique des équations différentielles tout juste abordées. L’utilisateur pourra ajuster, pour les espèces applicables, '
        'les paramètres suivants : la taille des portées, l’efficacité de prédation, l’efficacité de survie et la longévité dans des conditions optimales. Ces valeurs influenceront '
        'les cinq courbes affichées par le simulateur. Nous avons décidé d’associer au graphique ainsi produit une option ludique, dans laquelle l’utilisateur a pour but de choisir ses '
        'paramètres de telle sorte que les cinq populations de l’écosystème survivent à long terme. Pour ce faire, elles doivent demeurer à une valeur au-dessus du seuil d’extinction, '
        'fixé arbitrairement à 10 individus : lorsqu’une population comprend trop peu d’individus, le manque de diversité génétique résultant de la consanguinité mène à la déchéance '
        'd’une espèce. En s’aidant du graphique, l’utilisateur devra tenter d’assurer un équilibre des courbes 200 ans après le début de la simulation, c’est-à-dire bien au-delà de '
        'la plage de 20 ans affichée par le graphique. C’est là que réside le défi ! Quand il sera prêt à tester sa combinaison de paramètres, l’utilisateur n’aura qu’à cliquer sur '
        'le bouton «&nbspValider la viabilité&nbsp». Après cela, la vérification se fera de manière automatique jusqu’à ce que succès il y ait. Voici le bouton en question, qui apparaît '
        'dans le panneau latéral de la page de simulation :</div>',
        unsafe_allow_html=True)

    st.markdown("""<div style="display: flex; justify-content: center; margin-top: 40px; margin-bottom : 50px"> <img src="https://i.postimg.cc/QxNJ19t2/Bouton-simulateur-ecosysteme.png" width="100"> </div>""", unsafe_allow_html=True)

    st.markdown(
        '<div class="custom-text">La page de simulation fournit une multitude d’autres options de découverte, qui se concentrent sur l’analyse détaillée d’une année dont '
        'le choix revient à l’utilisateur. Au sein de celle-ci, ce sont les échanges énergétiques qui sont explorés, à partir de la différence entre l’énergie entrant dans une population '
        'et l’énergie en sortant. Pour un prédateur, l’énergie entrante équivaut à l’énergie perdue par ses proies à travers le terme de mortalité associé à la relation de prédation concernée, à '
        'laquelle on adjoint un coefficient correspondant au produit de l’efficacité d’ingestion et de l’efficacité d’assimilation. Pour la proie de base (les insectes), l’énergie entrante est '
        'simplement le produit du nombre de calories ingérées par jour, de l’efficacité alimentaire et du nombre d’individus. L’énergie sortante, pour sa part, correspond dans tous les cas au '
        'produit du nombre d’individus décédés (par prédation ou par mort naturelle) et de leur teneur calorique, auquel s’ajoute le terme du coût métabolique multiplié par le nombre d’individus. Tout '
        'compte fait, on réutilise certaines des équations ayant permis de calculer la variation des populations en y insérant les grandeurs obtenues lors de la résolution des équations '
        'différentielles, et on y ajoute quelques paramètres transformant une variation d’individus en une variation calorique. Ces informations concernant les flux énergétiques ont été utilisées '
        'de trois manières différentes. <i>En premier lieu</i>, elles ont servi à construire un bilan énergétique annuel, qui correspond à la différence entre l’énergie entrante et l’énergie '
        'sortante pour l’entièreté de la population sur l’échelle d’une année. Cette valeur est affichée, pour chaque espèce, dans un menu rétractable intitulé «&nbsp;Vue d’ensemble des '
        'résultats pour l’an <i>n</i>&nbsp;». <i>En deuxième lieu</i>, cinq graphiques représentent la variation calorique quotidienne pour les différentes espèces. On comprend ainsi que le bilan '
        'annuel pour une population donnée correspond à l’aire sous la courbe qui lui correspond. <i>En troisième lieu</i>, on retrouve un schéma illustrant les échanges énergétiques au sein des '
        'divers rapports de prédation. Chaque échange énergétique est représenté par le produit de l’énergie brute prélevée depuis une population et de l’efficacité alimentaire du prédateur. '
        'Si le flux énergétique est supérieur à celui de l’année précédente, la valeur est affichée dans une case verte ; si le flux est inférieur, la case est rouge&nbsp;; s’il n’y a pas d’année '
        'précédente (an 1), la case est grise.<br><br></div>',
        unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; font-size: 18px; font-weight: normal'><i>Nous tenons à remercier Magnific AI pour la création des sympathiques illustrations utilisées dans ce projet.</i></h1>", unsafe_allow_html=True)
