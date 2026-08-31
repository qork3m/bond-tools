import scipy.optimize


def bond_price(face_value, coupon_rate, market_rate, years):
    result = 0
    for year in range(1, years + 1):
        if year != years:
            result += (face_value*coupon_rate) / (1 + market_rate) ** year
        else:
            result += ((face_value*coupon_rate) + face_value) / \
                (1 + market_rate) ** year
    return result


def calculate_ytm(face_value, coupon_rate, years, market_price):
    def inner_function(r):
        return bond_price(face_value, coupon_rate, r, years) - market_price
    return scipy.optimize.brentq(inner_function, 0.0001, 1.0)


def current_yield(face_value, coupon_rate, market_price):
    return (face_value * coupon_rate) / market_price


def macaulay_duration(face_value, coupon_rate, market_rate, years):
    result = 0
    for year in range(1, years + 1):
        if year != years:
            pv = (face_value * coupon_rate) / ((1 + market_rate) ** year)
        else:
            pv = ((face_value * coupon_rate) + face_value) / \
                ((1 + market_rate) ** year)
        result += pv * year
    return result / bond_price(face_value, coupon_rate, market_rate, years)


def modified_duration(face_value, coupon_rate, market_rate, years):
    return macaulay_duration(face_value, coupon_rate, market_rate, years) / (1 + market_rate)


def convexity(face_value, coupon_rate, market_rate, years):
    result = 0
    for year in range(1, years + 1):
        if year != years:
            pv = (face_value * coupon_rate) / ((1 + market_rate) ** (year + 2))
        else:
            pv = ((face_value * coupon_rate) + face_value) / \
                ((1 + market_rate) ** (year + 2))
        result += pv * year * (year + 1)
    return result / bond_price(face_value, coupon_rate, market_rate, years)


def bond_price_spot(face_value, coupon_rate, spot_rates):
    result = 0
    for year, market_rate in enumerate(spot_rates, start=1):
        if year != len(spot_rates):
            result += (face_value*coupon_rate) / ((1 + market_rate) ** year)
        else:
            result += ((face_value*coupon_rate) + face_value) / \
                ((1 + market_rate) ** year)
    return result


def bootstrap_spot_rates(par_rates, face_value=1000):
    spot_rates = []
    for year, par_rate in enumerate(par_rates, start=1):
        coupon = (face_value * par_rate)
        pv_of_coupons = 0
        for y, spot_rate in enumerate(spot_rates, start=1):
            pv_of_coupons += coupon / ((1 + spot_rate) ** y)
        remaining = face_value - pv_of_coupons
        final_payment = coupon + face_value
        spot = (final_payment / remaining) ** (1 / year) - 1
        spot_rates.append(spot)
    return spot_rates
