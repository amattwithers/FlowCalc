#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()

area = float(form["area"].value)
flow = float(form["flow"].value)
bfi = float(form["bfi"].value)
svol = float(form["svol"].value)
rfc = float(form["rfc"].value)
bfc = float(form["bfc"].value)
sfc = float(form["sfc"].value)
rca = float(form["rca"].value)

conc = calc_load(area, flow, bfi, svol, rfc, bfc, sfc, rca)

print "<h1>New Concentration:</h1>"
print cgi.escape(conc)


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
