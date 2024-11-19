class Cat:
    age = 1
    eat = 40
    happy = 40
    is_sleeping = False
    name = ''
    
    def set_name(self, name2):
        Cat.name = name2
    
    def set_eat(self, eat):
        Cat.eat += eat
        self.check_stats()
    
    def set_happy(self, happy):
        Cat.happy += happy
        self.check_stats()
    
    def set_sleep(self, sleep):
        Cat.is_sleeping = sleep
    
    def check_stats(self):
        if Cat.eat<0:
            Cat.eat = 0
        elif Cat.eat>100:
            Cat.eat = 100
            self.set_happy(-30)
        if Cat.happy <0:
            Cat.happy = 0
        elif Cat.happy > 100:
            Cat.happy = 100
    
    def get_picture(self):
        if Cat.is_sleeping:
            return ['/static/sleeping.jpg', 'bg-info']
        else:
            if Cat.happy<=20:
                return ['/static/angry.jpg', 'bg-danger']
            elif Cat.happy<=60:
                return ['/static/sad.webp', 'bg-warning']
            else:
                return ['/static/happy.jpg', 'bg-success']
        
        
    
    
        