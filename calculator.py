 
import cowsay


# ----- PHYSICAL CONSTANTS OF MATERIALS -------------
prop_mat = [
    {"NAME": "STEEL A36  ", "E": 207, "Ys": 250, "G": 79.3},
    {"NAME": "AISI 304L  ", "E": 193, "Ys": 172, "G": 81.0},
    {"NAME": "DUPLEX 2205", "E": 200, "Ys": 460, "G": None}
]

# ----- LENGTH CONVERTER ----------------------------
def length_conv():
    print("UNITS:")
    print("METERS -------> (M)")
    print("KILOMETERS ---> (KM)")
    print("MILES --------> (MI)")
    print("----------------------------------")
    val = float(input("VALUE TO CONVERT: "))
    unit1 = input("INITIAL UNIT: ")
    unit2 = input("FINAL UNIT: ")
    unit1u = unit1.upper()
    unit2u = unit2.upper()
    print("----------------------------------")

    conv_to_meters = {"M": 1, "KM": 1000, "MI": 1609.34}

    if unit1u not in conv_to_meters or unit2u not in conv_to_meters:
        print("Invalid unit")
    else:

        val_in_meters = val * conv_to_meters[unit1u]
        converted_val = round((val_in_meters / conv_to_meters[unit2u]), 2)

        print(f"RESULT: {converted_val} {unit2u}")

# ----- PRESSURE CONVERTER -------------------------
def pressure_converter():
    print("UNITS:")
    print("PSI - BAR - KSI")
    print("----------------------------------")
    val = float(input("VALUE TO CONVERT: "))
    unit1 = input("INITIAL UNIT: ")
    unit2 = input("FINAL UNIT: ")
    unit1u = unit1.upper()
    unit2u = unit2.upper()
    print("----------------------------------")

    conv_to_psi = {"PSI": 1, "BAR": 14.5038, "KSI": 1000}

    if unit1u not in conv_to_psi or unit2u not in conv_to_psi:
        print("Invalid unit")
    else:
        val_in_psi = val * conv_to_psi[unit1u]
        converted_val = round((val_in_psi / conv_to_psi[unit2u]), 2)

        print(f"RESULT: {converted_val} {unit2u}")


# ----- POWER UNIT CONVERTER -------------

def power_converter():
    print("UNITS:")
    print("HP - KW")
    print("----------------------------------")
    val = float(input("VALUE TO CONVERT: "))
    unit1 = input("INITIAL UNIT: ")
    unit2 = input("FINAL UNIT: ")
    unit1u = unit1.upper()
    unit2u = unit2.upper()
    print("----------------------------------")

    conv_to_hp = {"HP": 1, "KW": 1.34102}

    if unit1u not in conv_to_hp or unit2u not in conv_to_hp:
        print("Invalid unit")
    else:
        val_in_hp = val * conv_to_hp[unit1u]
        converted_val = round((val_in_hp / conv_to_hp[unit2u]), 2)

        print(f"RESULT: {converted_val} {unit2u}")


# ----- PRESSURE CALCULATION  -------------------


def distributed_force():
    num1 = float(input("FORCE (N): "))
    num2 = float(input("AREA (mm2): "))
    res = round((num1 / num2), 2)
    print(" ")
    print("RESULT:", res, "MPa")
    return res

# ----- PHYSICAL PROPERTIES OF MATERIALS ----------------


def tabla_mat():
    print("PHYSICAL PROPERTY OF MATERIALS")
    print(" ")
    print("E  = modulus of elasticity (GPa)")
    print("Ys = yield strength (MPa)")
    print("G  = modulus of rigidity (GPa)")
    print(" ")
    print("MATERIAL       E      Ys     G")
    for mat in prop_mat:
        print(mat["NAME"], mat["E"], mat["Ys"], mat["G"], sep=" -- ")


# ------- MAIN MENU ----------------------------------------

print(" ")
print("UNIT CONVERTER\n1) PRESSURE 2) POWER 3) LENGTH")
print("CALCULATIONS")
print("4) DISTRIBUTED FORCE (N/mm2 = MPa) ")
print("INFORMATION")
print("5) PROPERTY OF MATERIALS")
print(" ")
print("99) FINISH PROGRAM ")
print("-----------------------------------")

# ----- OPERATION SELECTOR -----------------------------


sel = int(input("SELECT AN OPTION: "))

while sel != 99:

    if sel == 1:
        print("-----------------------------------")
        pressure_converter()
        print("-----------------------------------")
        sel = int(input("ANOTHER OPTION? "))
    elif sel == 2:
        print("-----------------------------------")
        power_converter()
        print("-----------------------------------")
    elif sel == 3:
        print("-----------------------------------")
        length_conv()
        print("-----------------------------------")
    elif sel == 4:
        print("-----------------------------------")
        distributed_force()
        print("-----------------------------------")
    elif sel == 5:
        print("-----------------------------------")
        tabla_mat()
        print("-----------------------------------")
        sel = int(input("ANOTHER OPTION? "))
    else:
        print(" ")
        print("ERROR")
else:
    print("-----------------------------------")
    print(cowsay.com("GOODBYE"))
    print("-----------------------------------")
