###################################################
# Python Code to Calculate Flow stuff
#
#
#
#
###################################################


def calc_load(area, flow, bfi, svol, rfc, bfc, sfc, rca):

    # Check input is correct
    if (bfi > 1.0):
        print("Error")
        return False

    # Calculate flows
    bflow = bfi * flow  # Base flow
    rflow = (1.0 - bfi) * flow  # Runoff flow

    bvol = area * bflow * 1.0e4  # Base Flow Volume
    rvol = (rca/100) * area * rflow * 1.0e4  # Runoff Flow Volume

    bload = bvol * bfc * 1.0e-6  # Base Load/kg
    sload = svol * sfc * 1.0e-6  # Source Load/kg
    rload = rvol * rfc * 1.0e-6  # Runoff Load/kg

    tot_load = bload + sload + rload
    tot_flow = bvol + rvol + svol
    new_conc = (tot_load * 1.0e6) / tot_flow

    return new_conc


if __name__ == '__main__':

    area = float(input("\nEnter Catchment area/ha: "))
    flow = float(input("Total flow in mm: "))
    bfi = float(input("Base Flow Index: "))
    svol = float(input("Source Volume/L: "))
    rfc = float(input("Runoff flow conc mg L^-1: "))
    bfc = float(input("Base flow conc mg L^-1: "))
    sfc = float(input("Source flow conc mg L^-1: "))
    rca = float(input("Percentage of catchment contributing to runoff: "))

    print("\nRunning... Calculating New Concentration...")

    conc = calc_load(area, flow, bfi, svol, rfc, bfc, sfc, rca)

    print("\nNew Concentration = %1.4f mg/L\n" % conc)
