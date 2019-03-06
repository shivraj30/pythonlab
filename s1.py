#create function no parameter
def func1():
	print("hii")
	print("hello")
func1()
#with parameter
def func3(a):
	print("hii"+a)
func3("suresh")




def func2(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func2(2,5,6)

def func4(university="IITB"):
	print("I am in"+"\t"+university)
func4("IITG")
func4("IITD")
func4()

def func5(a,b):
	print("hii other function")
	c=a+b
	return c

def func6():
	print("heiio, i am going to call other function")
	s=func5(2,4)
	print("addition is",s)
func6()


bl313@user:~$ python3 s1.py
hiisuresh
2 5 6 13
I am in	IITG
I am in	IITD
I am in	IITB
heiio, i am going to call other function
hiiother function
addition is 6



















