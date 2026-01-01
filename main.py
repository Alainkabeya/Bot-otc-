import requests
import os
import random
from datetime import datetime

# === TELEGRAM ===
BOT_TOKEN = os.getenv = "8218898659:AAHRRAlrQxpCHDG7AydgtnTbLvAVwZ8VtFE"
CHAT_ID = os.getenv = "1175920056"

# === PARAMÈTRES OTC ===
PAIR = "AUD/USD OTC"
TIMEFRAME = "1 MIN"
PROBABILITY_THRESHOLD = 65  # % minimum pour envoyer signal

def generate_fake_market_data():
    """
    Simulation logique OTC (car données OTC fermées)
    """
    trend = random.choice(["UP", "DOWN", "RANGE"])
    volatility = random.randint(1, 10)
    return trend, volatility

def otc_strategy():
    trend, volatility = generate_fake_market_data()

    if trend == "UP" and volatility <= 6:
        return "CALL", random.randint(65, 85)

    if trend == "DOWN" and volatility <= 6:
        return "PUT", random.randint(65, 85)

    return None, 0

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

def main():
    signal, probability = otc_strategy()

    if signal and probability >= PROBABILITY_THRESHOLD:
        now = datetime.utcnow().strftime("%H:%M UTC")
        message = (
            f"📊 SIGNAL OTC\n\n"
            f"Pair : {PAIR}\n"
            f"Timeframe : {TIMEFRAME}\n"
            f"Signal : {signal}\n"
            f"Probabilité : {probability}%\n"
            f"Heure : {now}\n\n"
            f"⏳ Expiration : 1 minute\n"
            f"⚠️ Gestion du risque obligatoire"
        )
        send_telegram(message)
    else:
        print("Aucun signal valide cette minute")

if __name__ == "__main__":
    main()
