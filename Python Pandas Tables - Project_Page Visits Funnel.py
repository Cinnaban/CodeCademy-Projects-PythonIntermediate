import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

merged = pd.merge(visits, cart, how='left')
#print(merged.head())
#print(merged.count())
total = merged.visit_time.count()
#print(total)
# Dataframe is 2000 rows long with 348 rows in cart_time

merged_null = merged.visit_time.count() - merged.cart_time.count()
# There are 1652 rows that are null in the Data Frame
#print(merged_null)

Percent_NCart = float(merged_null) / total
#print(str(Percent_NCart*100) + " %")
# There is 82.6 percent of users did not place a t-shirt in their cart

merge_cart = pd.merge(cart, checkout, how='left')
totalc = merge_cart.user_id.count()
checkout_null = merge_cart.cart_time.count() - merge_cart.checkout_time.count() 

Percent_NCheckout = float(checkout_null) / totalc
#print(totalc)
#print(checkout_null)
#print(str(Percent_NCheckout*100) + " %")
# There is 25.3 percent of users who put items in their cart but did not proceed to checkout 

all_data = visits.merge(visits, how='left').merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
#print(all_data.head())

totalch = all_data.checkout_time.count()
purchase_null = all_data.purchase_time.count()
Percent_NPurchase = float(purchase_null) / totalch
#print(str(Percent_NPurchase*100) + " %")
# There is 83.11 percent of users who proceeded to checkout did not purchase a t-shirt

#print(Percent_NCart)
#print(Percent_NCheckout)
#print(Percent_NPurchase)
# The weakest part of the funnel in the process is 83.11 percent of users who proceeded to checkout and did not choose to purchase

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
#print(all_data.time_to_purchase)

print(all_data.time_to_purchase.mean())






