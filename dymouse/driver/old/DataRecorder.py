from datetime import datetime
import time
from USBScale import DymoUSBScale



class DataRecorder(object):

    def __init__(self,filename='data.csv',plot=True,Nrecords=1000,sleep_time=0.5):

        self.filename = filename
        self.Nrecords = Nrecords
        self.sleep_time = sleep_time
        self.plot = plot
        if self.plot:
            import matplotlib.pylab as plt


    def make_record(self):

        scale = DymoUSBScale()

        data = []
        times = []

        with open(self.filename,'w') as f:
            f.write('')

        if self.plot:
            self.fig = figure()
            self.ax = self.fig.add_subplot(111)


        c = 0

        try:
            while c < self.Nrecords:

                g = scale.get_grams()
                g = str(g)
                data.append(g)

                t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                times.append(t)

                print t+","+g

                with open('data.csv','wa') as f:
                    f.write(t+","+g)



                if self.plot:

                    self.ax.plot(t,data,'bo-')
                    self.ax.set_xlabel('time')
                    self.ax.set_ylabel('mass (g)')
                    plt.show()
                    plt.draw()


                time.sleep(self.sleep_time)
                c += 1

        except KeyboardInterrupt:
            pass

