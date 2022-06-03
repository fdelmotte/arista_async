# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

import asyncio
import time


# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from aioeapi import Device


# -----------------------------------------------------------------------------
#
#                                 CODE BEGINS
#
# -----------------------------------------------------------------------------

async def get_information(host: str, username, password):
    async with Device(host=host, username=username, password=password, proto='http', port=80) as dev:
        '''Check the connectivity before sending the command'''
        if await dev.check_connection():
            result = await dev.cli(commands=['show version'])
            return host, result
        return host, "None"


async def main_function(inventory, username, password):
    commands_info = []
    """Build the list of tasks"""
    tasks = [get_information(host=host, username=username, password=password) for host in inventory]
    for this_dev in asyncio.as_completed(tasks):
        commands_info.append(await this_dev)
    return commands_info


async def main(inventory, username, password):
    start = time.time()
    result = await main_function(inventory, username, password)
    end = time.time()
    print(end - start)
    # print(result)
    for record in result:
        print(result[0][1][0]['version'])
