class cars:
    company= 'TATA'
    
    def start(self):
        print("welcome")
        
    def details(self):
        print(self.model)
        print(self.price)
        print(self.color)
car1= cars()
car2= cars()

car1.model = "xyz"
car1.price = 1500000
car1.color = 'white'

car2.model = "zyx"
car2.price = 1250000
car2.color = 'gray' 

car1.start() 
car1.details()

print("\n", end="")

car2.start() 
car2.details()