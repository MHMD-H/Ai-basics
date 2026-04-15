import statistics as stats

data = [1, 2, 3, 4, 5,5,8]
print(stats.mean(data))   # المتوسط 4
print(stats.median(data)) # الوسيط 4
print(stats.mode(data))   # المنوال 5
print(stats.stdev(data))  #  2.3 الانحراف المعياري
print(stats.variance(data))#5.333 التباين