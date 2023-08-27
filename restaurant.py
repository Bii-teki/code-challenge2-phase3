class  Restaurant:
    def __init__(self,name="Fast Food Restaurant"):
        self.name = name
        
    def rest_name(self):
        return self.name    

    # def set_rest(self, name):
    #     self.name=name
        
    restaurant = property(rest_name) 


restaurant = Restaurant()
print(restaurant.rest_name())     