class Product_info:
    def __init__(self,name,code):
        self.name = name
        self.code = code

A = Product_info("codetree","50")

n , c = tuple(input().split())
B = Product_info(n, c)

print(f"product {A.code} is {A.name}")
print(f"product {B.code} is {B.name}")