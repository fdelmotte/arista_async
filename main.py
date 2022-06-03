# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

import asyncio


# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

import dwarf


username = 'dwarf'
password = 'arista'
inventory_devices = ["192.168.59.151", "192.168.59.152", "192.168.59.150"]

if __name__ == '__main__':
    asyncio.run(dwarf.main(inventory=inventory_devices, username=username, password=password))