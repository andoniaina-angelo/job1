
def draw_rectangle(Width,height):
    
    print("|","-"*Width,"|")
    i=0
    while i!= height-2:
        print("|"," "*Width,"|")
        i+=1
    print( "|","-"*Width,"|")


draw_rectangle(10,3) 
