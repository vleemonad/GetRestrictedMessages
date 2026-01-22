from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

API_ID = int(input("Enter API_ID: ").strip())
API_HASH = input("Enter API_HASH: ").strip()


async def main():
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print("\nYour SESSION string:")
        print(client.session.save())
        print("\nCopy this whole line and paste it into your SESSION env variable.")


if __name__ == "__main__":
    asyncio.run(main())
