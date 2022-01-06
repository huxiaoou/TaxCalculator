import sys
import numpy as np
import pandas as pd

pd.set_option("display.width", 0)
pd.set_option("display.max_rows", None)


def lookup_rate_and_quick_minus(t_x: float) -> (float, float):
    if t_x < 36000:
        return 0.03, 0
    elif t_x < 144000:
        return 0.10, 2520
    elif t_x < 300000:
        return 0.20, 16920
    elif t_x < 420000:
        return 0.25, 31920
    elif t_x < 660000:
        return 0.30, 52920
    elif t_x < 960000:
        return 0.35, 85920
    else:
        return 0.45, 181920


def sol_0(t_annual_salary: float, t_annual_bonus: float):
    _s = t_annual_salary + t_annual_bonus
    _r, _d = lookup_rate_and_quick_minus(t_x=_s)
    _res = _s * _r - _d
    print("=" * 60)
    print("方案一：年终奖并入全年收入")
    print("应税收入:       {:>12.2f}".format(_s))
    print("对应税率:       {:>12.2f}".format(_r))
    print("对应速算扣除数:  {:>12.2f}".format(_d))
    print("总应纳税额:      {:>12.2f}".format(_res))
    return _res


def sol_1(t_annual_salary: float, t_annual_bonus: float):
    _r0, _d0 = lookup_rate_and_quick_minus(t_x=t_annual_salary)
    _r1, _d1 = lookup_rate_and_quick_minus(t_x=t_annual_bonus)
    _t0 = t_annual_salary * _r0 - _d0
    _t1 = t_annual_bonus * _r1 - _d1 / 12
    _res = _t0 + _t1
    print("=" * 60)
    print("方案二：年终奖单独计税")
    print("-" * 60)
    print("应税工资:       {:>12.2f}".format(t_annual_salary))
    print("对应税率:       {:>12.2f}".format(_r0))
    print("对应速算扣除数:  {:>12.2f}".format(_d0))
    print("应纳税额:       {:>12.2f}".format(_t0))
    print("-" * 60)
    print("应税奖金:       {:>12.2f}".format(t_annual_bonus))
    print("对应税率:       {:>12.2f}".format(_r1))
    print("对应速算扣除数:  {:>12.2f}".format(_d1))
    print("应纳税额:       {:>12.2f}".format(_t1))
    print("-" * 60)
    print("总应纳税额:     {:>12.2f}".format(_res))
    return _res


def sol_2(t_annual_salary: float, t_annual_bonus: float):
    _s = t_annual_salary + t_annual_bonus
    _r, _d = lookup_rate_and_quick_minus(t_x=_s)
    _res_a = _s * _r - _d
    _r0, _d0 = lookup_rate_and_quick_minus(t_x=t_annual_salary)
    _r1, _d1 = lookup_rate_and_quick_minus(t_x=t_annual_bonus)
    _t0 = t_annual_salary * _r0 - _d0
    _t1 = t_annual_bonus * _r1 - _d1 / 12
    _res_b = _t0 + _t1
    return {
        "SumIncome": _s,
        "Salary": t_annual_salary,
        "Bonus": t_annual_bonus,
        "R": _r,
        "D": _d,
        "Tax1": _res_a,
        "R0": _r0,
        "D0": _d0,
        "R1": _r0,
        "D1": _d0,
        "Tax2a": _t0,
        "Tax2b": _t1,
        "Tax2": _res_b,
        "Diff": _res_a - _res_b,
        "Opt": "并入计算" if _res_a < _res_b else "单独计算"
    }


if __name__ == "__main__":
    annual_salary = float(sys.argv[1])
    annual_bonus = float(sys.argv[2])

    # print("=" * 60)
    # print("应税年工资:{:>12.2f}".format(annual_salary))
    # print("应税年终奖:{:>12.2f}".format(annual_bonus))
    # tax_sol_0 = sol_0(annual_salary, annual_bonus)
    # tax_sol_1 = sol_1(annual_salary, annual_bonus)
    # print("=" * 60)
    # if tax_sol_0 < tax_sol_1:
    #     print("方案一优于方案二，建议采用方案一：年终奖并入全年收入")
    # elif tax_sol_0 > tax_sol_1:
    #     print("方案二优于方案一，建议采用方案二：年终奖单独计算")
    # else:
    #     print("两种方案没有明显差别，可随意选择")
    # print("=" * 60)

    d = 1000
    res = []
    for transfer in np.arange(0, annual_bonus, d):
        res.append(sol_2(annual_salary + transfer, annual_bonus - transfer))
    print(pd.DataFrame(res))
