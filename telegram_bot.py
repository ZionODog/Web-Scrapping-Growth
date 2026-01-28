import asyncio
from telegram import Bot
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

async def get_chat_id():
    bot = Bot(token=TOKEN)
    # Pega as ultimas mensagens enviadas para o bot
    updates = await bot.get_updates()
    
    if updates:
        # Pega o ID da última pessoa/grupo que falou com o bot
        last_chat_id = updates[-1].message.chat_id
        user_name = updates[-1].message.chat.first_name
        print(f"✅ Mensagem recebida de: {user_name}")
        print(f"🆔 O CHAT_ID correto é: {last_chat_id}")
    else:
        print("❌ Nenhuma mensagem encontrada. Envie um 'Oi' para o bot no Telegram primeiro.")

if __name__ == "__main__":
    asyncio.run(get_chat_id())