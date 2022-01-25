# Variabelen lengte en gewicht invulmogelijkheid
height = float(input("Jouw lengte in cm: "))
weight = float(input("Jouw gewicht in kg: "))

# Formule BMI
BMI = weight / (height/100)**2

print(f"Jouw BMI is {BMI}")

# Pietje
if BMI <= 18.4:
    print("Je hebt ondergewicht.")
elif BMI <= 24.9:
    print("Je hebt een gezond gewicht.")
elif BMI <= 29.9:
    print("Je hebt licht overgewicht.")
elif BMI <= 34.9:
    print("Je hebt zwaar overgewicht.")
elif BMI <= 39.9:
    print("Je bent obees.")
else:
    print("Maak een afspraak met een dokter!.")
