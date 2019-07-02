from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    dest1=destination()
    dest1.name="Delhi"
    dest1.price=600
    dest1.desc="city of love and power"

    dest2=destination()
    dest2.name="Mumbai"
    dest2.price=400
    dest2.desc="city which never sleeps"

    dest3=destination()
    dest3.name="Banglore"
    dest3.price=605
    dest3.desc="silicon valley"




    return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3})