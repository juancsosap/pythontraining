# -*- coding: utf-8 -*-

import socket
import time
import pickle
import logging

from threading import Thread
from threading import Lock

from consoletools import getch


class Message:

    def __init__(self, nick, message):
        self.__nick = nick
        self.__datetime = time.time()
        self.__message = message

    @property
    def datetime(self):
        return self.__datetime

    @property
    def message(self):
        return self.__message

    @property
    def nick(self):
        return self.__nick


class Chat:

    def __init__(self, host='127.0.0.1', port=5000,
                 servermode=True, protocol='udp', peers=10):
        self.__socketinfo = (str(host), int(port))
        self.__servermode = bool(servermode)
        self.__protocol = str(protocol)
        self.__peers = int(peers)

        self.__isactive = False
        self.__lock = Lock()

    @property
    def socketinfo(self):
        return self.__socketinfo

    @property
    def servermode(self):
        return self.__servermode

    @property
    def protocol(self):
        return self.__protocol

    @property
    def peers(self):
        return self.__peers

    @property
    def isactive(self):
        return self.__isactive

    def __getinput(self):
        msg = ''
        char = ''
        while char != '\\r':
            if char == '\\x08':
                if len(msg) > 0:
                    msg = msg[:-1]
                    print('\b \b')
            else:
                msg += char
            self.__lock.acquire()
            self.__current = f'\r{self.__nick} -> {msg}'
            print(self.__current, end='')
            self.__lock.release()
            char = getch()
        print()
        return msg

    def __loggingconfig(self):
        LOG_FORMAT = '%(levelname)s - %(asctime)s - %(message)s'
        logging.basicConfig(filename='chatserver.log',
                            level=logging.DEBUG,
                            format=LOG_FORMAT,
                            filemode='a')
        self.__logger = logging.getLogger()

    # Init the Client
    def init(self):
        if not self.servermode:
            if self.protocol == 'udp':
                self.__initudp()
            elif self.protocol == 'tcp':
                self.__inittcp()
        else:
            print('Only could be initiated in client mode.')
        self.__isactive = True

    def __initudp(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.setblocking(False)

        self.__nick = input('Nick: ')

        trecv = Thread(target=self.__recvudp)
        trecv.start()

        tsend = Thread(target=self.__sendudp)
        tsend.start()

        trecv.join()
        tsend.join()

        self.__isactive = False
        self.__socket.close()

    def __recvudp(self):
        while self.__isactive:
            try:
                self.__lock.acquire()
                data, addr = self.__socket.recvfrom(1024)
                msg = pickle.loads(data)
                print(f'\r{msg.datetime}|{msg.nick} <- {msg.message}')
                print(self.__current)
            except:
                pass
            finally:
                self.__lock.release()

    def __sendudp(self):
        msg = ''
        while msg != ':quit':
            print(f'{self.__nick} -> ', end='')
            msg = self.__getinput()
            if msg != '':
                self.__lock.acquire()
                data = pickle.dumps(Message(self.__nick, msg))
                self.__socket.sendto(data, self.socketinfo)
                self.__lock.release()

    def __inittcp(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect(self.socketinfo)
        self.__socket.setblocking(False)

        self.__nick = input('Nick: ')

        trecv = Thread(target=self.__recvtcp)
        trecv.start()

        tsend = Thread(target=self.__sendtcp)
        tsend.start()

        self.__isactive = False

        trecv.join()
        tsend.join()

        self.__socket.close()

    def __recvtcp(self):
        while self.__isactive:
            try:
                self.__lock.acquire()
                data = self.__socket.recv(1024)
                if data:
                    msg = pickle.loads(data)
                    print(f'\r{msg.datetime}|{msg.nick} <- {msg.message}')
                    print(self.__current)
            except Exception as e:
                self.__logger.error(e)
            finally:
                self.__lock.release()

    def __sendtcp(self):
        msg = ''
        while msg != ':quit':
            print(f'{self.__nick} -> ', end='')
            msg = self.__getinput()
            if msg != '':
                self.__lock.acquire()
                data = pickle.dumps(Message(self.__nick, msg))
                self.__socket.send(data)
                self.__lock.release()

    # Start the Server
    def start(self):
        self.__loggingconfig()
        if self.servermode:
            if self.protocol == 'udp':
                Thread(target=self.__startudp).start()
            elif self.protocol == 'tcp':
                Thread(target=self.__starttcp).start()
        else:
            print('Only could be started in server mode.')

    def __startudp(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(self.socketinfo)
        self.__socket.setblocking(False)

        self.__logger.debug('Server in UDP mode Starting.')

        self.__meeting = input('Meeting Name: ')

        self.__logger.debug(f'Meeting Name set to {self.__meeting}.')

        tprocess = Thread(target=self.__processudp)
        tprocess.start()

        self.__logger.debug('Server in UDP Mode Started.')

        while self.__isactive:
            cmd = input('CMD -> ')
            if cmd == ':quit':
                self.close()

        tprocess.join()

        self.__socket.close()

        self.__logger.debug('Server in UDP Mode Shutdown.')

    def __processudp(self):
        self.__clients = []
        while self.isactive:
            try:
                data, addr = self.__socket.recvfrom(1024)
                self.__logger.debug(f'Message received from {addr} client.')
                if addr not in self.__clients:
                    self.__clients.append(addr)
                    msg = f'Welcome to the {self.__meeting} meeting.'
                    data = pickle.dumps(Message('ROOT', msg))
                    self.__socket.sendto(data, addr)
                    msg = f'Currently there are {len(self.__clients)} connected.'
                    data = pickle.dumps(Message('ROOT', msg))
                    self.__socket.sendto(data, addr)
                    self.__logger.debug(f'Meeting Information send to {addr} Client.')

                for client in self.__clients:
                    if client != addr:
                        self.__socket.sendto(data, client)
            except Exception as e:
                self.__logger.error(e)
                self.__logger.debug('Server in UDP Mode Shutting down for erros.')
                self.close()

    def __starttcp(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind(self.socketinfo)
        self.__socket.listen(self.peers)
        self.__socket.setblocking(False)

        self.__logger.debug('Server in TCP Mode Starting.')

        self.__meeting = input('Meeting Name: ')

        self.__logger.debug(f'Meeting Name set to {self.__meeting}.')

        tacept = Thread(target=self.__acepttcp)
        tacept.start()

        tprocess = Thread(target=self.__processtcp)
        tprocess.start()

        self.__logger.debug('Server in TCP Mode Started.')

        while self.__isactive:
            cmd = input('CMD -> ')
            if cmd == ':quit':
                self.close()

        tacept.join()
        tprocess.join()

        self.__socket.close()

        self.__logger.debug('Server in TCP Mode Shutdown.')

    def __acepttcp(self):
        self.__clients = []
        while self.isactive:
            try:
                conn, addr = self.__socket.accept()
                conn.setblocking(False)
                self.__clients.append(conn)
                self.__logger.debug(f'Connected client {addr}.')
            except Exception as e:
                self.__logger.error(e)
                self.__logger.debug('Server in TCP Mode Shutting down for erros.')
                self.stop()

    def __processtcp(self):
        while self.isactive:
            if len(self.__clients) > 0:
                for clientConn in self.__clients:
                    try:
                        data = clientConn.recv(1024)
                        if data:
                            msg = pickle.load(data)
                            self.__logger.debug(f'Message received from {msg.nick} client.')
                            self.__logger.debug(f'Message from {msg.nick} send.')
                            for clientConnD in self.__clients:
                                try:
                                    if clientConnD != clientConn:
                                        clientConnD.send(data, clientConnD)
                                except Exception as e:
                                    self.__clients.remove(clientConnD)
                                    self.__logger.error(e)
                                    self.__logger.debug(f'Connection with Client {clientConnD} removed.')

                    except Exception as e:
                        self.__logger.error(e)
                        self.__logger.debug('Server in TCP Mode Shutting down for erros.')
                        self.stop()

    def stop(self):
        if self.servermode:
            if self.isactive:
                self.__isactive = False
                self.__logger.debug('Server Stopping.')
        else:
            print('Only could be stopped in server mode.')


if __name__ == '__main__':
    pass
