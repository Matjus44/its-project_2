# Report of project 2 from subject ITS

**Name and surname:** Matúš Janek

**Login:** 237464

## Summary

This report contains information about scenarios that have been modified.

## Modified scenarios

### Scenario: Search for product and add category USER 3 

Added one step of clicking on searchbar

### Scenario: Search for product and add wrong category USER 4 

Added one step of clicking on searchbar

### Scenario: Add product to the shoppning cart from result page USER 6

**Change of given step:**

`Given User is in "result page"` -> `Given User is in "home page"`

**Specifiing product that will be added into cart in when step:**

 `When User clicks on "add to cart"` -> `When User adds Samsung Galaxy Tab 10.1 to the cart`

### Scenario: Buy product USER 7 

**Added multiple given steps:**

`And User clicks on "Laptot & notebooks"`

`And clicks on "Show all laptops & notebooks"`

`And clicks on "HP LP3065"`

`And adds product into cart`

`And opens shopping cart`

`And clicks on "checkout"`

**Spliting when step into multiple ones:**

`When User fills in all adress details`

`And delivery` 

`And payment`

**Change of then step:**

`Then Checkout should be processed and order should appear in "Order history"` -> `Then Order should be processed`

**And deletion of these steps:**

`And clicks on "shopping cart" where is already product`

### Scenario: create an order ADMIN 8

Not implemented, I could not make the test work.

### Scenario: Search for product ADMIN 9

**Change of given step:**

`Given Log in as admin` -> `Given Admin is in "dashboard"`

`And click on "catalog"` -> `And clicks on "Catalog"`

`And "Products"` -> `And clicks on the "Products" tab`

### Scenario: Opening products page ADMIN 10

**Change of when step:**

`When admin clicks on "products"` -> `When clicks on the "Products" tab`

### Scenario: Delete order ADMIN 11

**Deletion of given step:**

`And click on the order`

**Change of when step:**

`When admin clicks on empty small square and click on "delete"` -> `When admin clicks on empty small square of the order and click on "delete"`

### Scenario: Creating a new product ADMIN 12

**Change of given steps:**

`Given Admin is in Catalog` -> `Given Admin is in "dashboard"`

`And clicks on the "Products" tab` -> `And clicks on "Catalog"`

**Added given step:**

`And clicks on the "Products" tab`








