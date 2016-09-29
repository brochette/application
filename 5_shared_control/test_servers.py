# -*- coding: utf-8 -*-
import struct, socket, threading, time, random, sys, logging
import pytia
from pytia import TiAServer, TiAConnectionHandler, TiASignalConfig

def cb(id):
    return [10*id, 20*id, 30*id, 40*id, 50*id, 60*id]

if __name__ == "__main__":
    server = TiAServer(('', 9000), TiAConnectionHandler)
    types = [pytia.TIA_SIG_SENSORS, pytia.TIA_SIG_USER_1]
    server.start([TiASignalConfig(channels=3, sample_rate=2, blocksize=2, callback=cb, id=i, is_master=i == 0, sigtype=types[i]) for i in range(2)])
    print('Signal types:', types)
    print('Waiting for requests')

    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        pass

    print ('Exiting')


