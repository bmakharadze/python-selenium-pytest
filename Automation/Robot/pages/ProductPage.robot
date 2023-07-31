*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${add_to_cart_btn}      id="add-to-cart-button-2"

*** Keywords ***
Click Add To Cart Button
    Click Element    ${add_to_cart_btn}