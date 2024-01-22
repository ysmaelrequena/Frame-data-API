from fastapi import FastAPI
from pydantic import BaseModel
from character_class import *

app = FastAPI()
ryu = Character(name="ryu", url='https://wiki.supercombo.gg/w/Street_Fighter_6/Ryu')

async def wait_ryu():
    return asyncio.run(ryu.get_framedata())


@app.get("/ryu")

async def ryu():
    result = await wait_ryu()
    
    return {result}