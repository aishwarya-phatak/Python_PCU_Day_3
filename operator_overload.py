#normally adding two int values
number_one = 12
number_two = 13

result_add = number_one + number_two
result_sub = number_one - number_two
result_gt  = number_one > number_two


#operator overload with different operators
class Number:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __gt__(self,other):
        return self.num > other.num
    def __eq__(self, other):
        return self.num == other.num

n1 = Number(112)
n2 = Number(230)

#addition of objects
print(f"adding two objects n1 and n2:{n1 + n2}")
#relational operator overloaded
print(f"checking greater out of two objects:{n1 > n2}")