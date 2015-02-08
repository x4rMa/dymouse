import time
import usb.core
import usb.util
 
VENDOR_ID = 0x0922
PRODUCT_ID = 0x8004
DATA_MODE_GRAMS = 2
DATA_MODE_OUNCES = 11
 
# find the USB device
device = usb.core.find(idVendor=VENDOR_ID,
                       idProduct=PRODUCT_ID)
 
try:
    device.detach_kernel_driver(0)
except Exception, e:
    pass

# use the first/default configuration

device.set_configuration()

# first endpoint
endpoint = device[0][(0,0)][0]
 
ea = endpoint.bEndpointAddress
ps = endpoint.wMaxPacketSize
 
# for some damn reason this thing holds onto its old
# value for at least 1 or 2 packets after changing
# so burn a few before you take one
try:
    device.read(ea,ps)
except usb.core.USBError:
    pass

preload = 3
while preload > 0:
    try:
        device.read(endpoint.bEndpointAddress,
                    endpoint.wMaxPacketSize)
    except usb.core.USBError:
        pass
    preload -= 1
 
# read a data packet
attempts = 10
data = None
while data is None and attempts > 0:
    try:
        data = device.read(endpoint.bEndpointAddress,
                           endpoint.wMaxPacketSize)
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            attempts -= 10
            continue
 
raw_weight = data[4] + data[5] * 256
grams=0

if data[2] == DATA_MODE_OUNCES:
    ounces = raw_weight * 0.1
    weight = ounces
elif data[2] == DATA_MODE_GRAMS:
    grams = raw_weight
    weight = grams * .035274
 
#pounds, ounces = divmod(weight, 16)
 
# in a word, jsonp
#print('here_is_the_weight({pounds:'+str(pounds)+',ounces:'+str(round(ounces, 2))+'})')
print "Raw weight:",raw_weight
print "Grams:",grams


