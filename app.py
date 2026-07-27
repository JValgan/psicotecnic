"""
PSICOTÈCNIC 3 EN 1 - App per a Streamlit
Versió amb navegació corregida
"""

import streamlit as st
import random
import time
from PIL import Image
import io

# ==============================================================
# CONFIGURACIÓ DE LA PÀGINA
# ==============================================================
st.set_page_config(
    page_title="🧠 Psicotècnic 3 en 1",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================
# CSS PERSONALITZAT
# ==============================================================

st.markdown("""
<style>
    /* ===== ESTILS GENERALS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #F0F4F8 0%, #E8EEF5 100%);
    }
    
    /* ===== HEADER ===== */
    .app-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.5rem;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(74,144,217,0.08);
        margin-bottom: 2rem;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .app-header-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .app-header-icon {
        font-size: 2rem;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        width: 50px;
        height: 50px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        box-shadow: 0 4px 15px rgba(74,144,217,0.25);
    }
    
    .app-header-title {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    
    .app-header-title span {
        color: #2D3436;
        -webkit-text-fill-color: #2D3436;
    }
    
    .app-header-badge {
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        padding: 0.25rem 1rem;
        border-radius: 100px;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        box-shadow: 0 2px 10px rgba(74,144,217,0.2);
    }
    
    /* ===== PÀGINA D'INICI ===== */
    .home-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        color: #2D3436;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .home-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #636E72;
        margin-bottom: 2rem;
    }
    
    .home-card {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        padding: 2rem 1.5rem;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.3);
        text-align: center;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        position: relative;
        overflow: hidden;
    }
    
    .home-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #4A90D9, #6A5ACD, #00B894);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .home-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 60px rgba(74,144,217,0.12);
        border-color: rgba(74,144,217,0.2);
    }
    
    .home-card:hover::before {
        transform: scaleX(1);
    }
    
    .home-card .icon {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        transition: transform 0.4s ease;
    }
    
    .home-card:hover .icon {
        transform: scale(1.1) rotate(-5deg);
    }
    
    .home-card .title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #2D3436;
        margin-bottom: 0.2rem;
    }
    
    .home-card .desc {
        font-size: 0.85rem;
        color: #636E72;
        line-height: 1.4;
        max-width: 200px;
    }
    
    .home-card .tag {
        margin-top: 0.6rem;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 0.25rem 1rem;
        border-radius: 100px;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        box-shadow: 0 2px 10px rgba(74,144,217,0.2);
        transition: all 0.3s ease;
    }
    
    .home-card:hover .tag {
        box-shadow: 0 4px 20px rgba(74,144,217,0.3);
        transform: scale(1.05);
    }
    
    /* ===== BOTÓ TORNAR ===== */
    .btn-back {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1.5rem;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 100px;
        font-size: 0.9rem;
        font-weight: 600;
        color: #4A90D9;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
        margin-bottom: 1.2rem;
        text-decoration: none;
    }
    
    .btn-back:hover {
        transform: translateX(-4px);
        box-shadow: 0 4px 20px rgba(74,144,217,0.12);
        border-color: rgba(74,144,217,0.2);
    }
    
    /* ===== INSTRUCCIONS ===== */
    .instructions {
        background: linear-gradient(135deg, rgba(240,246,254,0.9), rgba(232,240,250,0.9));
        backdrop-filter: blur(10px);
        padding: 1.2rem 1.8rem;
        border-radius: 16px;
        border: 1px solid rgba(74,144,217,0.12);
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(74,144,217,0.04);
    }
    
    .instructions::before {
        content: '💡';
        position: absolute;
        right: 1.5rem;
        top: 50%;
        transform: translateY(-50%);
        font-size: 3.5rem;
        opacity: 0.06;
    }
    
    .instructions-title {
        font-size: 0.8rem;
        font-weight: 700;
        color: #3A7BC8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .instructions-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.4rem 1.5rem;
    }
    
    .instructions-item {
        display: flex;
        align-items: flex-start;
        gap: 0.5rem;
        font-size: 0.85rem;
        color: #2D3436;
        line-height: 1.4;
        padding: 0.1rem 0;
    }
    
    .instructions-item .emoji {
        font-size: 1rem;
        min-width: 22px;
        text-align: center;
        margin-top: 1px;
    }
    
    .instructions-item strong {
        color: #3A7BC8;
        font-weight: 600;
    }
    
    .instructions-footer {
        margin-top: 0.6rem;
        padding-top: 0.6rem;
        border-top: 1px solid rgba(74,144,217,0.1);
        font-size: 0.75rem;
        color: #636E72;
        text-align: center;
        font-style: italic;
    }
    
    .instructions-footer span {
        display: inline-block;
        background: rgba(255,255,255,0.8);
        padding: 0.05rem 0.6rem;
        border-radius: 100px;
        font-weight: 500;
        color: #4A90D9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    
    /* ===== CONFIGURACIÓ ===== */
    .config-container {
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        margin-bottom: 1.5rem;
    }
    
    .config-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #636E72;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.4rem;
        display: block;
    }
    
    /* ===== BOTONS DE MÒDUL ===== */
    .mod-btn-group {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    
    .mod-btn {
        padding: 0.5rem 1.2rem;
        border: 2px solid #DFE6E9;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        background: white;
        color: #636E72;
        flex: 1;
        min-width: 80px;
        text-align: center;
    }
    
    .mod-btn:hover {
        border-color: #4A90D9;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(74,144,217,0.1);
    }
    
    .mod-btn.active {
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        border-color: transparent;
        box-shadow: 0 4px 20px rgba(74,144,217,0.3);
    }
    
    /* ===== NIVELLS ===== */
    .level-group {
        display: flex;
        gap: 0.4rem;
        flex-wrap: wrap;
    }
    
    .level-btn {
        padding: 0.35rem 1rem;
        border: 2px solid #DFE6E9;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        background: white;
        color: #636E72;
    }
    
    .level-btn:hover {
        border-color: #4A90D9;
        transform: translateY(-2px);
    }
    
    .level-btn.active {
        border-color: #4A90D9;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        box-shadow: 0 4px 15px rgba(74,144,217,0.2);
    }
    
    .level-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 4px;
    }
    
    .level-dot.easy { background: #00B894; }
    .level-dot.medium { background: #FDCB6E; }
    .level-dot.hard { background: #FF6B6B; }
    
    /* ===== BOTÓ COMENÇAR ===== */
    .btn-start {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        padding: 0.7rem 2rem;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        border: none;
        border-radius: 100px;
        font-size: 1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(74,144,217,0.3);
        width: 100%;
        text-align: center;
    }
    
    .btn-start:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 35px rgba(74,144,217,0.4);
    }
    
    .btn-start:active {
        transform: scale(0.97);
    }
    
    .btn-start:disabled {
        opacity: 0.5;
        cursor: not-allowed;
        transform: none;
    }
    
    /* ===== PREGUNTA ===== */
    .question-box {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        padding: 1.8rem;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .question-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #4A90D9, #6A5ACD, #00B894);
    }
    
    .question-box h3 {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2D3436;
        line-height: 1.5;
    }
    
    .question-number {
        display: inline-block;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        font-size: 0.65rem;
        font-weight: 700;
        padding: 0.15rem 0.8rem;
        border-radius: 100px;
        margin-bottom: 0.6rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        box-shadow: 0 2px 10px rgba(74,144,217,0.15);
    }
    
    /* ===== OPCIONS ===== */
    .option-btn {
        width: 100%;
        padding: 0.8rem 1rem;
        margin: 0.3rem 0;
        border: 2px solid #DFE6E9;
        border-radius: 12px;
        background: white;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: left;
        font-size: 0.95rem;
        font-weight: 500;
        color: #2D3436;
        position: relative;
        overflow: hidden;
    }
    
    .option-btn::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #4A90D9, #6A5ACD);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .option-btn:hover:not(.disabled) {
        border-color: #4A90D9;
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(74,144,217,0.08);
    }
    
    .option-btn:hover:not(.disabled)::after {
        transform: scaleX(0.3);
    }
    
    .option-btn .letter {
        display: inline-block;
        background: #F5F8FC;
        color: #636E72;
        font-size: 0.65rem;
        font-weight: 700;
        width: 24px;
        height: 24px;
        line-height: 24px;
        border-radius: 50%;
        margin-right: 0.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .option-btn.selected {
        border-color: #4A90D9;
        background: rgba(74,144,217,0.06);
        box-shadow: 0 0 0 4px rgba(74,144,217,0.08);
    }
    
    .option-btn.selected .letter {
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        box-shadow: 0 2px 10px rgba(74,144,217,0.2);
    }
    
    .option-btn.correct {
        border-color: #00B894;
        background: rgba(0,184,148,0.08);
    }
    
    .option-btn.correct .letter {
        background: #00B894;
        color: white;
    }
    
    .option-btn.wrong {
        border-color: #FF6B6B;
        background: rgba(255,107,107,0.08);
    }
    
    .option-btn.wrong .letter {
        background: #FF6B6B;
        color: white;
    }
    
    .option-btn.disabled {
        opacity: 0.85;
        cursor: default;
        transform: none !important;
    }
    
    /* ===== TIMER I PROGRÉS ===== */
    .timer-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        padding: 0.5rem 1rem;
        border-radius: 100px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
        margin-bottom: 0.8rem;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .timer-text {
        font-size: 0.95rem;
        font-weight: 600;
        color: #4A90D9;
    }
    
    .timer-text.warning {
        color: #FF6B6B;
        animation: pulse 1s ease infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .progress-container {
        flex: 1;
        margin: 0 0.5rem;
        height: 5px;
        background: #DFE6E9;
        border-radius: 4px;
        overflow: hidden;
        min-width: 60px;
    }
    
    .progress-fill {
        height: 5px;
        background: linear-gradient(90deg, #4A90D9, #6A5ACD, #00B894);
        border-radius: 4px;
        transition: width 0.5s ease;
    }
    
    /* ===== RESULTATS ===== */
    .results-container {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        text-align: center;
    }
    
    .results-emoji {
        font-size: 3.5rem;
        display: block;
        margin-bottom: 0.3rem;
    }
    
    .results-score {
        font-size: 3rem;
        font-weight: 700;
        color: #2D3436;
    }
    
    .results-score .total {
        font-size: 1.5rem;
        color: #636E72;
        font-weight: 500;
    }
    
    .results-percent {
        font-size: 1.3rem;
        font-weight: 600;
        color: #4A90D9;
        margin-top: 0.2rem;
    }
    
    .results-detail {
        margin-top: 1.2rem;
        text-align: left;
        max-height: 350px;
        overflow-y: auto;
    }
    
    .results-detail::-webkit-scrollbar {
        width: 5px;
    }
    
    .results-detail::-webkit-scrollbar-track {
        background: #F5F8FC;
        border-radius: 8px;
    }
    
    .results-detail::-webkit-scrollbar-thumb {
        background: #4A90D9;
        border-radius: 8px;
    }
    
    .result-item {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.5rem 0.8rem;
        border-radius: 10px;
        background: white;
        border: 1px solid #DFE6E9;
        margin-bottom: 0.3rem;
        transition: all 0.3s ease;
    }
    
    .result-item:hover {
        border-color: #4A90D9;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    
    .result-item .icon {
        font-size: 1.1rem;
        min-width: 26px;
        text-align: center;
    }
    
    .result-item .question-text {
        flex: 1;
        font-size: 0.85rem;
        font-weight: 500;
        color: #2D3436;
    }
    
    .result-item .answer-text {
        font-size: 0.8rem;
        color: #636E72;
        text-align: right;
    }
    
    .result-item .answer-text .correct {
        color: #00B894;
        font-weight: 600;
    }
    
    .result-item .answer-text .wrong {
        color: #FF6B6B;
        font-weight: 600;
    }
    
    /* ===== BOTONS DE RESULTATS ===== */
    .results-actions {
        display: flex;
        gap: 0.8rem;
        margin-top: 1.2rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .results-actions .btn {
        padding: 0.6rem 2rem;
        border-radius: 100px;
        font-size: 0.9rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        flex: 1;
        min-width: 120px;
        text-align: center;
    }
    
    .results-actions .btn-primary {
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        color: white;
        box-shadow: 0 4px 20px rgba(74,144,217,0.3);
    }
    
    .results-actions .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 35px rgba(74,144,217,0.4);
    }
    
    .results-actions .btn-secondary {
        background: rgba(99,110,114,0.1);
        color: #636E72;
        border: 2px solid #DFE6E9;
    }
    
    .results-actions .btn-secondary:hover {
        transform: translateY(-3px);
        border-color: #4A90D9;
        color: #4A90D9;
    }
    
    /* ===== MEMORITZACIÓ ===== */
    .memorization-container {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        margin-top: 1rem;
    }
    
    .memorization-timer {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #4A90D9, #6A5ACD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.8rem;
    }
    
    .memorization-image {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    /* ===== TEORIA I ORTOGRAFIA ===== */
    .theory-container {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.8rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        margin-top: 1rem;
    }
    
    .theory-container h2 {
        font-size: 1.3rem;
        font-weight: 700;
        color: #2D3436;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    
    .theory-container h3 {
        font-size: 1rem;
        font-weight: 600;
        color: #3A7BC8;
        margin: 1rem 0 0.4rem 0;
    }
    
    .theory-container .formula {
        background: white;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        border: 1px solid #DFE6E9;
        margin: 0.4rem 0;
        text-align: center;
        font-size: 1rem;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    .theory-container .example {
        background: white;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        border-left: 4px solid #4A90D9;
        margin: 0.4rem 0;
        font-size: 0.9rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    .theory-container .rule-box {
        background: white;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        border-left: 4px solid #00B894;
        margin: 0.4rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    .theory-container .rule-box.warning {
        border-left-color: #FDCB6E;
    }
    
    .theory-container .rule-box.danger {
        border-left-color: #FF6B6B;
    }
    
    .theory-toc {
        background: white;
        padding: 0.8rem 1.2rem;
        border-radius: 12px;
        border: 1px solid #DFE6E9;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    .theory-toc ul {
        columns: 2;
        column-gap: 1.5rem;
        padding-left: 1.2rem;
        margin: 0;
    }
    
    .theory-toc li {
        font-size: 0.85rem;
        break-inside: avoid;
        padding: 0.15rem 0;
    }
    
    .theory-toc a {
        color: #4A90D9;
        text-decoration: none;
        font-weight: 500;
        cursor: pointer;
        transition: color 0.3s ease;
    }
    
    .theory-toc a:hover {
        color: #3A7BC8;
        text-decoration: underline;
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .app-header {
            padding: 0.8rem 1rem;
            justify-content: center;
            gap: 0.3rem;
        }
        
        .app-header-title {
            font-size: 1.1rem;
        }
        
        .app-header-badge {
            font-size: 0.55rem;
            padding: 0.15rem 0.6rem;
        }
        
        .app-header-icon {
            width: 36px;
            height: 36px;
            font-size: 1.4rem;
        }
        
        .home-title {
            font-size: 1.5rem;
        }
        
        .home-card {
            min-height: 160px;
            padding: 1.2rem 1rem;
        }
        
        .home-card .icon {
            font-size: 2.5rem;
        }
        
        .home-card .title {
            font-size: 1rem;
        }
        
        .home-card .desc {
            font-size: 0.75rem;
        }
        
        .instructions-grid {
            grid-template-columns: 1fr;
            gap: 0.2rem;
        }
        
        .instructions::before {
            display: none;
        }
        
        .config-container {
            padding: 0.8rem 1rem;
        }
        
        .mod-btn {
            font-size: 0.75rem;
            padding: 0.35rem 0.8rem;
            min-width: 60px;
        }
        
        .level-btn {
            font-size: 0.7rem;
            padding: 0.25rem 0.7rem;
        }
        
        .results-score {
            font-size: 2.2rem;
        }
        
        .results-actions {
            flex-direction: column;
        }
        
        .results-actions .btn {
            min-width: auto;
        }
        
        .theory-toc ul {
            columns: 1;
        }
        
        .timer-container {
            border-radius: 16px;
            padding: 0.5rem 0.8rem;
            justify-content: center;
        }
        
        .progress-container {
            width: 100%;
            margin: 0.2rem 0;
        }
        
        .question-box {
            padding: 1rem;
        }
        
        .question-box h3 {
            font-size: 1rem;
        }
        
        .option-btn {
            font-size: 0.85rem;
            padding: 0.6rem 0.8rem;
        }
        
        .memorization-timer {
            font-size: 2rem;
        }
        
        .results-container {
            padding: 1.2rem;
        }
        
        .level-group {
            justify-content: center;
        }
        
        .btn-start {
            font-size: 0.9rem;
            padding: 0.5rem 1.5rem;
        }
    }
    
    @media (max-width: 480px) {
        .home-card {
            min-height: 140px;
            padding: 0.8rem;
        }
        
        .home-card .icon {
            font-size: 2rem;
        }
        
        .home-card .title {
            font-size: 0.9rem;
        }
        
        .home-card .desc {
            font-size: 0.7rem;
        }
        
        .mod-btn {
            font-size: 0.65rem;
            padding: 0.25rem 0.5rem;
            min-width: 50px;
        }
        
        .results-score {
            font-size: 1.8rem;
        }
        
        .results-emoji {
            font-size: 2.5rem;
        }
        
        .question-box h3 {
            font-size: 0.9rem;
        }
        
        .option-btn {
            font-size: 0.8rem;
            padding: 0.5rem 0.6rem;
        }
        
        .option-btn .letter {
            width: 20px;
            height: 20px;
            line-height: 20px;
            font-size: 0.55rem;
        }
        
        .result-item .question-text {
            font-size: 0.75rem;
        }
        
        .result-item .answer-text {
            font-size: 0.7rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================
# BASE DE DADES DE PREGUNTES
# ==============================================================

QUESTIONS = {
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

def get_module_instructions(module):
    instructions = {
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
    return instructions.get(module, instructions['calcul'])

# ==============================================================
# FUNCIONS AUXILIARS
# ==============================================================

def shuffle_array(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def select_random_questions(n, bank):
    bank_copy = bank.copy()
    shuffle_array(bank_copy)
    if n <= len(bank_copy):
        return bank_copy[:n]
    selected = bank_copy.copy()
    while len(selected) < n:
        extra = bank_copy[random.randint(0, len(bank_copy) - 1)]
        selected.append(extra.copy())
    return selected

def get_level_label(level):
    labels = {'easy': 'Fàcil', 'medium': 'Mitjà', 'hard': 'Difícil'}
    return labels.get(level, 'Fàcil')

# ==============================================================
# INICIALITZACIÓ DE L'ESTAT
# ==============================================================

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'module' not in st.session_state:
    st.session_state.module = 'calcul'
if 'level' not in st.session_state:
    st.session_state.level = 'easy'
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'time_limit' not in st.session_state:
    st.session_state.time_limit = 120
if 'timer_start' not in st.session_state:
    st.session_state.timer_start = None
if 'image_file' not in st.session_state:
    st.session_state.image_file = None
if 'mem_phase' not in st.session_state:
    st.session_state.mem_phase = 'viewing'
if 'mem_notes' not in st.session_state:
    st.session_state.mem_notes = ''
if 'view_time' not in st.session_state:
    st.session_state.view_time = 30

# ==============================================================
# FUNCIONS DE NAVEGACIÓ
# ==============================================================

def go_to_page(page):
    st.session_state.page = page
    st.rerun()

def reset_quiz():
    st.session_state.questions = []
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.total = 0
    st.session_state.time_limit = 120
    st.session_state.timer_start = None

# ==============================================================
# PÀGINA D'INICI
# ==============================================================

def home_page():
    st.markdown('<div class="home-title">🎯 Què vols practicar?</div>', unsafe_allow_html=True)
    st.markdown('<div class="home-subtitle">Selecciona una opció per començar</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="home-card">
            <div class="icon">📝</div>
            <div class="title">Pràctica</div>
            <div class="desc">Exercicis interactius de Càlcul, Català i Memorització</div>
            <div class="tag">▶ Començar</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶ Anar a Pràctica", key="btn_practica", use_container_width=True, type="primary"):
            go_to_page('practica')
    
    with col2:
        st.markdown("""
        <div class="home-card">
            <div class="icon">📐</div>
            <div class="title">Matemàtiques</div>
            <div class="desc">Conceptes i fórmules per resoldre els exercicis</div>
            <div class="tag">📖 Consultar</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Anar a Matemàtiques", key="btn_teoria", use_container_width=True, type="secondary"):
            go_to_page('teoria')
    
    with col3:
        st.markdown("""
        <div class="home-card">
            <div class="icon">📝</div>
            <div class="title">Ortografia</div>
            <div class="desc">Regles i normes per escriure correctament en català</div>
            <div class="tag">📖 Consultar</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Anar a Ortografia", key="btn_ortografia", use_container_width=True, type="secondary"):
            go_to_page('ortografia')

# ==============================================================
# PÀGINA: PRÀCTICA
# ==============================================================

def practica_page():
    st.markdown("""
    <div class="app-header">
        <div class="app-header-left">
            <div class="app-header-icon">🎯</div>
            <div class="app-header-title">Pràctica</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Tornar al menú", key="back_from_practica"):
        go_to_page('home')
    
    # Instruccions
    instr = get_module_instructions(st.session_state.module)
    
    st.markdown(f"""
    <div class="instructions">
        <div class="instructions-title">💡 {instr['title']}</div>
        <div class="instructions-grid">
    """, unsafe_allow_html=True)
    
    for emoji, text in instr['items']:
        st.markdown(f"""
        <div class="instructions-item">
            <span class="emoji">{emoji}</span>
            <span>{text}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
        </div>
        <div class="instructions-footer">{instr['footer']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Configuració
    with st.container():
        st.markdown('<div class="config-container">', unsafe_allow_html=True)
        
        # Selector de mòdul
        st.markdown('<span class="config-label">📚 Mòdul</span>', unsafe_allow_html=True)
        mod_cols = st.columns(3)
        modules = ['calcul', 'catala', 'memoritzacio']
        module_labels = {'calcul': '📐 Càlcul', 'catala': '📚 Català', 'memoritzacio': '👁️ Memorització'}
        
        for i, mod in enumerate(modules):
            with mod_cols[i]:
                if st.button(
                    module_labels[mod],
                    use_container_width=True,
                    type="primary" if st.session_state.module == mod else "secondary",
                    key=f"mod_{mod}"
                ):
                    st.session_state.module = mod
                    st.rerun()
        
        if st.session_state.module != 'memoritzacio':
            # Preguntes i temps
            col_a, col_b = st.columns(2)
            with col_a:
                num_q = st.number_input('📝 Preguntes', min_value=1, max_value=30, value=10, key="num_questions")
            with col_b:
                minutes = st.number_input('⏱️ Temps (min)', min_value=1, max_value=30, value=2, key="time_minutes")
            
            # Nivell
            st.markdown('<span class="config-label">📊 Nivell</span>', unsafe_allow_html=True)
            level_cols = st.columns(3)
            levels = ['easy', 'medium', 'hard']
            level_labels = {'easy': '🟢 Fàcil', 'medium': '🟡 Mitjà', 'hard': '🔴 Difícil'}
            
            for i, level in enumerate(levels):
                with level_cols[i]:
                    if st.button(
                        level_labels[level],
                        use_container_width=True,
                        type="primary" if st.session_state.level == level else "secondary",
                        key=f"level_{level}"
                    ):
                        st.session_state.level = level
                        st.rerun()
            
            # Botó començar
            if st.button('▶ Començar', use_container_width=True, type="primary", key="btn_start_quiz"):
                bank = QUESTIONS.get(st.session_state.module, {}).get(st.session_state.level, [])
                if bank:
                    selected = select_random_questions(num_q, bank)
                    st.session_state.questions = selected
                    st.session_state.total = len(selected)
                    st.session_state.current_q = 0
                    st.session_state.score = 0
                    st.session_state.answers = []
                    st.session_state.time_limit = minutes * 60
                    st.session_state.timer_start = time.time()
                    go_to_page('quiz')
                else:
                    st.warning('No hi ha preguntes per a aquest mòdul i nivell.')
        
        else:
            # Memorització
            uploaded_file = st.file_uploader("🖼️ Selecciona una imatge", type=['png', 'jpg', 'jpeg', 'gif'], key="mem_upload")
            if uploaded_file:
                st.session_state.image_file = uploaded_file
                st.image(uploaded_file, caption='Imatge carregada', use_container_width=True)
            
            view_time = st.number_input('⏱️ Visualització (s)', min_value=5, max_value=300, value=30, key="view_time_input")
            st.session_state.view_time = view_time
            
            if st.button('▶ Començar memorització', use_container_width=True, type="primary", key="btn_start_mem"):
                if st.session_state.image_file:
                    st.session_state.mem_phase = 'viewing'
                    go_to_page('memorization')
                else:
                    st.warning('Si us plau, selecciona una imatge primer.')
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================
# PÀGINA: QUIZ
# ==============================================================

def quiz_page():
    questions = st.session_state.questions
    current = st.session_state.current_q
    
    # Timer
    timer_html = '<div class="timer-container">'
    if st.session_state.timer_start:
        elapsed = time.time() - st.session_state.timer_start
        remaining = max(0, st.session_state.time_limit - elapsed)
        mins = int(remaining // 60)
        secs = int(remaining % 60)
        warning_class = 'warning' if remaining < 10 else ''
        timer_html += f'<span class="timer-text {warning_class}">⏱ {mins:02d}:{secs:02d}</span>'
        
        if remaining <= 0:
            go_to_page('results')
            return
    timer_html += '<div class="progress-container"><div class="progress-fill" style="width:' + str((current / len(questions) * 100) if questions else 0) + '%;"></div></div>'
    timer_html += f'<span style="font-size:0.8rem;color:#636E72;font-weight:500;">{current}/{len(questions)}</span>'
    timer_html += '</div>'
    st.markdown(timer_html, unsafe_allow_html=True)
    
    if current >= len(questions):
        go_to_page('results')
        return
    
    q = questions[current]
    
    # Pregunta
    st.markdown(f"""
    <div class="question-box">
        <span class="question-number">Pregunta {current + 1}</span>
        <h3>{q['q']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Opcions
    cols = st.columns(2)
    
    # Determinar si ja s'ha respost
    is_answered = len(st.session_state.answers) > current
    
    for i, opt in enumerate(q['options']):
        col = cols[i % 2]
        with col:
            is_selected = is_answered and st.session_state.answers[current] == i
            is_correct = i == q['correct']
            
            if is_answered:
                if is_correct:
                    btn_type = "success"
                elif is_selected:
                    btn_type = "danger"
                else:
                    btn_type = "secondary"
                disabled = True
                extra_class = 'correct' if is_correct else ('wrong' if is_selected else '')
            else:
                btn_type = "secondary"
                disabled = False
                extra_class = ''
            
            # Botó
            if st.button(
                f"{chr(65+i)}. {opt}",
                key=f"opt_{current}_{i}",
                use_container_width=True,
                type=btn_type,
                disabled=disabled
            ):
                if not is_answered:
                    st.session_state.answers.append(i)
                    if is_correct:
                        st.session_state.score += 1
                    st.session_state.current_q += 1
                    st.rerun()

# ==============================================================
# PÀGINA: RESULTATS
# ==============================================================

def results_page():
    st.markdown("""
    <div class="app-header">
        <div class="app-header-left">
            <div class="app-header-icon">📊</div>
            <div class="app-header-title">Resultats</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    total = len(st.session_state.questions)
    score = st.session_state.score
    percent = round((score / total) * 100) if total > 0 else 0
    
    emoji = '🌟' if percent >= 90 else '😊' if percent >= 70 else '🤔' if percent >= 50 else '📚' if percent >= 30 else '😢'
    
    st.markdown(f"""
    <div class="results-container">
        <span class="results-emoji">{emoji}</span>
        <div class="results-score">{score} <span class="total">/ {total}</span></div>
        <div class="results-percent">{percent}%</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Detall
    with st.expander("📋 Veure detall de respostes", expanded=False):
        for i, q in enumerate(st.session_state.questions):
            user_ans = st.session_state.answers[i] if i < len(st.session_state.answers) else -1
            is_correct = (user_ans == q['correct'])
            
            icon = '✅' if is_correct else '❌' if user_ans >= 0 else '⏭️'
            
            cols = st.columns([1, 4, 3])
            with cols[0]:
                st.markdown(f'<span style="font-size:1.1rem;">{icon}</span>', unsafe_allow_html=True)
            with cols[1]:
                st.markdown(f'<span style="font-weight:500;">{q["q"]}</span>', unsafe_allow_html=True)
            with cols[2]:
                if is_correct:
                    st.markdown(f'<span style="color:#00B894;font-weight:600;">✅ {q["options"][user_ans]}</span>', unsafe_allow_html=True)
                elif user_ans >= 0:
                    st.markdown(f'<span style="color:#FF6B6B;font-weight:600;">❌ {q["options"][user_ans]}</span> → <span style="color:#00B894;font-weight:600;">✅ {q["options"][q["correct"]]}</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span style="color:#636E72;">⏭️ No contestada</span>', unsafe_allow_html=True)
    
    # Botons
    col1, col2 = st.columns(2)
    with col1:
        if st.button('🔄 Repetir', use_container_width=True, type="primary", key="btn_repeat"):
            reset_quiz()
            go_to_page('practica')
    with col2:
        if st.button('🏠 Inici', use_container_width=True, key="btn_home_from_results"):
            reset_quiz()
            go_to_page('home')

# ==============================================================
# PÀGINA: TEORIA
# ==============================================================

def teoria_page():
    st.markdown("""
    <div class="app-header">
        <div class="app-header-left">
            <div class="app-header-icon">📐</div>
            <div class="app-header-title">Teoria de Matemàtiques</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Tornar al menú", key="back_from_teoria"):
        go_to_page('home')
    
    with st.container():
        st.markdown('<div class="theory-container">', unsafe_allow_html=True)
        
        st.markdown("""
        <h2>📐 Conceptes matemàtics</h2>
        <p style="color:#636E72;margin-bottom:1rem;">Principals conceptes per resoldre els exercicis de càlcul.</p>
        """, unsafe_allow_html=True)
        
        # Índex
        st.markdown("""
        <div class="theory-toc">
            <h3>📑 Continguts</h3>
            <ul>
                <li><a href="#prioritat">1. Prioritat d'operacions</a></li>
                <li><a href="#percentatges">2. Percentatges</a></li>
                <li><a href="#regla3">3. Regla de 3</a></li>
                <li><a href="#geometria">4. Geometria bàsica</a></li>
                <li><a href="#mitjana">5. Mitjana aritmètica</a></li>
                <li><a href="#fraccions">6. Fraccions</a></li>
                <li><a href="#potencies">7. Potències</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 1. Prioritat d'operacions
        st.markdown("""
        <h3 id="prioritat">1. Prioritat d'operacions</h3>
        <p>L'ordre de les operacions és fonamental per resoldre expressions matemàtiques.</p>
        <div class="rule-box">
            <strong>📋 Ordre de prioritat:</strong><br>
            1. <strong>Parèntesis</strong> ( ) — Primer de tot<br>
            2. <strong>Potències i arrels</strong> x², √x<br>
            3. <strong>Multiplicació i divisió</strong> ×, ÷ — D'esquerra a dreta<br>
            4. <strong>Suma i resta</strong> +, − — D'esquerra a dreta
        </div>
        <div class="example">
            <strong>💡 Exemple:</strong> 8 + 3 × 2 = 8 + 6 = 14<br>
            <span style="color:#636E72;font-size:0.85rem;">Primer 3 × 2 = 6, després 8 + 6 = 14</span>
        </div>
        <div class="example">
            <strong>💡 Exemple:</strong> (6 + 4) × 3 = 10 × 3 = 30<br>
            <span style="color:#636E72;font-size:0.85rem;">Primer 6 + 4 = 10, després 10 × 3 = 30</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. Percentatges
        st.markdown("""
        <h3 id="percentatges">2. Percentatges</h3>
        <p>Un percentatge és una fracció amb denominador 100.</p>
        <div class="formula">Percentatge = (Part / Total) × 100</div>
        <div class="formula">Quantitat × (Percentatge / 100)</div>
        <div class="example">
            <strong>💡 Exemple:</strong> 20% de 80 = 80 × 0.20 = 16
        </div>
        <div class="example">
            <strong>💡 Exemple:</strong> Un producte de 40 € amb 25% de descompte:<br>
            Descompte: 40 × 0.25 = 10 € → Preu final: 30 €
        </div>
        """, unsafe_allow_html=True)
        
        # 3. Regla de 3
        st.markdown("""
        <h3 id="regla3">3. Regla de 3</h3>
        <p>La regla de 3 s'utilitza per resoldre problemes de proporcionalitat.</p>
        <h4>📋 Regla de 3 directa</h4>
        <div class="formula">a/b = c/x → x = (b × c) / a</div>
        <div class="example">
            <strong>💡 Exemple:</strong> 3 kg → 6 €, 5 kg → x = (6 × 5) / 3 = 10 €
        </div>
        <h4>📋 Regla de 3 inversa</h4>
        <div class="formula">a × b = c × x → x = (a × b) / c</div>
        <div class="example">
            <strong>💡 Exemple:</strong> 2 persones → 12 h, 4 persones → x = (2 × 12) / 4 = 6 h
        </div>
        """, unsafe_allow_html=True)
        
        # 4. Geometria
        st.markdown("""
        <h3 id="geometria">4. Geometria bàsica</h3>
        <div class="formula">Perímetre rectangle: P = 2 × (ample + llarg)</div>
        <div class="example"><strong>💡 Exemple:</strong> 6 cm × 8 cm → P = 2 × (6 + 8) = 28 cm</div>
        <div class="formula">Àrea quadrat: A = costat²</div>
        <div class="example"><strong>💡 Exemple:</strong> 5 cm → A = 5² = 25 cm²</div>
        <div class="formula">Àrea triangle: A = (base × altura) / 2</div>
        <div class="example"><strong>💡 Exemple:</strong> 6 cm × 4 cm → A = (6 × 4) / 2 = 12 cm²</div>
        """, unsafe_allow_html=True)
        
        # 5. Mitjana
        st.markdown("""
        <h3 id="mitjana">5. Mitjana aritmètica</h3>
        <div class="formula">Mitjana = Suma de tots els valors / Nombre de valors</div>
        <div class="example"><strong>💡 Exemple:</strong> Mitjana de 4, 8, 6: (4 + 8 + 6) / 3 = 18 / 3 = 6</div>
        """, unsafe_allow_html=True)
        
        # 6. Fraccions
        st.markdown("""
        <h3 id="fraccions">6. Fraccions</h3>
        <div class="formula">Suma: a/b + c/d = (a×d + c×b) / (b×d)</div>
        <div class="example"><strong>💡 Exemple:</strong> 3/4 + 1/2 = (3×2 + 1×4) / (4×2) = 10/8 = 5/4</div>
        <div class="formula">Producte: a/b × c/d = (a×c) / (b×d)</div>
        <div class="example"><strong>💡 Exemple:</strong> 2/3 × 3/4 = 6/12 = 1/2</div>
        <div class="formula">Divisió: a/b ÷ c/d = (a×d) / (b×c)</div>
        <div class="example"><strong>💡 Exemple:</strong> 5/8 ÷ 3/4 = (5×4) / (8×3) = 20/24 = 5/6</div>
        """, unsafe_allow_html=True)
        
        # 7. Potències
        st.markdown("""
        <h3 id="potencies">7. Potències</h3>
        <div class="formula">aⁿ = a × a × ... × a (n vegades)</div>
        <div class="example"><strong>💡 Exemple:</strong> 2³ = 2 × 2 × 2 = 8</div>
        <div class="example"><strong>💡 Exemple:</strong> 3² × 2³ = 9 × 8 = 72</div>
        <div class="formula">Arrel quadrada: √x = y si y² = x</div>
        <div class="example"><strong>💡 Exemple:</strong> √49 + √16 = 7 + 4 = 11</div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================
# PÀGINA: ORTOGRAFIA
# ==============================================================

def ortografia_page():
    st.markdown("""
    <div class="app-header">
        <div class="app-header-left">
            <div class="app-header-icon">📝</div>
            <div class="app-header-title">Regles Ortogràfiques</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Tornar al menú", key="back_from_ortografia"):
        go_to_page('home')
    
    with st.container():
        st.markdown('<div class="theory-container">', unsafe_allow_html=True)
        
        st.markdown("""
        <h2>📝 Regles ortogràfiques</h2>
        <p style="color:#636E72;margin-bottom:1rem;">Normes bàsiques per escriure correctament en català.</p>
        """, unsafe_allow_html=True)
        
        # Índex
        st.markdown("""
        <div class="theory-toc">
            <h3>📑 Continguts</h3>
            <ul>
                <li><a href="#alfabet">1. L'alfabet</a></li>
                <li><a href="#vocals">2. Les vocals</a></li>
                <li><a href="#apostrof">3. Apostrofació i contraccions</a></li>
                <li><a href="#esses">4. Les esses: s, ss, c, ç, z</a></li>
                <li><a href="#b-v">5. La b i la v</a></li>
                <li><a href="#ela-geminada">6. La ela geminada: l·l</a></li>
                <li><a href="#erra">7. La erra: r i rr</a></li>
                <li><a href="#g-j">8. La g i la j</a></li>
                <li><a href="#ix-x">9. La ix i la x</a></li>
                <li><a href="#accentuacio">10. L'accentuació gràfica</a></li>
                <li><a href="#diacritics">11. Els accents diacrítics</a></li>
                <li><a href="#dieresi">12. La dièresi</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 1. L'alfabet
        st.markdown("""
        <h3 id="alfabet">1. L'alfabet català</h3>
        <p>L'alfabet català té 27 lletres:</p>
        <div style="background:white;padding:0.8rem;border-radius:12px;border:1px solid #DFE6E9;text-align:center;font-size:1.1rem;letter-spacing:0.5px;font-weight:600;margin:0.5rem 0;">
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        </div>
        <p style="color:#636E72;font-size:0.9rem;">Les lletres <strong>K</strong>, <strong>W</strong> i <strong>Y</strong> només s'usen en paraules d'origen estranger.</p>
        """, unsafe_allow_html=True)
        
        # 2. Les vocals
        st.markdown("""
        <h3 id="vocals">2. Les vocals</h3>
        <p>El català té 7 vocals: a, e, i, o, u, <strong>è</strong> (oberta) i <strong>é</strong> (tancada).</p>
        <div class="rule-box">
            <strong>🔊 Vocals obertes:</strong> à, è, ò<br>
            <strong>🔊 Vocals tancades:</strong> é, í, ó, ú
        </div>
        <div class="example">
            <strong>💡 Exemples:</strong><br>
            • <strong>è</strong> oberta: cafè, pedra<br>
            • <strong>é</strong> tancada: café, té<br>
            • <strong>ò</strong> oberta: cançó, colònia<br>
            • <strong>ó</strong> tancada: camió, arròs
        </div>
        """, unsafe_allow_html=True)
        
        # 3. Apostrofació
        st.markdown("""
        <h3 id="apostrof">3. Apostrofació i contraccions</h3>
        <p>S'apostrofen els articles <strong>el, la, en</strong> i les preposicions <strong>de, per</strong> davant de paraula que comença per vocal o h.</p>
        <div class="example">
            <strong>💡 Exemples:</strong> l'home, l'escola, d'ahir
        </div>
        <div class="rule-box warning">
            <strong>⚠️ Excepcions:</strong> No s'apostrofa davant de <strong>la, una</strong>, o davant de paraules que comencen per <strong>i</strong> o <strong>u</strong> àtones.
        </div>
        <p><strong>📋 Contraccions:</strong></p>
        <div class="example">
            • de + el = <strong>del</strong> → el llibre <strong>del</strong> noi<br>
            • per + el = <strong>pel</strong> → <strong>pel</strong> camí
        </div>
        """, unsafe_allow_html=True)
        
        # 4. Les esses
        st.markdown("""
        <h3 id="esses">4. Les esses: s, ss, c, ç, z</h3>
        <div class="rule-box">
            <strong>🔤 S</strong> — A començament de paraula, entre vocals (sonora), davant de consonant<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: sopa, casa, escola</span>
        </div>
        <div class="rule-box warning">
            <strong>🔤 SS</strong> — Entre vocals (sorda)<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: passar, cassola</span>
        </div>
        <div class="rule-box">
            <strong>🔤 C/Ç</strong> — Ç davant de <strong>a, o, u</strong>; C davant de <strong>e, i</strong><br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: braç, plaça, cervesa, ciència</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 5. La b i la v
        st.markdown("""
        <h3 id="b-v">5. La b i la v</h3>
        <div class="rule-box">
            <strong>🔤 B</strong> — Davant de <strong>l</strong> o <strong>r</strong>, en paraules que comencen per <strong>ab-, ob-, sub-</strong><br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: bla, bra, abans, obtenir</span>
        </div>
        <div class="rule-box">
            <strong>🔤 V</strong> — En paraules que comencen per <strong>ev-, ov-</strong><br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: evitar, ovella</span>
        </div>
        <div class="rule-box danger">
            <strong>⚠️ Atenció!</strong> Aquesta és una de les regles que més dubtes genera.
        </div>
        """, unsafe_allow_html=True)
        
        # 6. La ela geminada
        st.markdown("""
        <h3 id="ela-geminada">6. La ela geminada: l·l</h3>
        <p>La ela geminada <strong>l·l</strong> és un so característic del català.</p>
        <div class="rule-box">
            <strong>🔤 S'escriu l·l</strong> en paraules on hi ha dos sons <strong>l</strong> separats<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: col·legi, il·lusió, intel·ligent, novel·la</span>
        </div>
        <div class="rule-box danger">
            <strong>⚠️ Important!</strong> La ela geminada <strong>no</strong> és una <strong>l</strong> doble normal (ll). Són sons diferents!
        </div>
        """, unsafe_allow_html=True)
        
        # 7. La erra
        st.markdown("""
        <h3 id="erra">7. La erra: r i rr</h3>
        <div class="rule-box">
            <strong>🔤 R</strong> — A començament de paraula, entre vocals (vibrant simple)<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: ram, rosa, cara, hora</span>
        </div>
        <div class="rule-box">
            <strong>🔤 RR</strong> — Entre vocals (vibrant múltiple)<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: carro, terra, arrencar</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 8. La g i la j
        st.markdown("""
        <h3 id="g-j">8. La g i la j</h3>
        <div class="rule-box">
            <strong>🔤 G</strong> — Davant de <strong>e, i</strong> (so suau) o davant de <strong>a, o, u</strong> (so dur)<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: gent, girar, gat, gota, gust</span>
        </div>
        <div class="rule-box">
            <strong>🔤 J</strong> — Davant de <strong>a, o, u</strong><br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: ja, jo, jove, ajuda</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 9. La ix i la x
        st.markdown("""
        <h3 id="ix-x">9. La ix i la x</h3>
        <div class="rule-box">
            <strong>🔤 IX</strong> — Entre vocals<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: caixa, aixeta, exemple</span>
        </div>
        <div class="rule-box">
            <strong>🔤 X</strong> — A començament de paraula o al final<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: xarxa, xocolata, peix, reflex</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 10. L'accentuació
        st.markdown("""
        <h3 id="accentuacio">10. L'accentuació gràfica</h3>
        <div class="rule-box">
            <strong>🔤 Paraules agudes</strong> (última síl·laba): s'accentuen si acaben en vocal, -s, -en, -in<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: cafè, cançó, camí</span>
        </div>
        <div class="rule-box">
            <strong>🔤 Paraules planes</strong> (penúltima): s'accentuen si <strong>no</strong> acaben en vocal, -s, -en, -in<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: llàgrima, difícil, cànon</span>
        </div>
        <div class="rule-box">
            <strong>🔤 Paraules esdrúixoles</strong> (antepenúltima): sempre s'accentuen<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: pàgina, lògica, càntic</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 11. Accents diacrítics
        st.markdown("""
        <h3 id="diacritics">11. Els accents diacrítics</h3>
        <p>L'accent diacrític diferencia paraules que s'escriuen igual però tenen significats diferents.</p>
        <div class="example">
            <strong>💡 Exemples:</strong><br>
            • <strong>sé</strong> (saber) vs <strong>se</strong> (pronom)<br>
            • <strong>és</strong> (verb ser) vs <strong>es</strong> (pronom)<br>
            • <strong>més</strong> (quantitat) vs <strong>mes</strong> (mes)<br>
            • <strong>dóna</strong> (verb donar) vs <strong>dona</strong> (femella)
        </div>
        """, unsafe_allow_html=True)
        
        # 12. La dièresi
        st.markdown("""
        <h3 id="dieresi">12. La dièresi</h3>
        <p>La dièresi (¨) marca que una <strong>u</strong> es pronuncia en els grups <strong>gue, gui, que, qui</strong>.</p>
        <div class="rule-box">
            <strong>🔤 S'usa en</strong> güe, güi, qüe, qüi<br>
            <span style="color:#636E72;font-size:0.85rem;">💡 Exemples: aigües, qüestió, pingüí, argüir, ambigüitat</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================
# PÀGINA: MEMORITZACIÓ
# ==============================================================

def memorization_page():
    st.markdown("""
    <div class="app-header">
        <div class="app-header-left">
            <div class="app-header-icon">👁️</div>
            <div class="app-header-title">Memorització Visual</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Tornar a configuració", key="back_from_mem"):
        st.session_state.mem_phase = 'viewing'
        go_to_page('practica')
    
    with st.container():
        st.markdown('<div class="memorization-container">', unsafe_allow_html=True)
        
        if st.session_state.mem_phase == 'viewing':
            # Mostrar imatge
            if st.session_state.image_file:
                st.image(st.session_state.image_file, caption='👀 Memoritza aquesta imatge', use_container_width=True)
            
            # Timer
            view_time = st.session_state.view_time
            st.markdown(f'<div class="memorization-timer">⏱ {view_time}</div>', unsafe_allow_html=True)
            
            # Quadre de notes
            st.session_state.mem_notes = st.text_area('📝 Prendre notes', height=100,
                                                       placeholder='Escriu aquí les teves notes...',
                                                       key='mem_notes_area')
            
            # Barra de progrés
            progress_bar = st.progress(0)
            for i in range(view_time):
                progress_bar.progress((i + 1) / view_time)
                time.sleep(1)
            
            st.session_state.mem_phase = 'writing'
            st.rerun()
        
        elif st.session_state.mem_phase == 'writing':
            st.markdown('<h3 style="color:#2D3436;">✍️ Escriu el que recordes</h3>', unsafe_allow_html=True)
            st.info('La imatge ja no es mostra. Escriu tot el que recordis.')
            
            user_text = st.text_area('El teu text', height=200,
                                      placeholder='Escriu aquí tot el que recordis de la imatge...',
                                      key='mem_user_text')
            
            if st.button('🔍 Comparar', use_container_width=True, type="primary", key="btn_compare"):
                # Mostrar resultats
                st.markdown('<h3 style="color:#2D3436;margin-top:1.5rem;">📊 Comparació</h3>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<p style="font-weight:600;color:#2D3436;">🖼️ Imatge original</p>', unsafe_allow_html=True)
                    if st.session_state.image_file:
                        st.image(st.session_state.image_file, use_container_width=True)
                
                with col2:
                    st.markdown('<p style="font-weight:600;color:#2D3436;">✍️ El que has escrit</p>', unsafe_allow_html=True)
                    st.markdown(f"""
                    <div style="background:#F5F8FC;padding:1rem;border-radius:12px;min-height:120px;border:1px solid #DFE6E9;font-size:0.95rem;color:#2D3436;">
                        {user_text if user_text else '<span style="color:#636E72;">(No has escrit res)</span>'}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('<p style="font-weight:600;color:#2D3436;margin-top:0.5rem;">📝 Notes preses</p>', unsafe_allow_html=True)
                st.markdown(f"""
                <div style="background:#F5F8FC;padding:1rem;border-radius:12px;border:1px solid #DFE6E9;font-size:0.95rem;color:#2D3436;">
                    {st.session_state.mem_notes if st.session_state.mem_notes else '<span style="color:#636E72;">(No has pres notes)</span>'}
                </div>
                """, unsafe_allow_html=True)
                
                if st.button('🔄 Tornar a començar', use_container_width=True, key="btn_restart_mem"):
                    st.session_state.mem_phase = 'viewing'
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================
# ROUTER PRINCIPAL
# ==============================================================

# Navegació segons l'estat
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'practica':
    practica_page()
elif st.session_state.page == 'quiz':
    quiz_page()
elif st.session_state.page == 'results':
    results_page()
elif st.session_state.page == 'teoria':
    teoria_page()
elif st.session_state.page == 'ortografia':
    ortografia_page()
elif st.session_state.page == 'memorization':
    memorization_page()
