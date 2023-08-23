*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${add_to_cart_btn}      xpath://*[@id="add-to-cart-button-2"]
${cart_btn}             xpath://*[@id="bar-notification"]/div/p/a

*** Keywords ***
Is Peoduct Page Opened
    Element Should Be Visible    ${add_to_cart_btn}

Click Add To Cart Button
    [Arguments]     ${product_name}
    Click Element       //*[@id=concat('add-to-cart-button-', '${product_name}')]

Click Cart(Product) Button
    Wait Until Element Is Visible       ${cart_btn}
    Click Element       ${cart_btn}