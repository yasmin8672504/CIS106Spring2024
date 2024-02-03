# Problem #3
def compute_postage(weight, zip_code, postage, area_charge, weight_charge):
    if zip_code == 60171:
        area_charge[0] = 2.00
    elif zip_code == 60172:
        area_charge[0] = 2.50
    elif zip_code == 60635:
        area_charge[0] = 3.00
    else:
        area_charge[0] = 5.00
    
    if weight > 100:
        weight_charge[0] = 0.02 * weight
    elif weight > 50:
        weight_charge[0] = 0.03 * weight
    else:
        weight_charge[0] = 0.05 * weight 
    
    
    postage[0] = area_charge[0] + weight_charge[0]
    
    return area_charge[0], weight_charge[0], postage[0]

weight = float(input("Enter the weight of the package in ounces: "))
zip_code = int(input("Enter the zip code: "))
postage = [0]  
area_charge = [0]  
weight_charge = [0] 

area_charge_value, weight_charge_value, postage_value = compute_postage(weight, zip_code, postage, area_charge, weight_charge)

print("Area charge: $", area_charge_value)
print("Weight charge: $", weight_charge_value)
print("Postage: $", postage_value)
