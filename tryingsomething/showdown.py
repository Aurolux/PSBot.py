#Import aiohttp (a dependency) and asyncio (included in the standard library)
import aiohttp, asyncio

#The PS websocket URL.
MAIN = 'ws://sim.smogon.com:8000/showdown/websocket'


#This will be our main class for our bot. It handles the websocket connection.
class PSBot:

    def __init__(self):
        #Our asyncio loop so we can handle PS sending multiple messages at the same time
        self.loop = asyncio.get_event_loop()


    #Run this function with the PS server URL to connect.
    def connect(self, server):

        #Runs our clientLoop function forever. We need to always have this running to get new messages from PS.
        self.loop.run_until_complete(self.clientLoop(server))
        self.loop.close()

 

    async def clientLoop(self, server):
        
        #This part is a little complicated - we use aiohttp to create a client session
        session = aiohttp.ClientSession()

        #And then we use that to connect to a URL's websocket (session.ws_connect(server)).
        async with session.ws_connect(server) as ws:
            #We want to keep a reference to the websocket, so we save it into our class as self.websocket.
            self.websocket = ws

            #This part handles the messages we get from PS.
            async for msg in ws:
                #Making sure it's a plaintext message.
                if msg.type == aiohttp.WSMsgType.TEXT:

                    #str(msg.data) is our plaintext message - we add this to our asyncio event loop to handle it concurrently.
                    self.loop.create_task(self.DATAHANDLEFUNCTION(str(msg.data)))



    #This method allows us to use our self.websocket to send a message to PS. I believe "return r" will always return None.
    async def send(self, message):
        r = await self.websocket.send_str(message)
        return r



    async def DATAHANDLEFUNCTION(self, message):
        messages = message.split('\n')
        for i in messages:
            print(messages)
        #PS will constantly be sending messages to you. Handle them here.
