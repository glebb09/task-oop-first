from Vehicle import Vehicle

car1 = Vehicle('VW', 417, 'red', 2010, 'Germany', 4, True)
car2 = Vehicle('Renault', 220, 'green', 1958, 'China', 2, False)



print(car1.engine_status)
car1.start_engine()
print(car1.engine_status)
print(car1.headlights_status)
car1.switch_on_headlights("далфывыф")
print(car1.headlights_status)

