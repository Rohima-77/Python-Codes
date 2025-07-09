# {}
# key value pair
# not indexing
# Key is immutable

a = {'Turi' : 1,'Ruyi' : 3,5:[1,2,3],8:[6,7,8]}
print(type(a))

for i in a:
    print(i) # ekhane sudhu key gula print hoise
    
    for i in a.values():
        print(i) #ekhane sudhu value gula print hbe
        
        print(a.keys(),a.values())
        
        for k,v in a.items():
            print(f"keys: {k},values{v}")
            
        a = [1,2,3]
        b = ['c++','python','Java']
        print(dict(zip(a,b)))
