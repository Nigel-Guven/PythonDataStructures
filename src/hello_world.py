print('Hello World!')

class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color    
    
cookie_one = Cookie('Green')
cookie_two = Cookie('Blue')

print(cookie_one.color)
print(cookie_two.color)

cookie_two.set_color('yellow')

print(cookie_one.color)
print(cookie_two.color)
