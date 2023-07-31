*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${login_btn}            xpath://*[contains(text(), 'Log in')][1]
${register_btn}         xpath://*[contains(text(), 'Log in')][1]
${computers_btn}        xpath://*[contains(text(),'Computers')][1]
${cart_btn}             class="cart-label"

*** Keywords ***
Click Home Page Login Button
    Click Element    ${login_btn}

Click Home Page Register Button
    Click Element    ${login_btn}

Click Computers Button
    Click Element    ${computers_btn}

Click Cart Buttn
    Click Element    ${cart_btn}