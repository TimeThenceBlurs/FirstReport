# -*- coding: utf-8 -*-
"""
三天打渔两天晒网问题
====================
中国有句古话叫"三天打渔两天晒网"。
某人从 1990 年 1 月 1 日起开始"三天打渔两天晒网"，
即第 1~3 天打渔，第 4~5 天晒网，之后每 5 天循环一次。
输入任意一天，判断这个人在打渔还是在晒网。

解题思路（计算思维：把问题分解为可自动化的步骤）：
1. 计算目标日期距离起始日 1990-01-01 经过了多少天（天数差）
2. 天数差对 5 取余数（周期为 5 天：3 天打渔 + 2 天晒网）
3. 余数为 0、1、2 -> 打渔；余数为 3、4 -> 晒网
"""

from datetime import date

START_DATE = date(1990, 1, 1)   # 起始日期
CYCLE = 5                        # 周期：3 天打渔 + 2 天晒网


def judge(target: date) -> str:
    """判断某一天是打渔还是晒网，返回 '打渔' 或 '晒网'。"""
    days = (target - START_DATE).days   # 距离起始日经过的天数
    remainder = days % CYCLE            # 对周期取余
    if remainder < 3:
        return "打渔"
    else:
        return "晒网"


def main():
    s = input("请输入日期 (格式 YYYY-MM-DD，例如 2026-09-29): ").strip()
    try:
        target = date.fromisoformat(s)
    except ValueError:
        print("日期格式不正确，请使用 YYYY-MM-DD 格式，且不能早于 1990-01-01。")
        return
    if target < START_DATE:
        print("日期不能早于 1990-01-01。")
        return
    print(f"{target} 这天他在 {judge(target)}")


if __name__ == "__main__":
    main()
