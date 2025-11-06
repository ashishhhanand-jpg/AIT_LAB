facts = [
    "john_is_cold.",           
    "raining.",                
    "john_Forgot_His_Raincoat.",  
    "fred_lost_his_car_keys.", 
    "peter_footballer."        
]


def verify_fact(fact):
    fact = fact.rstrip(".")
    # Perform some logic to verify the fact
    if fact == "john_Forgot_His_Raincoat":
        return True
    elif fact == "raining":
        return True
    elif fact == "foggy":
        return True
    elif fact == "Cloudy":
        return False  # Assume it's not cloudy
    else:
        return False

# Verify each fact
for fact in facts:
    if verify_fact(fact):
        print(f"{fact} - Yes")
    else:
        print(f"{fact} - No")
      
