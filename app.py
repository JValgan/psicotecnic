"""
PSICOTÈCNIC 3 EN 1 - Aplicació completa en Python amb Tkinter
Conversió del codi JavaScript original
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import time
import json
from PIL import Image, ImageTk
import os
import threading

# ==============================================================
# BASE DE DADES DE PREGUNTES (COMPLETA)
# ==============================================================

PROBLEM_BANK = {
    'calcul': {
        'easy': [
            {'q': 'Quant és 8 + 3 × 2 ?', 'options': ['22', '14', '19', '16'], 'correct': 1},
            {'q': 'Quant és (6 + 4) × 3 ?', 'options': ['30', '26', '34', '28'], 'correct': 0},
            {'q': 'Quant és 12 − 4 ÷ 2 ?', 'options': ['4', '10', '8', '6'], 'correct': 1},
            {'q': 'Quant és 15 − 3 × 4 + 2 ?', 'options': ['5', '9', '7', '11'], 'correct': 0},
            {'q': 'Quant és 20 ÷ (2 + 3) ?', 'options': ['4', '5', '8', '10'], 'correct': 0},
            {'q': 'Quin és el 20% de 80 ?', 'options': ['12', '16', '18', '20'], 'correct': 1},
            {'q': 'Quin és el 35% de 200 ?', 'options': ['60', '70', '75', '80'], 'correct': 1},
            {'q': 'Si un producte costa 40 € i té un 25% de descompte, quant paguem?', 'options': ['30 €', '28 €', '32 €', '35 €'], 'correct': 0},
            {'q': 'El 15% de 300 és:', 'options': ['45', '50', '40', '55'], 'correct': 0},
            {'q': 'Si 3 kg de pomes costen 6 €, quant costen 5 kg?', 'options': ['8 €', '10 €', '12 €', '9 €'], 'correct': 1},
            {'q': 'Un cotxe consumeix 8 L cada 100 km. Quants litres per a 250 km?', 'options': ['18 L', '20 L', '22 L', '24 L'], 'correct': 1},
            {'q': 'Si 4 treballadors fan una feina en 6 hores, quant trigaran 8 treballadors?', 'options': ['3 h', '4 h', '5 h', '2 h'], 'correct': 0},
            {'q': 'Si 2 persones pinten una casa en 12 hores, quant trigaran 4 persones?', 'options': ['6 h', '8 h', '5 h', '4 h'], 'correct': 0},
            {'q': 'Quant és 2³ + 4 ?', 'options': ['10', '12', '14', '8'], 'correct': 1},
            {'q': 'La meitat de 3/4 és:', 'options': ['1/4', '3/8', '1/2', '2/3'], 'correct': 1},
            {'q': 'Un rectangle fa 6 cm d\'ample i 8 cm de llarg. Quin és el perímetre?', 'options': ['24 cm', '28 cm', '30 cm', '32 cm'], 'correct': 1},
            {'q': 'L\'àrea d\'un quadrat de 5 cm de costat és:', 'options': ['20 cm²', '25 cm²', '30 cm²', '15 cm²'], 'correct': 1},
            {'q': 'Quina és la mitjana de 4, 8, 6 ?', 'options': ['5', '6', '7', '4'], 'correct': 1},
            {'q': 'Quants minuts hi ha en 2,5 hores?', 'options': ['120', '150', '180', '100'], 'correct': 1},
        ],
        'medium': [
            {'q': 'Quant és 1.250 + 3.750 × 2 ?', 'options': ['8.750', '7.500', '10.000', '6.250'], 'correct': 0},
            {'q': 'Quant és (4.800 + 1.200) × 3 ?', 'options': ['15.000', '16.000', '17.000', '18.000'], 'correct': 3},
            {'q': 'Quant és 12.500 − 4.800 ÷ 4 ?', 'options': ['10.100', '10.300', '10.500', '10.700'], 'correct': 2},
            {'q': 'Quant és (2.400 × 3) + (1.800 × 2) ?', 'options': ['10.800', '10.200', '11.400', '9.600'], 'correct': 0},
            {'q': 'Quin és el 17,5% de 800 ?', 'options': ['120', '130', '140', '150'], 'correct': 2},
            {'q': 'Quin és el 22,5% de 1.200 ?', 'options': ['250', '260', '270', '280'], 'correct': 2},
            {'q': 'Si un producte costa 850 € i té un 18% de descompte, quant paguem?', 'options': ['687 €', '697 €', '707 €', '717 €'], 'correct': 1},
            {'q': 'Quin percentatge representa 234 sobre 1.300 ?', 'options': ['16%', '17%', '18%', '19%'], 'correct': 2},
            {'q': 'El 32% de 2.500 és:', 'options': ['700', '750', '800', '850'], 'correct': 2},
            {'q': 'Si 12 kg de pomes costen 78 €, quant costen 18 kg?', 'options': ['112 €', '115 €', '117 €', '120 €'], 'correct': 2},
            {'q': 'Un cotxe consumeix 9,5 L cada 100 km. Quants litres per a 450 km?', 'options': ['40,75 L', '41,75 L', '42,75 L', '43,75 L'], 'correct': 2},
            {'q': 'Si 15 treballadors fan una feina en 8 hores, quant trigaran 25 treballadors?', 'options': ['4,6 h', '4,8 h', '5 h', '5,2 h'], 'correct': 1},
            {'q': 'Si 4 persones pinten una casa en 15 hores, quant trigaran 6 persones?', 'options': ['8 h', '9 h', '10 h', '12 h'], 'correct': 2},
            {'q': 'Si 5 màquines fan una comanda en 12 dies, 8 màquines trigaran?', 'options': ['7 dies', '7,5 dies', '8 dies', '8,5 dies'], 'correct': 1},
            {'q': 'Compras 5 articles de 24,50 € cadascun, però et fan un 15% de descompte. Quant pagues?', 'options': ['99,13 €', '104,13 €', '109,13 €', '114,13 €'], 'correct': 1},
            {'q': 'Quin és el 20% del 30% de 1.500 ?', 'options': ['80', '85', '90', '95'], 'correct': 2},
            {'q': 'L\'àrea d\'un triangle amb base 8,5 cm i altura 6,4 cm és:', 'options': ['27,2 cm²', '28,4 cm²', '29,6 cm²', '30,8 cm²'], 'correct': 0},
        ],
        'hard': [
            {'q': 'Quant és 2.500 × 1.2 + 3.000 × 0.8 ?', 'options': ['5.200', '5.400', '5.600', '5.800'], 'correct': 1},
            {'q': 'Quant és (8.500 − 3.200) × 0.75 ?', 'options': ['3.975', '4.125', '4.275', '4.425'], 'correct': 0},
            {'q': 'Quant és 1.250 + 750 × (2.000 − 1.500) ?', 'options': ['375.000', '376.250', '375.750', '376.000'], 'correct': 1},
            {'q': 'Quin és el 37,5% de 2.400 ?', 'options': ['850', '875', '900', '925'], 'correct': 2},
            {'q': 'Si 450 € és el 18% d\'una quantitat, quina és la quantitat total?', 'options': ['2.400 €', '2.450 €', '2.500 €', '2.550 €'], 'correct': 2},
            {'q': 'Un producte puja un 12% i val 1.008 €. Quant valia abans?', 'options': ['880 €', '890 €', '900 €', '910 €'], 'correct': 2},
            {'q': 'Si 9 metres de tela costen 67,50 €, quant costen 15 metres?', 'options': ['110,50 €', '112,50 €', '114,50 €', '116,50 €'], 'correct': 1},
            {'q': 'Una màquina produeix 450 peces en 5 hores. Quantes en produirà en 8 hores?', 'options': ['680', '700', '720', '740'], 'correct': 2},
            {'q': 'Per omplir una piscina, 6 aixetes triguen 8 hores. Quantes hores trigaran 4 aixetes?', 'options': ['10 h', '11 h', '12 h', '14 h'], 'correct': 2},
            {'q': 'Si 10 persones fan una feina en 6 dies, quant trigaran 15 persones?', 'options': ['3 dies', '4 dies', '5 dies', '6 dies'], 'correct': 1},
            {'q': 'Un cotxe consumeix 7,2 L/100km en ciutat i 5,8 L/100km en carretera. Quants litres consumeix en un viatge de 150 km per ciutat i 200 km per carretera?', 'options': ['21,8 L', '22,4 L', '22,8 L', '23,2 L'], 'correct': 1},
            {'q': 'Un producte val 1.500 €, puja un 8% i després baixa un 5%. Quin és el preu final?', 'options': ['1.534 €', '1.539 €', '1.544 €', '1.549 €'], 'correct': 1},
            {'q': 'Un article té dos descomptes: 10% i 15%. Si val 600 €, quant pagues finalment?', 'options': ['450 €', '459 €', '468 €', '477 €'], 'correct': 1},
            {'q': 'Un terreny de 2.500 m² es divideix: 45% per a jardí, 35% per a edifici i la resta per a piscina. Quants m² té la piscina?', 'options': ['450 m²', '475 m²', '500 m²', '525 m²'], 'correct': 2},
            {'q': 'Quin és el 15% de 2.400 més el 8% de 1.800 ?', 'options': ['480', '490', '500', '510'], 'correct': 2},
            {'q': 'Si 25 treballadors fan una feina en 10 dies, quants treballadors es necessiten per fer-la en 6 dies?', 'options': ['38', '40', '42', '44'], 'correct': 2},
        ]
    },
    'catala': {
        'easy': [
            {'q': 'Quin és el sinònim de "content"?', 'options': ['Trist', 'Alegre', 'Enfadat', 'Cansat'], 'correct': 1},
            {'q': 'Quin és el sinònim de "ràpid"?', 'options': ['Lent', 'Veloç', 'Pausat', 'Feixuc'], 'correct': 1},
            {'q': 'Quin és el sinònim de "gran"?', 'options': ['Petit', 'Menut', 'Gros', 'Estret'], 'correct': 2},
            {'q': 'Quin és el sinònim de "bonic"?', 'options': ['Lleig', 'Maco', 'Trist', 'Fosc'], 'correct': 1},
            {'q': 'Quin és el sinònim de "feliç"?', 'options': ['Trist', 'Avalotat', 'Content', 'Enfadat'], 'correct': 2},
            {'q': 'Quin és l\'antònim de "alt"?', 'options': ['Baix', 'Gran', 'Llarg', 'Estret'], 'correct': 0},
            {'q': 'Quin és l\'antònim de "clar"?', 'options': ['Lluent', 'Fosc', 'Tènue', 'Brillant'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "fort"?', 'options': ['Dèbil', 'Poderós', 'Robust', 'Enèrgic'], 'correct': 0},
            {'q': 'Quin és l\'antònim de "dolç"?', 'options': ['Salat', 'Amarg', 'Àcid', 'Picant'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "ple"?', 'options': ['Omplert', 'Buit', 'Saturat', 'Farcit'], 'correct': 1},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Ajudar', 'Ajjudar', 'Ajuddar', 'Ajuddà'], 'correct': 0},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Vaixell', 'Vaxell', 'Vaixell', 'Vaixell'], 'correct': 1},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Exemple', 'Eixemple', 'Exxemple', 'Exenple'], 'correct': 0},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Pijama', 'Pijamma', 'Pigama', 'Pijamà'], 'correct': 2},
            {'q': 'Avi és a vell com...', 'options': ['Nen és a jove', 'Jove és a gran', 'Vell és a jove', 'Nen és a gran'], 'correct': 0},
            {'q': 'Aigua és a líquid com...', 'options': ['Gel és a gas', 'Vapor és a líquid', 'Gel és a sòlid', 'Vapor és a gas'], 'correct': 2},
            {'q': 'Gos és a lladrar com...', 'options': ['Gat és a bordar', 'Gat és a miolar', 'Vaca és a udolar', 'Ocell és a nedar'], 'correct': 1},
            {'q': 'Què vol dir "efímer"?', 'options': ['Que dura molt', 'Que dura poc', 'Que és etern', 'Que és gran'], 'correct': 1},
            {'q': 'Què vol dir "càndid"?', 'options': ['Astut', 'Innocent', 'Trist', 'Alegre'], 'correct': 1},
            {'q': 'Què vol dir "àrid"?', 'options': ['Humit', 'Sec', 'Fèrtil', 'Verd'], 'correct': 1},
        ],
        'medium': [
            {'q': 'Quin és el sinònim de "tranquil"?', 'options': ['Nerviós', 'Agitat', 'Calmat', 'Intranquil'], 'correct': 2},
            {'q': 'Quin és el sinònim de "caminar"?', 'options': ['Córrer', 'Marxar', 'Saltar', 'Jeure'], 'correct': 1},
            {'q': 'Quin és el sinònim de "parlar"?', 'options': ['Callar', 'Xerrar', 'Cridar', 'Xiuxiuejar'], 'correct': 1},
            {'q': 'Quin és el sinònim de "treballar"?', 'options': ['Dormir', 'Laborar', 'Jugar', 'Descansar'], 'correct': 1},
            {'q': 'Quin és el sinònim de "amable"?', 'options': ['Rude', 'Cortès', 'Trist', 'Alegre'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "càlid"?', 'options': ['Tebi', 'Fred', 'Escalfat', 'Cremós'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "suau"?', 'options': ['Rugós', 'Tou', 'Lliscant', 'Vellutat'], 'correct': 0},
            {'q': 'Quin és l\'antònim de "llarg"?', 'options': ['Ample', 'Alt', 'Curt', 'Estret'], 'correct': 2},
            {'q': 'Quin és l\'antònim de "profund"?', 'options': ['Fondal', 'Superficial', 'Avançat', 'Fosc'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "generós"?', 'options': ['Liberal', 'Gelós', 'Avar', 'Trist'], 'correct': 2},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Excepcional', 'Exepcional', 'Excepcionàl', 'Excepçional'], 'correct': 1},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Innecessari', 'Innesessari', 'Innecessari', 'Innecessari'], 'correct': 1},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Exhaurir', 'Exaurir', 'Exhaurir', 'Exhaurir'], 'correct': 1},
            {'q': 'Mestre és a ensenyar com...', 'options': ['Metge és a curar', 'Pintor és a cantar', 'Arquitecte és a cuinar', 'Escriptor és a ballar'], 'correct': 0},
            {'q': 'Ull és a veure com...', 'options': ['Orella és a escoltar', 'Orella és a veure', 'Nas és a tocar', 'Boca és a olorar'], 'correct': 0},
            {'q': 'Llibre és a llegir com...', 'options': ['Pel·lícula és a mirar', 'Música és a escriure', 'Quadre és a dibuixar', 'Carta és a enviar'], 'correct': 0},
            {'q': 'Sol és a dia com...', 'options': ['Lluna és a nit', 'Lluna és a dia', 'Estel és a nit', 'Estel és a dia'], 'correct': 0},
            {'q': 'Què vol dir "fugac"?', 'options': ['Que dura molt', 'Que passa ràpid', 'Que és fort', 'Que és feble'], 'correct': 1},
            {'q': 'Què vol dir "lúcid"?', 'options': ['Fosc', 'Clar', 'Nebulós', 'Tèrbol'], 'correct': 1},
            {'q': 'Què vol dir "tènue"?', 'options': ['Fort', 'Dèbil', 'Lluent', 'Fosc'], 'correct': 1},
            {'q': 'Què vol dir "fèrtil"?', 'options': ['Àrid', 'Productiu', 'Estèril', 'Pobre'], 'correct': 1},
        ],
        'hard': [
            {'q': 'Quin és el sinònim de "efusiu"?', 'options': ['Tímid', 'Expansiu', 'Serè', 'Fred'], 'correct': 1},
            {'q': 'Quin és el sinònim de "obstinat"?', 'options': ['Flexible', 'Testarut', 'Dèbil', 'Indecís'], 'correct': 1},
            {'q': 'Quin és el sinònim de "lúgubre"?', 'options': ['Alegre', 'Trist', 'Viu', 'Animós'], 'correct': 1},
            {'q': 'Quin és el sinònim de "perniciós"?', 'options': ['Benèfic', 'Nociu', 'Innocent', 'Saludable'], 'correct': 1},
            {'q': 'Quin és el sinònim de "efímer"?', 'options': ['Etern', 'Fugac', 'Perenne', 'Durader'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "perniciós"?', 'options': ['Nociu', 'Benèfic', 'Tòxic', 'Mortal'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "lúgubre"?', 'options': ['Trist', 'Alegre', 'Fosc', 'Pesat'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "efusiu"?', 'options': ['Expansiu', 'Tímid', 'Càlid', 'Afectuós'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "fèrtil"?', 'options': ['Productiu', 'Estèril', 'Fecund', 'Prolífic'], 'correct': 1},
            {'q': 'Quin és l\'antònim de "lúcid"?', 'options': ['Clar', 'Tèrbol', 'Nítid', 'Diàfan'], 'correct': 1},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Conseguir', 'Consseguir', 'Conseguir', 'Conseguir'], 'correct': 1},
            {'q': 'Quina paraula està mal escrita?', 'options': ['Oportunitat', 'Oportunitat', 'Oportunitat', 'Oportunitat'], 'correct': 0},
            {'q': 'Aeroport és a avió com...', 'options': ['Estació és a tren', 'Port és a cotxe', 'Aeroport és a vaixell', 'Estació és a autobús'], 'correct': 0},
            {'q': 'Pluja és a paraigua com...', 'options': ['Sol és a barret', 'Neva és a abric', 'Vent és a paraigua', 'Calor és a barret'], 'correct': 0},
            {'q': 'Peix és a aigua com...', 'options': ['Ocell és a cel', 'Ocell és a terra', 'Peix és a terra', 'Ocell és a mar'], 'correct': 0},
            {'q': 'Músic és a orquestra com...', 'options': ['Actor és a teatre', 'Actor és a pel·lícula', 'Actor és a escenari', 'Actor és a obra'], 'correct': 0},
            {'q': 'Reloj és a hora com...', 'options': ['Calendari és a any', 'Calendari és a mes', 'Calendari és a dia', 'Calendari és a setmana'], 'correct': 2},
            {'q': 'Què vol dir "imminent"?', 'options': ['Que ja ha passat', 'Que està a punt de passar', 'Que és llunyà', 'Que és improbable'], 'correct': 1},
            {'q': 'Què vol dir "obstinat"?', 'options': ['Flexible', 'Testarut', 'Dèbil', 'Indecís'], 'correct': 1},
            {'q': 'Què vol dir "perniciós"?', 'options': ['Benèfic', 'Nociu', 'Innocent', 'Saludable'], 'correct': 1},
            {'q': 'Què vol dir "lúgubre"?', 'options': ['Alegre', 'Trist', 'Viu', 'Animós'], 'correct': 1},
            {'q': 'Què vol dir "efusiu"?', 'options': ['Tímid', 'Expansiu', 'Serè', 'Fred'], 'correct': 1},
        ]
    }
}

# ==============================================================
# INSTRUCCIONS PER MÒDUL
# ==============================================================

MODULE_INSTRUCTIONS = {
    'calcul': {
        'title': '📐 Càlcul · Matemàtiques',
        'items': [
            ('➕', 'Resol <strong>operacions combinades</strong> amb prioritat'),
            ('💯', 'Calcula <strong>percentatges</strong> i descomptes'),
            ('📊', 'Aplica <strong>regles de 3</strong> directes i inverses'),
            ('📏', 'Resol problemes de <strong>geometria</strong> i mitjanes')
        ],
        'footer': '⏱ Tens temps limitat · 3 nivells de dificultat'
    },
    'catala': {
        'title': '📚 Català · Llengua',
        'items': [
            ('🔤', 'Tria el <strong>sinònim</strong> correcte de cada paraula'),
            ('🔄', 'Identifica l\'<strong>antònim</strong> adequat'),
            ('✍️', 'Detecta paraules <strong>mal escrites</strong>'),
            ('🧩', 'Completa <strong>analogies</strong> i relaciona conceptes'),
            ('📖', 'Tria la <strong>definició</strong> correcta de paraules')
        ],
        'footer': '⏱ Temps limitat · 3 nivells de dificultat · Basat en fonts oficials'
    },
    'memoritzacio': {
        'title': '👁️ Memorització · Visual',
        'items': [
            ('🖼️', 'Carrega una <strong>imatge</strong> amb text a memoritzar'),
            ('⏱️', 'Mira la imatge durant el <strong>temps indicat</strong>'),
            ('📝', 'Pren <strong>notes</strong> mentre mires la imatge'),
            ('✍️', 'Escriu tot el que <strong>recordes</strong> de la imatge'),
            ('🔍', 'Compara el teu text amb la <strong>imatge original</strong>')
        ],
        'footer': '👀 Entrena la teva memòria visual i capacitat de retenció'
    }
}

# ==============================================================
# CLASSE PRINCIPAL DE L'APLICACIÓ
# ==============================================================

class PsicotecnicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Psicotècnic 3 en 1")
        self.root.geometry("1000x750")
        self.root.configure(bg='#F5F8FC')
        self.root.minsize(800, 600)
        
        # Estat
        self.current_module = 'calcul'
        self.current_level = 'easy'
        self.questions = []
        self.user_answers = []
        self.current_index = 0
        self.score = 0
        self.total_questions = 0
        self.is_finished = False
        self.is_answered = False
        self.timer_running = False
        self.time_left = 120
        self.timer_id = None
        
        # Estat per a memorització
        self.image_path = None
        self.image_url = None
        self.notes = ''
        self.memorization_phase = 'idle'  # idle | memorization | writing | results
        
        # Configuració colors
        self.colors = {
            'primary': '#4A90D9',
            'primary_dark': '#3A7BC8',
            'primary_light': '#7BB3E6',
            'success': '#00B894',
            'danger': '#FF6B6B',
            'warning': '#FDCB6E',
            'bg': '#F5F8FC',
            'white': '#FFFFFF',
            'text': '#2D3436',
            'text_light': '#636E72',
            'border': '#DFE6E9'
        }
        
        # Crear interfície
        self.create_widgets()
        
        # Iniciar en mode pràctica
        self.current_page = 'home'
        self.show_home()
    
    # ==============================================================
    # CREACIÓ DE LA INTERFÍCIE
    # ==============================================================
    
    def create_widgets(self):
        """Crea tots els widgets de l'aplicació"""
        
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # === HEADER ===
        self.header = tk.Frame(self.main_frame, bg='white', height=70)
        self.header.pack(fill='x', pady=(0, 15))
        self.header.pack_propagate(False)
        
        header_left = tk.Frame(self.header, bg='white')
        header_left.pack(side='left', padx=20, fill='y')
        
        self.header_icon = tk.Label(header_left, text='🧠', font=('Inter', 24), bg='white')
        self.header_icon.pack(side='left', padx=(0, 10))
        
        self.header_title = tk.Label(header_left, text='Psicotècnic 3 en 1', 
                                     font=('Inter', 18, 'bold'), bg='white', 
                                     fg=self.colors['text'])
        self.header_title.pack(side='left')
        
        # === CONTENIDOR PRINCIPAL ===
        self.content_frame = tk.Frame(self.main_frame, bg='white', 
                                      relief='flat', bd=1)
        self.content_frame.pack(fill='both', expand=True, pady=10)
        
        # Aquest frame contindrà tot el contingut dinàmic
        self.dynamic_frame = tk.Frame(self.content_frame, bg='white')
        self.dynamic_frame.pack(fill='both', expand=True, padx=20, pady=15)
    
    # ==============================================================
    # NAVEGACIÓ ENTRE PÀGINES
    # ==============================================================
    
    def clear_content(self):
        """Neteja el contingut del frame dinàmic"""
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()
    
    def show_home(self):
        """Mostra la pàgina d'inici"""
        self.clear_content()
        self.current_page = 'home'
        
        # Títol
        title = tk.Label(self.dynamic_frame, text='🎯 Què vols practicar?',
                         font=('Inter', 20, 'bold'), bg='white', fg=self.colors['text'])
        title.pack(pady=(10, 5))
        
        subtitle = tk.Label(self.dynamic_frame, text='Selecciona una opció per començar',
                            font=('Inter', 14), bg='white', fg=self.colors['text_light'])
        subtitle.pack(pady=(0, 20))
        
        # Grid de cards
        grid_frame = tk.Frame(self.dynamic_frame, bg='white')
        grid_frame.pack(fill='both', expand=True)
        
        cards = [
            ('📝', 'Pràctica', 'Exercicis interactius de Càlcul, Català i Memorització', 'practica'),
            ('📐', 'Matemàtiques', 'Conceptes i fórmules per resoldre els exercicis', 'teoria'),
            ('📝', 'Ortografia', 'Regles i normes per escriure correctament en català', 'ortografia')
        ]
        
        for i, (icon, title_text, desc, page) in enumerate(cards):
            frame = tk.Frame(grid_frame, bg='white', relief='ridge', bd=1)
            frame.grid(row=0, column=i, padx=10, pady=10, sticky='nsew')
            grid_frame.grid_columnconfigure(i, weight=1)
            
            # Icona
            icon_label = tk.Label(frame, text=icon, font=('Inter', 36), bg='white')
            icon_label.pack(pady=(15, 5))
            
            # Títol
            title_label = tk.Label(frame, text=title_text, font=('Inter', 16, 'bold'),
                                   bg='white', fg=self.colors['text'])
            title_label.pack()
            
            # Descripció
            desc_label = tk.Label(frame, text=desc, font=('Inter', 11),
                                  bg='white', fg=self.colors['text_light'],
                                  wraplength=200, justify='center')
            desc_label.pack(pady=(5, 10))
            
            # Botó
            btn = tk.Button(frame, text='▶ Començar' if page == 'practica' else '📖 Consultar',
                            bg=self.colors['primary'], fg='white',
                            font=('Inter', 10, 'bold'), relief='flat',
                            padx=20, pady=5, cursor='hand2',
                            command=lambda p=page: self.go_to_page(p))
            btn.pack(pady=(0, 15))
            
            # Efecte hover
            def on_enter(e, f=frame):
                f.configure(bg='#F8FAFC')
            def on_leave(e, f=frame):
                f.configure(bg='white')
            
            frame.bind('<Enter>', on_enter)
            frame.bind('<Leave>', on_leave)
    
    def go_to_page(self, page):
        """Navega a una pàgina específica"""
        if page == 'practica':
            self.show_practica()
        elif page == 'teoria':
            self.show_teoria()
        elif page == 'ortografia':
            self.show_ortografia()
        elif page == 'home':
            self.show_home()
    
    # ==============================================================
    # PÀGINA: PRÀCTICA
    # ==============================================================
    
    def show_practica(self):
        """Mostra la pàgina de pràctica"""
        self.clear_content()
        self.current_page = 'practica'
        
        # Botó tornar
        self.create_back_button()
        
        # Instruccions
        self.create_instructions('calcul')
        
        # Configuració
        self.create_config()
        
        # Zona de preguntes
        self.create_question_area()
    
    def create_back_button(self):
        """Crea el botó per tornar enrere"""
        back_frame = tk.Frame(self.dynamic_frame, bg='white')
        back_frame.pack(fill='x', pady=(0, 10))
        
        btn = tk.Button(back_frame, text='← Tornar al menú',
                        bg='white', fg=self.colors['primary'],
                        font=('Inter', 11, 'bold'), relief='flat',
                        cursor='hand2', command=lambda: self.go_to_page('home'))
        btn.pack(side='left')
    
    def create_instructions(self, module):
        """Crea les instruccions per al mòdul actual"""
        instr_frame = tk.Frame(self.dynamic_frame, bg='#F0F6FE', 
                               relief='flat', bd=1)
        instr_frame.pack(fill='x', pady=(0, 15), ipady=10, ipadx=10)
        
        data = MODULE_INSTRUCTIONS.get(module, MODULE_INSTRUCTIONS['calcul'])
        
        # Títol
        title = tk.Label(instr_frame, text=f'💡 {data["title"]}',
                         font=('Inter', 12, 'bold'), bg='#F0F6FE',
                         fg=self.colors['primary_dark'])
        title.pack(anchor='w', padx=10, pady=(5, 5))
        
        # Items en grid
        grid_frame = tk.Frame(instr_frame, bg='#F0F6FE')
        grid_frame.pack(fill='x', padx=10, pady=5)
        
        for i, (emoji, text) in enumerate(data['items']):
            row = i // 2
            col = i % 2
            item_frame = tk.Frame(grid_frame, bg='#F0F6FE')
            item_frame.grid(row=row, column=col, sticky='w', padx=5, pady=2)
            
            emoji_label = tk.Label(item_frame, text=emoji, font=('Inter', 12),
                                   bg='#F0F6FE')
            emoji_label.pack(side='left')
            
            # Eliminar etiquetes HTML i posar en negreta
            clean_text = text.replace('<strong>', '').replace('</strong>', '')
            text_label = tk.Label(item_frame, text=clean_text,
                                  font=('Inter', 10), bg='#F0F6FE',
                                  fg=self.colors['text'])
            text_label.pack(side='left', padx=(5, 0))
        
        # Footer
        footer = tk.Label(instr_frame, text=data['footer'],
                          font=('Inter', 9, 'italic'), bg='#F0F6FE',
                          fg=self.colors['text_light'])
        footer.pack(anchor='w', padx=10, pady=(5, 0))
    
    def create_config(self):
        """Crea la barra de configuració"""
        config_frame = tk.Frame(self.dynamic_frame, bg=self.colors['bg'],
                                relief='flat', bd=1)
        config_frame.pack(fill='x', pady=(0, 15), ipady=10, ipadx=10)
        
        # Selector de mòdul
        module_frame = tk.Frame(config_frame, bg=self.colors['bg'])
        module_frame.pack(side='left', padx=5)
        
        tk.Label(module_frame, text='Mòdul:', font=('Inter', 10, 'bold'),
                 bg=self.colors['bg'], fg=self.colors['text_light']).pack(side='left', padx=(0, 5))
        
        modules = [
            ('📐 Càlcul', 'calcul'),
            ('📚 Català', 'catala'),
            ('👁️ Memorització', 'memoritzacio')
        ]
        
        self.module_buttons = {}
        for text, module_id in modules:
            btn = tk.Button(module_frame, text=text,
                            bg=self.colors['primary'] if module_id == self.current_module else 'white',
                            fg='white' if module_id == self.current_module else self.colors['text'],
                            font=('Inter', 9), relief='flat',
                            padx=12, pady=4, cursor='hand2',
                            command=lambda m=module_id: self.change_module(m))
            btn.pack(side='left', padx=2)
            self.module_buttons[module_id] = btn
        
        # Separador
        tk.Frame(config_frame, bg=self.colors['border'], width=2, height=30).pack(side='left', padx=10)
        
        # Configuració per a cada mòdul
        self.config_items_frame = tk.Frame(config_frame, bg=self.colors['bg'])
        self.config_items_frame.pack(side='left', padx=5)
        
        self.update_config_items()
        
        # Botó començar
        self.start_btn = tk.Button(config_frame, text='▶ Començar',
                                   bg=self.colors['primary'], fg='white',
                                   font=('Inter', 11, 'bold'), relief='flat',
                                   padx=25, pady=6, cursor='hand2',
                                   command=self.start_quiz)
        self.start_btn.pack(side='right', padx=5)
    
    def update_config_items(self):
        """Actualitza els elements de configuració segons el mòdul"""
        for widget in self.config_items_frame.winfo_children():
            widget.destroy()
        
        if self.current_module == 'memoritzacio':
            # Configuració per a memorització
            # Imatge
            img_frame = tk.Frame(self.config_items_frame, bg=self.colors['bg'])
            img_frame.pack(side='left', padx=5)
            
            tk.Label(img_frame, text='Imatge:', font=('Inter', 9, 'bold'),
                     bg=self.colors['bg'], fg=self.colors['text_light']).pack(side='left')
            
            self.image_btn = tk.Button(img_frame, text='📂 Seleccionar',
                                       bg=self.colors['primary'], fg='white',
                                       font=('Inter', 8), relief='flat',
                                       padx=10, pady=3, cursor='hand2',
                                       command=self.select_image)
            self.image_btn.pack(side='left', padx=(5, 0))
            
            self.image_label = tk.Label(img_frame, text='Cap imatge',
                                        font=('Inter', 8), bg=self.colors['bg'],
                                        fg=self.colors['text_light'])
            self.image_label.pack(side='left', padx=(5, 0))
            
            # Temps de visualització
            time_frame = tk.Frame(self.config_items_frame, bg=self.colors['bg'])
            time_frame.pack(side='left', padx=10)
            
            tk.Label(time_frame, text='Visualització (s):', font=('Inter', 9, 'bold'),
                     bg=self.colors['bg'], fg=self.colors['text_light']).pack(side='left')
            
            self.view_entry = tk.Entry(time_frame, width=5, font=('Inter', 10),
                                       relief='solid', bd=1, justify='center')
            self.view_entry.insert(0, '30')
            self.view_entry.pack(side='left', padx=(5, 0))
        
        else:
            # Configuració per a Càlcul i Català
            # Preguntes
            q_frame = tk.Frame(self.config_items_frame, bg=self.colors['bg'])
            q_frame.pack(side='left', padx=5)
            
            tk.Label(q_frame, text='Preguntes:', font=('Inter', 9, 'bold'),
                     bg=self.colors['bg'], fg=self.colors['text_light']).pack(side='left')
            
            self.q_entry = tk.Entry(q_frame, width=5, font=('Inter', 10),
                                    relief='solid', bd=1, justify='center')
            self.q_entry.insert(0, '10')
            self.q_entry.pack(side='left', padx=(5, 0))
            
            # Temps
            time_frame = tk.Frame(self.config_items_frame, bg=self.colors['bg'])
            time_frame.pack(side='left', padx=10)
            
            tk.Label(time_frame, text='Temps (min):', font=('Inter', 9, 'bold'),
                     bg=self.colors['bg'], fg=self.colors['text_light']).pack(side='left')
            
            self.t_entry = tk.Entry(time_frame, width=5, font=('Inter', 10),
                                    relief='solid', bd=1, justify='center')
            self.t_entry.insert(0, '2')
            self.t_entry.pack(side='left', padx=(5, 0))
            
            # Nivell
            level_frame = tk.Frame(self.config_items_frame, bg=self.colors['bg'])
            level_frame.pack(side='left', padx=10)
            
            tk.Label(level_frame, text='Nivell:', font=('Inter', 9, 'bold'),
                     bg=self.colors['bg'], fg=self.colors['text_light']).pack(side='left')
            
            self.level_var = tk.StringVar(value='easy')
            levels = [('🟢 Fàcil', 'easy'), ('🟡 Mitjà', 'medium'), ('🔴 Difícil', 'hard')]
            
            for text, value in levels:
                rb = tk.Radiobutton(level_frame, text=text, variable=self.level_var,
                                    value=value, bg=self.colors['bg'],
                                    font=('Inter', 8), selectcolor='white',
                                    activebackground=self.colors['bg'])
                rb.pack(side='left', padx=3)
    
    def change_module(self, module):
        """Canvia el mòdul actiu"""
        self.current_module = module
        self.reset_state()
        
        # Actualitzar botons
        for mod_id, btn in self.module_buttons.items():
            if mod_id == module:
                btn.configure(bg=self.colors['primary'], fg='white')
            else:
                btn.configure(bg='white', fg=self.colors['text'])
        
        # Actualitzar config
        self.update_config_items()
        
        # Actualitzar instruccions
        self.create_instructions(module)
    
    def select_image(self):
        """Selecciona una imatge per a memorització"""
        file_path = filedialog.askopenfilename(
            title='Selecciona una imatge',
            filetypes=[('Imatges', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Tots els fitxers', '*.*')]
        )
        if file_path:
            self.image_path = file_path
            self.image_label.config(text=os.path.basename(file_path), fg=self.colors['success'])
    
    # ==============================================================
    # ZONA DE PREGUNTES
    # ==============================================================
    
    def create_question_area(self):
        """Crea l'àrea on es mostraran les preguntes"""
        # Aquesta àrea es neteja i omple dinàmicament
        self.question_frame = tk.Frame(self.dynamic_frame, bg='white',
                                       relief='flat', bd=1)
        self.question_frame.pack(fill='both', expand=True)
        
        self.question_label = tk.Label(self.question_frame,
                                       text='Selecciona un mòdul i prem "Començar"',
                                       font=('Inter', 14), bg='white',
                                       fg=self.colors['text_light'])
        self.question_label.pack(pady=50)
        
        self.options_frame = tk.Frame(self.question_frame, bg='white')
        self.options_frame.pack(pady=10)
        
        # Feedback bar
        self.feedback_frame = tk.Frame(self.question_frame, bg='white')
        self.feedback_frame.pack(fill='x', pady=10)
        
        self.progress_label = tk.Label(self.feedback_frame, text='0 / 0',
                                       font=('Inter', 10), bg='white',
                                       fg=self.colors['text_light'])
        self.progress_label.pack(side='left', padx=10)
        
        self.timer_label = tk.Label(self.feedback_frame, text='⏱ 0:00',
                                    font=('Inter', 10), bg='white',
                                    fg=self.colors['text'])
        self.timer_label.pack(side='right', padx=10)
    
    # ==============================================================
    # LÒGICA DEL QUIZ
    # ==============================================================
    
    def reset_state(self):
        """Reinicia l'estat de l'aplicació"""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        self.timer_running = False
        self.is_finished = False
        self.current_index = 0
        self.user_answers = []
        self.questions = []
        self.score = 0
        self.total_questions = 0
        self.is_answered = False
        
        # Netejar zona de preguntes
        self.clear_question_area()
    
    def clear_question_area(self):
        """Neteja l'àrea de preguntes"""
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.question_label.config(text='Selecciona un mòdul i prem "Començar"')
        self.progress_label.config(text='0 / 0')
        self.timer_label.config(text='⏱ 0:00')
        self.start_btn.config(state='normal')
    
    def start_quiz(self):
        """Inicia el qüestionari"""
        if self.current_module == 'memoritzacio':
            self.start_memorization()
            return
        
        try:
            num_q = int(self.q_entry.get())
            minutes = int(self.t_entry.get())
            level = self.level_var.get()
        except:
            messagebox.showerror('Error', 'Si us plau, introdueix números vàlids')
            return
        
        # Seleccionar preguntes
        bank = PROBLEM_BANK[self.current_module][level]
        self.questions = random.sample(bank, min(num_q, len(bank)))
        self.total_questions = len(self.questions)
        self.user_answers = []
        self.current_index = 0
        self.score = 0
        self.is_finished = False
        
        # Deshabilitar botó start
        self.start_btn.config(state='disabled')
        
        # Mostrar primera pregunta
        self.show_question()
        
        # Iniciar temporitzador
        self.time_left = minutes * 60
        self.timer_running = True
        self.update_timer()
    
    def show_question(self):
        """Mostra la pregunta actual"""
        if self.current_index >= len(self.questions):
            self.show_results()
            return
        
        q = self.questions[self.current_index]
        
        # Netejar opcions
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Mostrar pregunta
        level_labels = {'easy': 'Fàcil', 'medium': 'Mitjà', 'hard': 'Difícil'}
        level = self.level_var.get() if hasattr(self, 'level_var') else 'easy'
        
        self.question_label.config(
            text=f'Pregunta {self.current_index + 1}: {q["q"]}',
            font=('Inter', 14, 'bold'),
            fg=self.colors['text']
        )
        
        # Opcions
        self.option_buttons = []
        for i, opt in enumerate(q['options']):
            btn = tk.Button(self.options_frame,
                           text=f'{chr(65+i)}. {opt}',
                           font=('Inter', 11), bg='white',
                           relief='ridge', bd=2, pady=8,
                           anchor='w', padx=15,
                           command=lambda idx=i: self.select_option(idx))
            btn.pack(fill='x', pady=4, padx=20)
            self.option_buttons.append(btn)
        
        self.progress_label.config(text=f'{self.current_index + 1} / {self.total_questions}')
        self.is_answered = False
    
    def select_option(self, idx):
        """Selecciona una opció"""
        if self.is_answered or self.is_finished:
            return
        
        q = self.questions[self.current_index]
        is_correct = (idx == q['correct'])
        
        if is_correct:
            self.score += 1
            self.option_buttons[idx].config(bg=self.colors['success'], fg='white')
        else:
            self.option_buttons[idx].config(bg=self.colors['danger'], fg='white')
            self.option_buttons[q['correct']].config(bg=self.colors['success'], fg='white')
        
        self.user_answers.append(idx)
        self.is_answered = True
        
        # Deshabilitar botons
        for btn in self.option_buttons:
            btn.config(state='disabled')
        
        # Següent pregunta després d'un moment
        self.root.after(1500, self.next_question)
    
    def next_question(self):
        """Passa a la següent pregunta"""
        if self.is_finished:
            return
        
        self.current_index += 1
        if self.current_index >= len(self.questions):
            self.show_results()
        else:
            self.show_question()
    
    def show_results(self):
        """Mostra els resultats finals"""
        self.is_finished = True
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        
        # Netejar opcions
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        total = self.total_questions
        percent = round((self.score / total) * 100) if total > 0 else 0
        
        emoji = '🌟' if percent >= 90 else '😊' if percent >= 70 else '🤔' if percent >= 50 else '📚' if percent >= 30 else '😢'
        
        self.question_label.config(text=f'{emoji} Resultats: {self.score}/{total} ({percent}%)',
                                   font=('Inter', 18, 'bold'),
                                   fg=self.colors['text'])
        
        # Mostrar detall
        detall_frame = tk.Frame(self.options_frame, bg='white')
        detall_frame.pack(fill='both', expand=True)
        
        # Scroll per al detall
        canvas = tk.Canvas(detall_frame, bg='white', highlightthickness=0)
        scrollbar = tk.Scrollbar(detall_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for i, q in enumerate(self.questions):
            user_ans = self.user_answers[i] if i < len(self.user_answers) else -1
            is_correct = (user_ans == q['correct'])
            
            frame = tk.Frame(scrollable_frame, bg='white', pady=3)
            frame.pack(fill='x')
            
            icon = '✅' if is_correct else '❌' if user_ans >= 0 else '⏭️'
            color = self.colors['success'] if is_correct else self.colors['danger'] if user_ans >= 0 else self.colors['warning']
            
            tk.Label(frame, text=f'{icon} {q["q"]}', font=('Inter', 10),
                     bg='white', fg=color).pack(side='left')
            
            if user_ans == -1:
                tk.Label(frame, text='(No contestada)', font=('Inter', 9),
                         bg='white', fg=self.colors['text_light']).pack(side='left', padx=10)
            elif is_correct:
                tk.Label(frame, text=f'→ {q["options"][user_ans]}', font=('Inter', 9),
                         bg='white', fg=self.colors['success']).pack(side='left', padx=10)
            else:
                tk.Label(frame, text=f'→ Tu: {q["options"][user_ans]}', font=('Inter', 9),
                         bg='white', fg=self.colors['danger']).pack(side='left', padx=10)
                tk.Label(frame, text=f'✅ {q["options"][q["correct"]]}', font=('Inter', 9),
                         bg='white', fg=self.colors['success']).pack(side='left', padx=5)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Botons
        btn_frame = tk.Frame(self.options_frame, bg='white')
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text='🔄 Repetir', command=self.start_quiz,
                  bg=self.colors['primary'], fg='white',
                  font=('Inter', 11), relief='flat',
                  padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)
        
        tk.Button(btn_frame, text='🏠 Inici', command=lambda: self.go_to_page('home'),
                  bg=self.colors['text_light'], fg='white',
                  font=('Inter', 11), relief='flat',
                  padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)
        
        self.start_btn.config(state='normal')
    
    def update_timer(self):
        """Actualitza el temporitzador"""
        if not self.timer_running or self.is_finished:
            return
        
        if self.time_left <= 0:
            self.timer_running = False
            self.show_results()
            return
        
        mins = self.time_left // 60
        secs = self.time_left % 60
        self.timer_label.config(text=f'⏱ {mins:02d}:{secs:02d}')
        self.time_left -= 1
        
        self.timer_id = self.root.after(1000, self.update_timer)
    
    # ==============================================================
    # MEMORITZACIÓ
    # ==============================================================
    
    def start_memorization(self):
        """Inicia el mòdul de memorització"""
        if not self.image_path:
            messagebox.showerror('Error', 'Si us plau, selecciona una imatge primer')
            return
        
        try:
            view_time = int(self.view_entry.get())
        except:
            messagebox.showerror('Error', 'Introdueix un temps vàlid')
            return
        
        # Netejar zona de preguntes
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        self.memorization_phase = 'memorization'
        self.notes = ''
        self.start_btn.config(state='disabled')
        
        # Timer
        self.timer_label.config(text=f'⏱ {view_time}')
        
        # Mostrar imatge
        try:
            img = Image.open(self.image_path)
            max_size = (500, 400)
            img.thumbnail(max_size, Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(self.options_frame, image=photo, bg='white')
            img_label.image = photo
            img_label.pack(pady=10)
        except:
            messagebox.showerror('Error', 'No s\'ha pogut carregar la imatge')
            return
        
        # Quadre de notes
        notes_frame = tk.Frame(self.options_frame, bg='white')
        notes_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(notes_frame, text='📝 Prendre notes:', font=('Inter', 11, 'bold'),
                 bg='white').pack(anchor='w')
        
        self.notes_text = tk.Text(notes_frame, height=5, width=60,
                                  font=('Inter', 11), wrap='word')
        self.notes_text.pack(fill='x', pady=5)
        
        # Iniciar compte enrere
        self.time_left = view_time
        self.timer_running = True
        self.update_memorization_timer(view_time, img_label)
    
    def update_memorization_timer(self, remaining, img_label):
        """Actualitza el temporitzador de memorització"""
        if remaining <= 0:
            self.timer_running = False
            self.notes = self.notes_text.get('1.0', tk.END).strip()
            self.go_to_writing_phase()
            return
        
        self.timer_label.config(text=f'⏱ {remaining}')
        self.root.after(1000, lambda: self.update_memorization_timer(remaining - 1, img_label))
    
    def go_to_writing_phase(self):
        """Passa a la fase d'escriptura"""
        self.memorization_phase = 'writing'
        
        # Netejar
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        self.question_label.config(text='✍️ Escriu el que recordes',
                                   font=('Inter', 18, 'bold'),
                                   fg=self.colors['text'])
        
        tk.Label(self.options_frame, text='La imatge ja no es mostra. Escriu tot el que recordis.',
                 font=('Inter', 12), bg='white',
                 fg=self.colors['text_light']).pack(pady=5)
        
        self.write_text = tk.Text(self.options_frame, height=8, width=60,
                                  font=('Inter', 12), wrap='word')
        self.write_text.pack(padx=20, pady=10, fill='both', expand=True)
        
        btn_frame = tk.Frame(self.options_frame, bg='white')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text='🔍 Comparar', command=self.compare_memorization,
                  bg=self.colors['success'], fg='white',
                  font=('Inter', 12, 'bold'), relief='flat',
                  padx=30, pady=10, cursor='hand2').pack()
    
    def compare_memorization(self):
        """Compara el text escrit amb l'original"""
        user_text = self.write_text.get('1.0', tk.END).strip()
        
        if not user_text:
            messagebox.showwarning('Atenció', 'Si us plau, escriu alguna cosa')
            return
        
        self.memorization_phase = 'results'
        
        # Netejar
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        self.question_label.config(text='📊 Resultats de la memorització',
                                   font=('Inter', 18, 'bold'),
                                   fg=self.colors['text'])
        
        # Grid per resultats
        grid_frame = tk.Frame(self.options_frame, bg='white')
        grid_frame.pack(fill='both', expand=True, padx=10)
        
        # Imatge original
        left_frame = tk.Frame(grid_frame, bg='white', relief='ridge', bd=1)
        left_frame.pack(side='left', fill='both', expand=True, padx=5)
        
        tk.Label(left_frame, text='🖼️ Imatge original', font=('Inter', 12, 'bold'),
                 bg='white').pack(pady=5)
        
        try:
            img = Image.open(self.image_path)
            max_size = (300, 250)
            img.thumbnail(max_size, Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(left_frame, image=photo, bg='white')
            img_label.image = photo
            img_label.pack(pady=5, expand=True)
        except:
            tk.Label(left_frame, text='(No s\'ha pogut carregar la imatge)',
                     bg='white').pack(pady=20)
        
        # Text escrit
        right_frame = tk.Frame(grid_frame, bg='white', relief='ridge', bd=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=5)
        
        tk.Label(right_frame, text='✍️ El que has escrit', font=('Inter', 12, 'bold'),
                 bg='white').pack(pady=5)
        
        text_display = tk.Text(right_frame, height=10, width=30,
                               font=('Inter', 11), wrap='word')
        text_display.insert('1.0', user_text if user_text else '(No has escrit res)')
        text_display.config(state='disabled')
        text_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Notes
        notes_frame = tk.Frame(self.options_frame, bg='white', relief='ridge', bd=1)
        notes_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(notes_frame, text='📝 Notes preses durant la memorització',
                 font=('Inter', 12, 'bold'), bg='white').pack(anchor='w', padx=10, pady=5)
        
        notes_display = tk.Text(notes_frame, height=4, width=60,
                                font=('Inter', 11), wrap='word')
        notes_display.insert('1.0', self.notes if self.notes else '(No has pres notes)')
        notes_display.config(state='disabled')
        notes_display.pack(fill='x', padx=10, pady=5)
        
        # Botons
        btn_frame = tk.Frame(self.options_frame, bg='white')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text='🔄 Tornar a començar',
                  command=self.reset_memorization,
                  bg=self.colors['primary'], fg='white',
                  font=('Inter', 11), relief='flat',
                  padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)
        
        tk.Button(btn_frame, text='🏠 Inici', command=lambda: self.go_to_page('home'),
                  bg=self.colors['text_light'], fg='white',
                  font=('Inter', 11), relief='flat',
                  padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)
        
        self.start_btn.config(state='normal')
    
    def reset_memorization(self):
        """Reinicia el mòdul de memorització"""
        self.memorization_phase = 'idle'
        self.start_btn.config(state='normal')
        self.show_practica()
    
    # ==============================================================
    # PÀGINA: TEORIA
    # ==============================================================
    
    def show_teoria(self):
        """Mostra la pàgina de teoria de matemàtiques"""
        self.clear_content()
        self.current_page = 'teoria'
        
        # Botó tornar
        self.create_back_button()
        
        # Contingut de teoria
        teoria_frame = tk.Frame(self.dynamic_frame, bg='white')
        teoria_frame.pack(fill='both', expand=True)
        
        # Títol
        tk.Label(teoria_frame, text='📐 Conceptes matemàtics',
                 font=('Inter', 18, 'bold'), bg='white',
                 fg=self.colors['text']).pack(pady=10)
        
        tk.Label(teoria_frame, text='Principals conceptes per resoldre els exercicis de càlcul.',
                 font=('Inter', 12), bg='white',
                 fg=self.colors['text_light']).pack(pady=(0, 15))
        
        # Contingut amb scroll
        canvas = tk.Canvas(teoria_frame, bg='white', highlightthickness=0)
        scrollbar = tk.Scrollbar(teoria_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Continguts
        sections = [
            ('1. Prioritat d\'operacions', [
                'L\'ordre de les operacions és fonamental per resoldre expressions matemàtiques.',
                '📋 Ordre de prioritat:',
                '  1. Parèntesis ( ) — Primer de tot',
                '  2. Potències i arrels x², √x',
                '  3. Multiplicació i divisió ×, ÷ — D\'esquerra a dreta',
                '  4. Suma i resta +, − — D\'esquerra a dreta',
                '💡 Exemple: 8 + 3 × 2 = 8 + 6 = 14',
                '💡 Exemple: (6 + 4) × 3 = 10 × 3 = 30'
            ]),
            ('2. Percentatges', [
                'Un percentatge és una fracció amb denominador 100.',
                '📋 Fórmula: Percentatge = (Part / Total) × 100',
                '📋 Calcular: Quantitat × (Percentatge / 100)',
                '💡 Exemple: 20% de 80 = 80 × 0.20 = 16',
                '💡 Exemple: 25% de 40 = 40 × 0.25 = 10 € de descompte'
            ]),
            ('3. Regla de 3', [
                '📋 Regla de 3 directa: a/b = c/x → x = (b × c) / a',
                '💡 Exemple: 3 kg → 6 €, 5 kg → x = (6 × 5) / 3 = 10 €',
                '📋 Regla de 3 inversa: a × b = c × x → x = (a × b) / c',
                '💡 Exemple: 2 persones → 12 h, 4 persones → x = (2 × 12) / 4 = 6 h'
            ]),
            ('4. Geometria bàsica', [
                '📋 Perímetre rectangle: P = 2 × (ample + llarg)',
                '💡 6 cm × 8 cm → P = 2 × (6 + 8) = 28 cm',
                '📋 Àrea quadrat: A = costat²',
                '💡 5 cm → A = 5² = 25 cm²',
                '📋 Àrea triangle: A = (base × altura) / 2',
                '💡 6 cm × 4 cm → A = (6 × 4) / 2 = 12 cm²'
            ]),
            ('5. Mitjana aritmètica', [
                '📋 Mitjana = Suma de tots els valors / Nombre de valors',
                '💡 Mitjana de 4, 8, 6: (4 + 8 + 6) / 3 = 18 / 3 = 6'
            ]),
            ('6. Fraccions', [
                '📋 Suma: a/b + c/d = (a×d + c×b) / (b×d)',
                '💡 3/4 + 1/2 = (3×2 + 1×4) / (4×2) = 10/8 = 5/4',
                '📋 Producte: a/b × c/d = (a×c) / (b×d)',
                '💡 2/3 × 3/4 = 6/12 = 1/2',
                '📋 Divisió: a/b ÷ c/d = a/b × d/c = (a×d) / (b×c)',
                '💡 5/8 ÷ 3/4 = 5/8 × 4/3 = 20/24 = 5/6'
            ]),
            ('7. Potències', [
                '📋 a^n = a × a × ... × a (n vegades)',
                '💡 2³ = 2 × 2 × 2 = 8',
                '💡 3² × 2³ = 9 × 8 = 72',
                '📋 Arrel quadrada: √x = y si y² = x',
                '💡 √49 + √16 = 7 + 4 = 11'
            ])
        ]
        
        for title, items in sections:
            # Títol de secció
            tk.Label(scrollable_frame, text=title,
                     font=('Inter', 14, 'bold'), bg='white',
                     fg=self.colors['primary_dark']).pack(anchor='w', pady=(10, 5))
            
            for item in items:
                if item.startswith('📋') or item.startswith('💡'):
                    tk.Label(scrollable_frame, text=item,
                             font=('Inter', 11), bg='white',
                             fg=self.colors['text']).pack(anchor='w', padx=15, pady=2)
                else:
                    tk.Label(scrollable_frame, text=item,
                             font=('Inter', 11), bg='white',
                             fg=self.colors['text']).pack(anchor='w', padx=5, pady=2)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    # ==============================================================
    # PÀGINA: ORTOGRAFIA
    # ==============================================================
    
    def show_ortografia(self):
        """Mostra la pàgina de regles ortogràfiques"""
        self.clear_content()
        self.current_page = 'ortografia'
        
        # Botó tornar
        self.create_back_button()
        
        # Contingut d'ortografia
        orto_frame = tk.Frame(self.dynamic_frame, bg='white')
        orto_frame.pack(fill='both', expand=True)
        
        # Títol
        tk.Label(orto_frame, text='📝 Regles ortogràfiques',
                 font=('Inter', 18, 'bold'), bg='white',
                 fg=self.colors['text']).pack(pady=10)
        
        tk.Label(orto_frame, text='Normes bàsiques per escriure correctament en català.',
                 font=('Inter', 12), bg='white',
                 fg=self.colors['text_light']).pack(pady=(0, 15))
        
        # Contingut amb scroll
        canvas = tk.Canvas(orto_frame, bg='white', highlightthickness=0)
        scrollbar = tk.Scrollbar(orto_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Continguts
        sections = [
            ('1. L\'alfabet català', [
                'L\'alfabet català té 27 lletres:',
                'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z',
                'Les lletres K, W i Y només s\'usen en paraules d\'origen estranger.'
            ]),
            ('2. Les vocals', [
                'El català té 7 vocals: a, e, i, o, u, è (oberta) i é (tancada)',
                '🔊 Vocals obertes: à, è, ò',
                '🔊 Vocals tancades: é, í, ó, ú',
                '💡 Exemples:',
                '  • è oberta: cafè, pedra',
                '  • é tancada: café, té',
                '  • ò oberta: cançó, colònia',
                '  • ó tancada: camió, arròs'
            ]),
            ('3. Apostrofació i contraccions', [
                '📋 Apostrofació:',
                'S\'apostrofen els articles el, la, en i les preposicions de, per',
                'davant de paraula que comença per vocal o h.',
                '💡 Exemples: l\'home, l\'escola, d\'ahir',
                '⚠️ Excepcions: No s\'apostrofa davant de la, una, o davant de i/u àtones.',
                '📋 Contraccions:',
                'de + el = del → el llibre del noi',
                'per + el = pel → pel camí'
            ]),
            ('4. Les esses: s, ss, c, ç, z', [
                '🔤 S — A començament de paraula, entre vocals (sonora), davant de consonant',
                '💡 Exemples: sopa, casa, escola',
                '🔤 SS — Entre vocals (sorda)',
                '💡 Exemples: passar, cassola',
                '🔤 C/Ç — Ç davant de a, o, u; C davant de e, i',
                '💡 Exemples: braç, plaça, cervesa, ciència'
            ]),
            ('5. La b i la v', [
                '🔤 B — Davant de l o r, en paraules que comencen per ab-, ob-, sub-',
                '💡 Exemples: bla, bra, abans, obtenir',
                '🔤 V — En paraules que comencen per ev-, ov-',
                '💡 Exemples: evitar, ovella',
                '⚠️ Atenció! Aquesta és una de les regles que més dubtes genera.'
            ]),
            ('6. La ela geminada: l·l', [
                'La ela geminada l·l és un so característic del català.',
                '🔤 S\'escriu l·l en paraules on hi ha dos sons l separats',
                '💡 Exemples: col·legi, il·lusió, intel·ligent, novel·la',
                '⚠️ Important! La ela geminada no és una l doble normal (ll).'
            ]),
            ('7. La erra: r i rr', [
                '🔤 R — A començament de paraula, entre vocals (vibrant simple)',
                '💡 Exemples: ram, rosa, cara, hora',
                '🔤 RR — Entre vocals (vibrant múltiple)',
                '💡 Exemples: carro, terra, arrencar'
            ]),
            ('8. La g i la j', [
                '🔤 G — Davant de e, i (so suau) o davant de a, o, u (so dur)',
                '💡 Exemples: gent, girar, gat, gota, gust',
                '🔤 J — Davant de a, o, u',
                '💡 Exemples: ja, jo, jove, ajuda'
            ]),
            ('9. La ix i la x', [
                '🔤 IX — Entre vocals',
                '💡 Exemples: caixa, aixeta, exemple',
                '🔤 X — A començament de paraula o al final',
                '💡 Exemples: xarxa, xocolata, peix, reflex'
            ]),
            ('10. L\'accentuació gràfica', [
                '🔤 Paraules agudes (última síl·laba): s\'accentuen si acaben en vocal, -s, -en, -in',
                '💡 Exemples: cafè, cançó, camí',
                '🔤 Paraules planes (penúltima): s\'accentuen si NO acaben en vocal, -s, -en, -in',
                '💡 Exemples: llàgrima, difícil, cànon',
                '🔤 Paraules esdrúixoles (antepenúltima): sempre s\'accentuen',
                '💡 Exemples: pàgina, lògica, càntic'
            ]),
            ('11. Els accents diacrítics', [
                'L\'accent diacrític diferencia paraules que s\'escriuen igual.',
                '💡 Exemples:',
                '  • sé (saber) vs se (pronom)',
                '  • és (verb ser) vs es (pronom)',
                '  • més (quantitat) vs mes (mes)',
                '  • dóna (verb donar) vs dona (femella)'
            ]),
            ('12. La dièresi', [
                'La dièresi (¨) marca que una u es pronuncia en els grups gue, gui, que, qui.',
                '🔤 S\'usa en güe, güi, qüe, qüi',
                '💡 Exemples: aigües, qüestió, pingüí, argüir, ambigüitat'
            ])
        ]
        
        for title, items in sections:
            # Títol de secció
            tk.Label(scrollable_frame, text=title,
                     font=('Inter', 14, 'bold'), bg='white',
                     fg=self.colors['primary_dark']).pack(anchor='w', pady=(10, 5))
            
            for item in items:
                if item.startswith('💡') or item.startswith('⚠️'):
                    tk.Label(scrollable_frame, text=item,
                             font=('Inter', 11), bg='white',
                             fg=self.colors['text']).pack(anchor='w', padx=15, pady=2)
                elif item.startswith('  •'):
                    tk.Label(scrollable_frame, text=item,
                             font=('Inter', 10), bg='white',
                             fg=self.colors['text_light']).pack(anchor='w', padx=30, pady=1)
                else:
                    tk.Label(scrollable_frame, text=item,
                             font=('Inter', 11), bg='white',
                             fg=self.colors['text']).pack(anchor='w', padx=5, pady=2)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')


# ==============================================================
# PUNT D'ENTRADA
# ==============================================================

def main():
    root = tk.Tk()
    app = PsicotecnicApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()