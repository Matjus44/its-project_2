Feature: search and buy

    Scenario: Search for product USER 1
    Given User is in "home page"
    And clicks on "searchbar"
    When user writes iMAC and press enter
    Then iMac should be seen

    Scenario: Search for non existing product USER 2 
    Given User is in "home page"
    And clicks on "searchbar"
    When user writes traktor and presses enter
    Then No results should be shown

    Scenario: Search for product and add category USER 3 
    Given User is in "home page"
    And clicks on "searchbar"
    And user writes iMAC and press enter
    And iMac should be seen
    When user selects "category" to Mac
    Then iMac should be seen
    
    Scenario: Search for product and add wrong category USER 4 
    Given User is in "home page"
    And clicks on "searchbar"
    And user writes iMAC and press enter
    And iMac should be seen
    When user selects "category" to WebCameras
    Then No result should be shown

    Scenario: Display product page USER 5 
    Given User is in "home page"
    When User clicks on some product
    Then The products page should be seen

    Scenario: Add product to the shoppning cart from result page USER 6
    Given User is in "home page"
    When User adds Samsung Galaxy Tab 10.1 to the cart
    Then Product should appear in shopping cart

    Scenario: Buy product USER 7 
    Given User is in "home page"
    And User clicks on "Laptot & notebooks"
    And clicks on "Show all laptops & notebooks"
    And clicks on "HP LP3065"
    And adds product into cart
    And opens shopping cart
    And clicks on "checkout"
    When User fills in all adress details 
    And delivery 
    And payment
    And clicks on "Confirm Order"
    Then Order should be processed

    # Scenario: create an order ADMIN 8
    # Given I am at the "order page"
    # And I click "add order"
    # And I fill in necessary data
    # When I click "confirm order"
    # Then The order will be added

    Scenario: Search for product ADMIN 9
    Given Admin is in "dashboard"
    And clicks on "Catalog" 
    And clicks on the "Products" tab
    When admin puts into filter iMAC
    Then admin should see the product.

    
