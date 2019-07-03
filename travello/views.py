from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    dest1=destination()
    dest1.name="Delhi"
    dest1.price=600
    dest1.img='destination_1.jpg'
    dest1.desc="city of love and power"
    dest1.offer=False

    dest2=destination()
    dest2.name="Mumbai"
    dest2.price=400
    dest2.img='destination_2.jpg'
    dest2.desc="city which never sleeps"
    dest2.offer=True

    dest3=destination()
    dest3.name="Banglore"
    dest3.price=605
    dest3.img='destination_3.jpg'
    dest3.desc="silicon valley"
    dest3.offer=False

    dests=[dest1,dest2,dest3]




    return render(request,'index.html',{'dest':dests})