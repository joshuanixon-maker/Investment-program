"""
Investment Program
Calculates compound growth of a $1,000 investment at a 7% annual return
using A = P * (1 + r) ** n, displaying the balance at the end of years 1-30.
"""

PRINCIPAL = 1000.00          # P: original amount invested
ANNUAL_RATE = 0.07           # r: annual rate of return (7%)
TOTAL_YEARS = 30             # n: final year to calculate
MILESTONES = (10, 20, 30)    # years to highlight in the summary


def calculate_balance(principal, rate, years):
    """Return the amount on deposit after `years` years: A = P(1 + r)^n."""
    return principal * (1 + rate) ** years


def print_header():
    print("=" * 46)
    print("        INVESTMENT GROWTH CALCULATOR")
    print("=" * 46)
    print(f"  Initial investment : ${PRINCIPAL:,.2f}")
    print(f"  Annual return      : {ANNUAL_RATE * 100:.0f}%")
    print(f"  Time horizon       : {TOTAL_YEARS} years")
    print("=" * 46)


def print_yearly_table():
    print(f"\n{'Year':>6} | {'Balance at End of Year':>24}")
    print("-" * 6 + "-+-" + "-" * 24)
    for year in range(1, TOTAL_YEARS + 1):
        balance = calculate_balance(PRINCIPAL, ANNUAL_RATE, year)
        marker = "  <-- milestone" if year in MILESTONES else ""
        print(f"{year:>6} | {'$' + format(balance, ',.2f'):>24}{marker}")


def print_summary():
    print("\n" + "=" * 46)
    print("  SUMMARY")
    print("=" * 46)
    for year in MILESTONES:
        balance = calculate_balance(PRINCIPAL, ANNUAL_RATE, year)
        gain = balance - PRINCIPAL
        print(f"  After {year:>2} years: ${balance:>10,.2f}   (gain ${gain:,.2f})")
    print("=" * 46)


def main():
    print_header()
    print_yearly_table()
    print_summary()


if __name__ == "__main__":
    main()
