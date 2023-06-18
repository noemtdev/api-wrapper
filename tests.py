import asyncio

from blockgamebot.api import Scammers

scammers = Scammers("LY4z8aCG1e9V3da64e1D1egbAddd4aafr13ef34ec8")

async def main():

    # Get all scammers
    all_scammers = await scammers.get_all()
    print(all_scammers)

    # Lookup a scammer
    scammer = await scammers.lookup("asov")
    print(scammer)

asyncio.run(main())