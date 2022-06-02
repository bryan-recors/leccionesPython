#estructura = [x for x in range(0,100)]
#print(estructura)

#estructura2 = tuple(x for x in range(0,100))
#print(estructura2)

#estructura2 = tuple(x for x in range(0,100) if x % 2 == 0)
#print(estructura2)

"""
estructura2 = tuple((x for x in range(0,100) 
                        if x % 2 == 0
                        if x < 50
                    ))
print(estructura2)
"""
estructura = tuple(x for x in range(0,100) if x % 2 == 0)

estructura3 = {indice:valor for indice, valor in enumerate(estructura)}

print(estructura3)

