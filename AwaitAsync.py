# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:31:52 2021

@author: LuizF
"""
import numpy as np
import asyncio
import random

async def print_number(i):
    print(i, 'start')
    await asyncio.sleep(random.random())
    print(i, 'done')

async def main():
    await asyncio.wait([
        asyncio.create_task(print_number(i))
        for i in range(10)
    ])
    print('main done')

asyncio.run(main())

