import aiohttp

class Scammers:
    def __init__(self, api_key, session:aiohttp.ClientSession=None):

        self.key = api_key

        self.session = session
        self.urls = {
            "all": f"https://api.nom-nom.link/scammers?key={self.key}",
            "lookup": f"https://api.nom-nom.link/lookup/scammer/ARGUMENTS?key={self.key}",
        }

    
    async def get_all(self):

        if self.session is None:
            self.session = aiohttp.ClientSession()
        
        async with self.session.get(self.urls["all"]) as resp:
            jsonResponse = await resp.json()
            await self.session.close()
        
        return jsonResponse
        
    async def lookup(self, argument):

        if self.session is None:
            self.session = aiohttp.ClientSession()
            
        async with self.session.get(self.urls["lookup"].replace("ARGUMENTS", argument)) as resp:
            jsonResponse = await resp.json()
            await self.session.close()
        
        return jsonResponse
        
class itemImages:
    def __init__(self, session:aiohttp.ClientSession=None):

        self.session = session
        self.urls = {
            "base": "https://api.nom-nom.link/skyblock/items/{variation}/{item}/"
        }

        self.variations = ["normal", "enchanted"]


    async def get_image(self, item:str, variation="normal"):

        if self.session is None:
            self.session = aiohttp.ClientSession()
        
        error = ""

        if variation.lower() not in self.variations:
            error += (f"Variations must be one of the following: {self.variations}, defaulting to 'normal'. ")
            variation = "normal"
            
        response = self.urls["base"].replace("{variation}", variation).replace("{item}", item.upper()) 
        async with self.session.get(response) as resp:
            if resp.status == 404:
                error += f"The item '{item}' does not exist, defaulting to 'barrier'."
                item = "barrier"
                response = self.urls["base"].replace("{variation}", variation).replace("{item}", item.upper())
            await self.session.close()
        
        return {"url": response, "error": error}
