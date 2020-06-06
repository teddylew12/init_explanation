
from classes.math import Adder
from classes import Subtracter
from multiply import Multiplyer
adder=Adder()
subt= Subtracter()
mult = Multiplyer()
out = adder.add(2,3)
print(out)
out2 = subt.subtract(out,3)
print(out2)
out3 = mult.multiply(out2,2)
print(out3)