temps = [221, 234, -999, 340, 230]

# new_temps = [temp / 10 for temp in temps if temp != -999]
# print(new_temps)


# List with If-else conditional
new_temps = [temp / 10 if temp != -999 else 0 for temp in temps]
print(new_temps)

