import bond_tools

face_value = 1000
coupon_rate = 0.10
market_rate = 0.12
years = 3
par_rates = [0.08, 0.09, 0.10]


price = bond_tools.bond_price(face_value, coupon_rate, market_rate, years)
print(f"Price: {price:.2f}")

ytm = bond_tools.calculate_ytm(face_value, coupon_rate, years, price)
print(f"YTM (Yield to Maturity): {ytm:.2%}")

current_yield = bond_tools.current_yield(face_value, coupon_rate, price)
print(f"Current Yield: {current_yield:.2%}")

mac_dur = bond_tools.macaulay_duration(
    face_value, coupon_rate, market_rate, years)
print(f"Macaulay Duration: {mac_dur:.2f}")

mod_dur = bond_tools.modified_duration(
    face_value, coupon_rate, market_rate, years)
print(f"Modified Duration: {mod_dur:.2f}")

conv = bond_tools.convexity(face_value, coupon_rate, market_rate, years)
print(f"Convexity: {conv:.2f}")

spots = bond_tools.bootstrap_spot_rates(par_rates)
print("Spot Rates:")
for year, spot in enumerate(spots, start=1):
    print(f" Year {year}: {spot:.2%}")

spot_price = bond_tools.bond_price_spot(face_value, coupon_rate, spots)
print(f"Spot Bond Price: {spot_price:.2f}")
