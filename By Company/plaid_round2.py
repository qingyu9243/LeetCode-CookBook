"""
customer check out cart using coupon.

coupon = { 'category': 'fruit',
   'percent_discount': 15,
   'amount_discount': None,
   'minimum_num_items_required': 2,
   'minimum_amount_required': 10.00
  }

cart = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
 ] 
lma@plaid.com 
"""
from collections import defaultdict
def applyCoupon(coupon_single, cart):
    # build a category to total price map
    dict_category_to_total_price = defaultdict(list) # {category: [count, total_price]}
    for cart_item in cart:
        p = cart_item['price']
        cate_ = cart_item['category']

        #for price, category in cart_item.items():
        if cate_ not in dict_category_to_total_price:
            dict_category_to_total_price[cate_] = [1, int(p)]
        else:
            dict_category_to_total_price[cate_][0] += 1 # count
            dict_category_to_total_price[cate_][1] += int(p) # total_price

    # check coupon, raise error when coupon doesn't work
    coupon_num_satisfied = False
    coupon_amount_satisfied = False
    applied_coupon = False
    if coupon_single['category'] in dict_category_to_total_price:
        if coupon_single['minimum_num_items_required']:
            cnt = dict_category_to_total_price[coupon_single['category']][0]
            if cnt >= coupon_single['minimum_num_items_required']:
                coupon_num_satisfied = True
    
    if coupon_single['category'] in dict_category_to_total_price:
        if coupon_single['minimum_amount_required']:
            amt = dict_category_to_total_price[coupon_single['category']][1]
            if amt >= coupon_single['minimum_amount_required']:
                coupon_amount_satisfied = True    

    total_price_in_cart = 0

    if coupon_single['minimum_num_items_required'] and coupon_single['minimum_amount_required'] and coupon_num_satisfied and coupon_amount_satisfied:
        category_ = coupon_single['category']
        if coupon_single['percent_discount']:
            percent = coupon_single['percent_discount']
            price_adjusted = dict_category_to_total_price[category_][1] * (100 - percent)/100
            applied_coupon = True
            total_price_in_cart += price_adjusted

        if coupon_single['amount_discount']:
            amt_reduce = coupon_single['amount_discount']
            amt_adjusted = dict_category_to_total_price[category_][1] - amt_reduce
            applied_coupon = True
            total_price_in_cart += amt_adjusted

    #print(dict_category_to_total_price)
    for cate, cnt_and_totalprice in dict_category_to_total_price.items():
        if cate != coupon_single['category']:
            #print(cnt_and_totalprice, cate)
            total_price_in_cart += cnt_and_totalprice[1]

    #print(coupon_num_satisfied, coupon_amount_satisfied, applied_coupon)
    if not applied_coupon:
        total_price_in_cart += dict_category_to_total_price[coupon_single['category']][1]

    # return total price in cart
    return total_price_in_cart

c = { 'category': 'fruit',
   'percent_discount': 15,
   'amount_discount': None,
   'minimum_num_items_required': 2,
   'minimum_amount_required': 10.00
  }
cart = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
 ] 
print(applyCoupon(c, cart)) # 33.5

c_2 = { 'category': 'clothing',
   'percent_discount': 15,
   'amount_discount': None,
   'minimum_num_items_required': 1,
   'minimum_amount_required': 10.00
  }
cart_2 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
 ] 
print(applyCoupon(c_2, cart_2)) # 35

c_3 = { 'category': 'clothing',
   'percent_discount': None,
   'amount_discount': 4,
   'minimum_num_items_required': 1,
   'minimum_amount_required': 10.00
  }
cart_3 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 15.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
 ] 
print(applyCoupon(c_3, cart_3)) # 2+20+8+15-4 = 41

c_4 = { 'category': 'toy',
   'percent_discount': None,
   'amount_discount': 4,
   'minimum_num_items_required': 3,
   'minimum_amount_required': 5.00
  }
cart_4 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 15.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
 ] 
print(applyCoupon(c_4, cart_4)) # 2+20+8+15 = 45