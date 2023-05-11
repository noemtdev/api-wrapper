import asyncio

from blockgamebot.api import Scammers, itemImages

scammers = Scammers("BLOCKGAMEBOT_API_KEY")
images = itemImages()

async def main():

    # Get all scammers
    all_scammers = await scammers.get_all()
    print(all_scammers)

    # Lookup a scammer
    scammer = await scammers.lookup("asov") # First part of tag, whole tag or discord ID may be used
    print(scammer)

    # Get an item image
    url = await images.get_image("bread", variation="enchanted") # Variation defaults to "normal", options are "normal" or "enchanted"
    print(url)

asyncio.run(main())
