import asyncio

from blockgamebot.api import Scammers

scammers = Scammers("###")

async def main():

    # Get all scammers
    all_scammers = await scammers.get_all()
    print(all_scammers)

    # Lookup a scammer
    scammer = await scammers.lookup("asov")
    print(scammer)

asyncio.run(main())