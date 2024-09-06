"""
Description
An order management system for a restaurant is being developed. Implement the OrderSystem class and the IOrderSystem interface as described.

The IOrder interface contains the methods that the Order class should implement.

Add the following properties to the class:
name (String)
price (int)
 

Create a new class called OrderSystem and implement the IOrderSystem interface.

Implement the following methods:
addToCart(IOrder order): add the order item to the cart
removeFromCart(IOrder order): remove the order item from the cart

calculateTotalAmount(): calculate the discounted prices for each order in the cart and sum the values

categoryDiscounts(): Calculate discounts for each product category in the cart. First, group the products in the basket according to category, then sum the discounted prices for each group. The discounted price calculation is shown as Discounted Price = Order Price - ((Order Price * Discount Rate) % 100). The method returns a map of categories name and the discount amount. (key = category, value = category discount)

cartItems(): This method retrieves the list of items in the cart along with their quantities. It groups the products by their names and counts the number of products ordered for each group. The method returns this map of names of items in the cart and their quantities. (key = name, value = item count)

 
Category determination is done as follows:

Order Price <= 10: Cheap
Order Price <= 20 and OrderPrice > 10: Moderate
Order Price > 20 and OrderPrice > 20: Expensive
The discount per category is as follows:

Cheap  = 10%
Moderate = 20%
Expensive = 30%
 

Example

There are 2 Order objects, with name, price:

Television 40

Computer 30

 

After they are added, calculate the total amount from orders.

e.g. The Price for Television = 40 and 40 > 20, so the discount equals 30%. The discounted price = 40 - ((40*30)/100) = 28. Similarly, the 30% discounted price of Computer is 21.

 

Output:

Total Amount: 49

Expensive Category Discount: 49

Television (1 items)

Computer (1 items)

 

Input Format For Custom Testing
Sample Case 1
Sample Input For Custom Testing

STDIN        Function
-----        --------
9            number of orders n = 9
Order-1 49   first order: name = 'Order-1', price = 49
Order-2 31   second order...
Order-3 74
Order-4 21
Order-5 64
Order-6 94
Order-7 23
Order-8 23
Order-9 71
Sample Output

Total Amount: 319
Expensive Category Discount: 131
Order-1 (1 items)
Order-2 (1 items)
Order-3 (1 items)
Order-4 (1 items)
Order-5 (1 items)
Order-6 (1 items)
Order-7 (1 items)
Order-8 (1 items)
Order-9 (1 items)
Explanation

9 orders are added and grouped by price category. All items are in the 'Expensive' category, so only 1 group of items is reported. Data is read, method calls are made, and results are printed by the provided stub.

Sample Case 2
Java 15
1192021222324252627
IOException {
Line: 27 Col: 64

Input / Output

Test Cases
Input
9
Order-1 49
Order-2 31
Order-3 74
Order-4 21
Order-5 64
Order-6 94
Order-7 23
Order-8 23
Order-9 71
Run Code to see your output here.
"""

"""
import java.io.*;
import java.util.*;

interface IOrder {
    void setName(String name);
    String getName();
    void setPrice(int price);
    int getPrice();
}

interface IOrderSystem {
    void addToCart(IOrder order);
    void removeFromCart(IOrder order);
    int calculateTotalAmount();
    Map<String, Integer> categoryDiscounts();
    Map<String, Integer> cartItems();
}

class Order implements IOrder {
    private String name;
    private int price;

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public int getPrice() {
        return this.price;
    }
}

class OrderSystem implements IOrderSystem {
    private List<IOrder> cart = new ArrayList<>();

    @Override
    public void addToCart(IOrder order) {
        cart.add(order);
    }

    @Override
    public void removeFromCart(IOrder order) {
        cart.remove(order);
    }

    @Override
    public int calculateTotalAmount() {
        int totalAmount = 0;
        for (IOrder order : cart) {
            int price = order.getPrice();
            int discountRate = getDiscountRate(price);
            int discountedPrice = price - (price * discountRate / 100);
            totalAmount += discountedPrice;
        }
        return totalAmount;
    }

    @Override
    public Map<String, Integer> categoryDiscounts() {
        Map<String, Integer> discounts = new HashMap<>();
        int cheapDiscount = 0, moderateDiscount = 0, expensiveDiscount = 0;

        for (IOrder order : cart) {
            int price = order.getPrice();
            int discountRate = getDiscountRate(price);
            int discount = (price * discountRate / 100);
            if (price <= 10) {
                cheapDiscount += discount;
            } else if (price <= 20) {
                moderateDiscount += discount;
            } else {
                expensiveDiscount += discount;
            }
        }

        if (cheapDiscount > 0) {
            discounts.put("Cheap", cheapDiscount);
        }
        if (moderateDiscount > 0) {
            discounts.put("Moderate", moderateDiscount);
        }
        if (expensiveDiscount > 0) {
            discounts.put("Expensive", expensiveDiscount);
        }

        return discounts;
    }

    @Override
    public Map<String, Integer> cartItems() {
        Map<String, Integer> items = new HashMap<>();
        for (IOrder order : cart) {
            String name = order.getName();
            items.put(name, items.getOrDefault(name, 0) + 1);
        }
        return items;
    }

    private int getDiscountRate(int price) {
        if (price <= 10) {
            return 10;
        } else if (price <= 20) {
            return 20;
        } else {
            return 30;
        }
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter textWriter = new PrintWriter(System.out);

        IOrderSystem orderSystem = new OrderSystem();
        int oCount = Integer.parseInt(br.readLine().trim());
        for (int i = 1; i <= oCount; i++) {
            String[] a = br.readLine().trim().split(" ");
            IOrder e = new Order();
            e.setName(a[0]);
            e.setPrice(Integer.parseInt(a[1]));
            orderSystem.addToCart(e);
        }
        int totalAmount = orderSystem.calculateTotalAmount();
        textWriter.println("Total Amount: " + totalAmount);

        Map<String, Integer> categoryDiscounts = orderSystem.categoryDiscounts();
        for (Map.Entry<String, Integer> entry : categoryDiscounts.entrySet()) {
            if(entry.getValue() > 0) {
                textWriter.println(entry.getKey() + " Category Discount: " + entry.getValue());
            }
        }

        Map<String, Integer> cartItems = orderSystem.cartItems();
        for (Map.Entry<String, Integer> entry : cartItems.entrySet()) {
            textWriter.println(entry.getKey() + " (" + entry.getValue() + " items)");
        }

        textWriter.flush();
        textWriter.close();
    }
}

"""