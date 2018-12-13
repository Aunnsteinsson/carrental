from datetime import date

start = "2018-12-10"
end = "2019-1-1"

start = date(start)
end = date(end)
print(start, end)


days_of_rent = date(end) - date(start)
print(days_of_rent)
