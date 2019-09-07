# Use your newfound knowledge of loops to discover trends
# in the operation of the newest hair salon in town, Carly’s Clippers.
# 利用你对循环的新知识，来发现城里最新的美发沙龙卡莉理发器的经营趋势。

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
total_revenue = 0

for pri in prices:
    total_price += pri
average_price = total_price / len(prices)
print(f"The average price is: {average_price}")

new_prices = [(np - 5) for np in prices]
print(new_prices)

for i in range(len(hairstyles)):
    total_revenue += prices[1] * last_week[i]
print(f"Total Revenue:{total_revenue}")
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[cuts] for cuts in range(len(hairstyles)-1) if new_prices[cuts] < 30]
print(cuts_under_30)


