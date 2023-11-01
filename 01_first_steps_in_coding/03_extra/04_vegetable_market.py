N_bgn = float(input())
M_bgn = float(input())
veg_kg = int(input())
fru_kg = int(input())

total_bgn_veg = N_bgn * veg_kg
total_bgn_fru = M_bgn * fru_kg
total_bgn = total_bgn_veg + total_bgn_fru
total_eur = total_bgn / 1.94

print("%.2f" % total_eur)

