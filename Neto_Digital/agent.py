from datetime import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    city_lower = city.lower()
    if city_lower == "new york":
        return {
            "status": "success",
            "report": "The weather in New York is sunny with a temperature of 25°C."
        }
    elif city_lower in ["salvador", "salvador, bahia", "salvador bahia"]:
        return {
            "status": "success",
            "report": "O tempo em Salvador, Bahia está ensolarado com temperatura em torno de 28°C."
        }
    else:
        return {
            "status": "error",
            "error_message": f"No weather info for {city}."
        }

def get_current_time(city: str) -> dict:
    city_lower = city.lower()
    if city_lower == "new york":
        tz = ZoneInfo("America/New_York")
    elif city_lower in ["salvador", "salvador, bahia", "salvador bahia"]:
        tz = ZoneInfo("America/Bahia")
    else:
        return {
            "status": "error",
            "error_message": f"Timezone not known for {city}."
        }

    now = datetime.now(tz)
    return {
        "status": "success",
        "report": f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    }

def saudacao_por_horario():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia"
    elif 12 <= hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

saudacao = saudacao_por_horario()

root_agent = Agent(
    name="neto_digital",
    model="gemini-2.0-flash",
    description="Agente para idosos em compras online.",
    instruction=(
        f"Você é o Neto Digital, um assistente virtual gentil, paciente e muito educado.\n"
        f"Quando a conversa começar, faça o seguinte:\n"
        f"1. Cumprimente o usuário com '{saudacao}'.\n"
        f"2. Depois diga: 'No que posso ajudar?'.\n"
        f"3. Espere a pessoa falar.\n"
        f"4. Responda com calma, usando palavras simples e explicando tudo passo a passo mas que seja de forma direta e breve.\n"
        f"5. Se a pessoa pedir ajuda, ofereça informações claras e fáceis de entender.\n"
        f"6. Nunca use palavras difíceis ou técnicas.\n"
    ),
    tools=[get_weather, get_current_time],
)