# TaxCalculator

个税计算器

## 输入

两个参数，分别是全年应税的工资收入(Salary)和年终奖(Bonus)。

## 主要内容

会自动计算以下两种方案下哪种方案最优

方案一：年终奖并入全年工资薪资收入
方案二：按照国家相关政策，年终奖单独计算。此种方案受益于国家政策，延续到2023年底。

## 输出解读

+ 输出表格第一行
+ 从第二行开始，输出结果表示：假设可以将部分年终奖收入(X)调整到工资收入后，纳税方案的比较。即调整后的收入和年终奖分别为 Salary+X 和 Bonus-X
+ 最后一列给出推荐的方案
