import statistics
tab = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
grades = list(filter(lambda x: x>2, tab))
print(f"Arithmetic mean for grades <> 2.0 is {round(statistics.mean(grades), 2)}")