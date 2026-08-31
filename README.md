# bond-tools

A small Python toolkit for fixed income calculations — bond pricing, yield
measures, interest rate risk, and spot rate bootstrapping.

## Why this exists

I built this while working through fixed income theory, translating each
concept into code as I learned it. Every formula here is written directly from
its mathematical definition rather than pulled from a library: no `numpy`, no
`pandas`, no financial packages. The only external dependency is `scipy`, used
for the numerical root-finding that yield-to-maturity requires.

The point was to understand where each formula comes from. Duration is the
first derivative of price with respect to yield; convexity is the second.
Writing them out makes that visible in a way that calling a library function
does not.

## Functions

| Function | What it does |
|---|---|
| `bond_price` | Prices a bond as the present value of its cash flows |
| `calculate_ytm` | Solves for yield to maturity given a market price (numerically, via `brentq`) |
| `current_yield` | Annual coupon divided by market price |
| `macaulay_duration` | Weighted average time to receive the bond's cash flows |
| `modified_duration` | Price sensitivity to a change in yield |
| `convexity` | Second-order correction to the duration estimate |
| `bond_price_spot` | Prices a bond using a term structure of spot rates instead of a single yield |
| `bootstrap_spot_rates` | Derives spot rates from par yields, one maturity at a time |

## Usage

```bash
python examples.py
```

`examples.py` runs every function against a sample bond (1000 face value, 10%
coupon, 3 years, 12% market rate) and prints the results:

```
Price: 951.96
YTM (Yield to Maturity): 12.00%
Current Yield: 10.50%
Macaulay Duration: 2.73
Modified Duration: 2.44
Convexity: 8.42
Spot Rates:
 Year 1: 8.00%
 Year 2: 9.05%
 Year 3: 10.14%
Spot Bond Price: 1000.00
```

Two things in that output are worth pointing out.

The YTM comes back as exactly 12% — the price was calculated at 12%, then the
yield was solved back out of that price, so the forward and inverse functions
agree.

The final line returns exactly the face value. The input `[0.08, 0.09, 0.10]`
is a set of *par* rates: three bonds trading at par. Bootstrapping converts
them into spot rates, and pricing a 3-year 10% bond off those spot rates
returns 1000 — back to par. The round trip closes.

## Notes

- Annual coupons only; semiannual payments are not handled.
- Cumulative return over a window is approximated as the sum of periodic
  returns rather than compounded — the difference is negligible at these
  magnitudes.
- `bootstrap_spot_rates` assumes the input bonds trade at par.

## Next

Forward rates, the relationship between spot and forward curves, and credit
spreads.