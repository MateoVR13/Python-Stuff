#lists store mutiple items in a single variable

jobs = ["Manager","Salesman","Receptionist","Warehouse","Security Guard"]

# print(jobs[1])

# jobs[1] = "Security Guard"

jobs.append("President")
jobs.remove("Warehouse")
jobs.pop()
jobs.insert(0,"Officer")
jobs.sort()
jobs.clear()

for x in jobs:
    print(x)
