# Ask the user for inputs
prior_arrests = int(input("Prior arrests: ") )
local_ordinance = input("Prior arrests for local orginance (Y/N): ") 
age = int(input("Age at release: ") )

## start with the number of prior arrests
risk_score = prior_arrests

# subtract 1 if no prior arrests for a local ordinance
if local_ordinance.upper() == "N":
    risk_score -= 1

# subtract 1 if age at release is greater than 40
if age > 40:
    risk_score -= 1

## result reslute
print(f'The recidivism risk score is {risk_score}')
