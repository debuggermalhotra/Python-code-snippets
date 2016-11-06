class employee:
	#common baseclass for all emplyees
	empcount=0
	
	def __init__(self,name,salary,id_no):
		self.name=name;
		self.salary=salary
		self.id_no=id_no
		
		employee.empcount += 1
	
	
	def displaycount(self):
		print "Total emplyee d" % employee.empcount
		
	def displayempolyee(self):
		print "Name: ",self.name, ", Salary: ",self.salary, ", Id number: ",self.id_no	
		
#creating first object of employee class:

emp1=employee("farhan",2344,3455)

#creating first object of employee class:
emp2=employee("Rajesh",5600,1234)

#accessing  attributs:

emp1.displayempolyee()
emp2.displayempolyee()
print("\nTotal employee :%d"% employee.empcount) 
