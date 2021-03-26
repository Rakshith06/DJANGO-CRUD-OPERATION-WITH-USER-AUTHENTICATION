import  os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authproject.settings')
django.setup()
from faker import Faker
from myapp.models import Employee
f=Faker()
def populate(n):
    for i in range(n):
        fno=f.random_int(min=1,max=20)
        fname=f.name()
        fsal=f.random_int(min=10000,max=100000)
        fadd=f.address()
        e=Employee.objects.get_or_create(eno=fno,ename=fname,esal=fsal,eadd=fadd)
populate(20)
