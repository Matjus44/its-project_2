Feature: Managment Feature

    Scenario: Opening products page ADMIN 10
    Given Admin is in "dashboard"
    And clicks on "Catalog"
    When clicks on the "Products" tab
    Then list of products should apper

    Scenario: Delete order ADMIN 11
    Given Admin is in "dashboard"
    And clicks on "sales"
    And clicks on "Orders"
    When admin clicks on empty small square of the order and click on "delete"
    Then Order should not appear in order anymore

    Scenario: Creating a new product ADMIN 12
    Given Admin is in "dashboard"
    And clicks on "Catalog"
    And clicks on the "Products" tab
    When Admin clicks on the "Add New" button
    And Fill up necessary information
    And clicks on the "Save" button
    Then The product is created

    Scenario: Update product info ADMIN 13
    Given Admin is in Catalog
    And clicks on the "Products" tab
    When Admin clicks on the "Edit" button next to the product to be updated
    And changes the product details
    And Admin clicks on the "Save" button
    Then The product shows the updated details

    Scenario: Delete product ADMIN 14
    Given Admin is in Catalog
    And clicks on the "Products" tab
    When Admin checks the checkmark next to the product to be deleted
    And clicks on the "Delete" button
    Then The product is deleted

    Scenario: Update availability of product ADMIN 15
    Given Admin is in Catalog
    And clicks on the "Products" tab
    When Admin clicks on the "Edit" buttom of "Apple Cinema 30"
    And changes quantity from 990 to 988
    And admin will click on the "Save" button
    Then The product shows the updated quantity