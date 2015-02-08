from datetime import datetime
import time
import usb.core
import usb.util



class USBScaleSingleton(object):
    """
    Singleton class for the DymoUSBScale

    (Useful to avoid repeatedly creating/destroying
    instances of the scale)
    """
    def __new__(self,**kwargs):
        try:
            return self.scale
        except AttributeError:
            self.scale = DymoUSBScale(**kwargs)
            return self.scale




class DymoUSBScale(object):
    """
    Driver for Dymo USB postage scale
    """

    def __init__(self,sleep_time=1.0,init=True):
        self.VENDOR_ID = 0x0922
        self.PRODUCT_ID = 0x8004
        self.DATA_MODE_GRAMS = 2
        self.DATA_MODE_OUNCES = 11

        if init:
            self.device_init()



    def device_init(self):

        # find the USB device
        self.device = usb.core.find(idVendor=self.VENDOR_ID,
                                   idProduct=self.PRODUCT_ID)
        try:
            self.device.detach_kernel_driver(0)
        except Exception, e:
            print "Unable to detach USB device from kernel driver. Continuing..."
            pass
 
        # use the first/default configuration
        self.device.set_configuration()

        # first endpoint
        endpoint = self.device[0][(0,0)][0]

        # see charlesreid1.com/wiki/USB_Scale/RaspberryPi
        self.ea = endpoint.bEndpointAddress
        self.ps = endpoint.wMaxPacketSize

        try:
            self.device.read(self.ea, self.ps)
        except usb.core.USBError:
            pass


    def read_value(self):

        # flush out the first few data values
        preload = 3
        while preload > 0:
            try:
                self.device.read(self.ea,self.ps)
            except usb.core.USBError:
                pass
            preload -= 1


        # read a data packet
        attempts = 3
        data = None
        while data is None and attempts > 0:
            try:
                data = self.device.read(self.ea, self.ps)
            except usb.core.USBError as e:
                data = None
                if e.args == ('Operation timed out',):
                    attempts -= 10
                    continue
 
        raw_weight = data[4] + data[5] * 256

        data_mode = data[2]

        return datetime.now(), raw_weight, data_mode





    def get_weight(self,mode):
        return self.get(mode)

    def get_grams(self):
        return self.get('grams')

    def get_ounces(self):
        return self.get('ounces')

    def get_lboz(self):
        return self.get('lboz')

    def get_lb(self):
        return self.get('lb')




    def get(self,units):

        timestamp, raw_weight, data_mode = self.read_value() 

        ounces=0
        grams=0

        g2oz = 0.035274

        if data_mode==self.DATA_MODE_OUNCES:
            ounces = raw_weight * 0.1
            grams = ounces/g2oz
        elif data_mode==self.DATA_MODE_GRAMS:
            grams = raw_weight
            ounces = grams*g2oz
        
        if units=='grams':
            return timestamp,grams

        elif units=='ounces':
            return timestamp,ounces

        elif units=='lboz':
            lb, oz = divmod(ounces, 16)
            return timestamp,lb,oz

        elif units=='lb':
            lb = timestamp,ounces/16.0
            return timestamp,lb


    def echo(self):

        print "Grams:",self.get_grams()
        print "lb:",self.get_lb()
        print "lb/oz:",self.get_lboz()
        print "oz:",self.get_ounces()






