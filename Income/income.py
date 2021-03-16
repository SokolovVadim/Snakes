import matplotlib.pyplot as plt

MONTH_NUM = 12

def calculate_income(monthly_income, monthly_spendings, duration):
	print('Calculations for monthly income =', monthly_income,
	', spendings =', monthly_spendings, ', duration =', duration, "months")

	annual_revenue  = MONTH_NUM * monthly_income
	total_spendings = MONTH_NUM * monthly_spendings
	monthly_savings = monthly_income - monthly_spendings
	total_savings   = MONTH_NUM * monthly_savings

	print('In one year:')
	print('Annual revenue:',  annual_revenue)
	print('Total spendings:', total_spendings)
	print('Total savings:',   total_savings)

	savings_list = list(range(0, duration * monthly_savings, monthly_savings))
	savings_list.append(duration * monthly_savings)
	print(savings_list)
	return savings_list

def plot_savings(savings_list):
	months = list(range(0, len(savings_list)))
	plt.plot(months, savings_list)
	plt.show()

if __name__ == "__main__":
	savings_list = calculate_income(50, 20, 24)
	plot_savings(savings_list)

