from django.shortcuts import render
from .models import Notebook, Ticker, OrderType
from segment.models import Branch
import sys
from moex.views import Config
from moex.views import MicexAuth
from moex.views import MicexISSClient
from moex.views import MicexISSDataHandler

# Create your views here.
def index(request):
    #scripts = Notebook.objects.order_by('-fieldDate')
    scripts = Notebook.objects.all()
    return render(request, 'journal/journal.html', { 'scripts':scripts,})
    
    



class MyData:
    """ Container that will be used by the handler to store data.
    Kept separately from the handler for scalability purposes: in order
    to differentiate storage and output from the processing.
    """
    def __init__(self):
        self.history = []

    def print_history(self):
        print ("=" * 49)
        print ("|%15s|%15s|%15s|" % ("SECID", "CLOSE", "TRADES"))
        print ("=" * 49)
        for sec in self.history:
            print ("|%15s|%15.2f|%15d|" % (sec[0], sec[1], sec[2]))
        print ("=" * 49)


class MyDataHandler(MicexISSDataHandler):
    """ This handler will be receiving pieces of data from the ISS client.
    """
    def do(self, market_data):
        """ Just as an example we add all the chunks to one list.
        In real application other options should be considered because some
        server replies may be too big to be kept in memory.
        """
        self.data.history = self.data.history + market_data


def main():
    my_config = Config(user='korhall@yandex.ru', password='m1KR0$o4t', proxy_url='')
    my_auth = MicexAuth(my_config)
    if my_auth.is_real_time():
        iss = MicexISSClient(my_config, my_auth, MyDataHandler, MyData)
        iss.get_history_securities('stock',
                                   'shares',
                                   'eqne',
                                   '2010-04-29')
        iss.handler.data.print_history()
        test=iss.get_history_securities('stock',
                                   'shares',
                                   'eqne',
                                   '2010-04-29')
        return render(request, 'main/main.html', { 'test':test[0],})

if __name__ == '__main__':
    try:
        main()
    except:
        print ("Sorry:", sys.exc_type, ":", sys.exc_value)
