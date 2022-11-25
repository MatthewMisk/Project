SalesList = []

Months = 12
CurrentMonth = 0
TotalSales = 0
for CurrentMonth in range(Months):
    Sales = float(input("please enter the sales for month "+str(CurrentMonth)+" "))
    SalesList.append(Sales)
    TotalSales = TotalSales + Sales
    CurrentMonth = CurrentMonth + 1
    
    
def Average(SalesList):
    return sum(SalesList) / len(SalesList)

HighestSales = max(SalesList)
LowestSales = min(SalesList)

print("Total Sales for the month: "+str(TotalSales))
print("HighestSales for the year: "+str(HighestSales))
print("LowestSales for the year: "+str(LowestSales))
print("Average for the year was: "+str(sum(SalesList) / len(SalesList)))
print(SalesList)
