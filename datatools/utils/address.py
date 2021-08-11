import re

class IPv4:
    def __init__(self, address, prefix):
        if IPv4.validip(address) and IPv4.validprefix(prefix):
            self.address = address
            self.prefix = prefix
        else:
            raise Exception('Invalid Argument')
    
    def netmask(self):
        prefix = int(self.prefix)
        mask = []
        for i in range(4):
            if prefix >= 8:
                mask.append('255')
                prefix -= 8
            else:
                mask.append(256 - 2 ** (8 - prefix))
                prefix = 0
        return '{}.{}.{}.{}'.format(*mask)

    def netaddress(self):
        address = IPv4.asbits(self.address, toflat=True)
        netmask = IPv4.asbits(self.netmask(), toflat=True)
        netaddress = []
        for addr, netm in zip(address, netmask):
            netaddress.append(1 if addr == 1 and netm == 1 else 0)
        return IPv4.asstr(IPv4.asint(netaddress, fromflat=True, frombinary=True, toflat=False))

    def broadcastaddress(self):
        willcard = IPv4.notaddress(self.netmask())
        return IPv4.addressadder(self.netaddress(), willcard)

    def hostrange(self):
        hosts, host = [], self.netaddress()
        while self.within(host):
            hosts.append(host)
            host = IPv4.addressadder(host, '0.0.0.1')
        return hosts

    def within(self, address):
        if IPv4.validip(address):
            address = IPv4(address, self.prefix)
            return self.netaddress() == address.netaddress()
        else:
            raise Exception('Invalid Argument')

    @staticmethod
    def notaddress(address):
        if IPv4.validip(address):
            address = IPv4.asbits(address, toflat=True)
            result = [0 if bit == 1 else 1 for bit in address]
            return IPv4.asstr(IPv4.asint(result, fromflat=True, frombinary=True, toflat=False))
        raise Exception('Invalid Argument') 

    @staticmethod
    def addressadder(address1, address2):
        if IPv4.validip(address1) and IPv4.validip(address2):
            address = IPv4.asint(address1, toflat=True) + IPv4.asint(address2, toflat=True)
            return IPv4.asstr(address, fromflat=True)
        raise Exception('Invalid Argument') 

    @staticmethod
    def asstr(address, fromflat=False):
        if fromflat:
            return IPv4.asstr(IPv4.asint(address, fromflat=True, toflat=False))
        else:
            if len(address) == 4:
                address = '{}.{}.{}.{}'.format(*address)
                if IPv4.validip(address):
                    return address
        raise Exception('Invalid Argument') 

    @staticmethod
    def asint(address, fromflat=False, frombinary=False, toflat=True):
        if frombinary:
            if not fromflat:
                address = tuple([bit for byte in address for bit in byte])
            if len(address) == 32 and set(address) == {0, 1}:
                addresslist = []
                for o in range(4):
                    value = 0
                    for i in range(8):
                        j = i + 8 * o
                        value += address[j] * 2 ** (7 - i)
                    addresslist.append(value)
                if toflat:
                    return IPv4.asint(IPv4.asstr(addresslist), toflat=True)
                return addresslist
        else:
            if fromflat:
                o4 = int(address/(256**3))
                o3 = int(address/(256**2)) - o4*(256**1)
                o2 = int(address/(256**1)) - o4*(256**2) - o3*(256**1)
                o1 = int(address/(256**0)) - o4*(256**3) - o3*(256**2) - o2*(256**1)
                octects = (o4, o3, o2, o1)
            else:
                octects = [int(octect) for octect in address.split('.')]
            if toflat:
                return octects[-1] + octects[-2]*256 + octects[-3]*(256**2) + octects[-4]*(256**3)
            return octects
        raise Exception('Invalid Argument')       
        
    @staticmethod
    def asbits(address, toflat=False):
        if IPv4.validip(address):
            octects = IPv4.tooctects(address)
            result = [IPv4.tobits(octect) for octect in octects]
            if toflat:
                return tuple([bit for byte in result for bit in byte])
            return tuple(result)
        raise Exception('Invalid Argument')   
        
    @staticmethod
    def validip(address):
        regex = r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
        match = re.match(regex, str(address))
        if match:
            valid = True
            for i in range(1, 5):
                valid = valid and IPv4.validoctect(match.group(i))
            return valid
        return False

    @staticmethod
    def validprefix(prefix):
        regex = r'^[0-9]+$'
        if re.match(regex, str(prefix)):
            prefix = int(prefix)
            return (prefix >= 0 and prefix <=32) 
        return False

    @staticmethod
    def validoctect(octect):
        regex = r'^[0-9]+$'
        if re.match(regex, str(octect)):
            octect = int(octect)
            return (octect >= 0 and octect <=255) 
        return False

    @staticmethod
    def tooctects(address):
        if IPv4.validip(address):
            return tuple(address.split('.'))
        else:
            raise Exception('Invalid Argument')

    @staticmethod
    def tobits(octect):
        if IPv4.validoctect(octect):
            num = int(octect)
            byte = []
            for i in range(8):
                value = 2 ** (7 - i)
                if num >= value:
                    num -= value
                    byte.append(1)
                else:
                    byte.append(0)
            return tuple(byte)
        raise Exception('Invalid Argument')

    