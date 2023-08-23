*** Settings ***
Library         SeleniumLibrary
Resource        pages/HomePage.robot
Resource        pages/RegisterPage.robot
Resource        pages/LoginPage.robot
Resource        pages/ComputersPage.robot
Resource        pages/DesktopsPage.robot
Resource        pages/ProductPage.robot
Resource    pages/CheckoutPage.robot
Variables       enums/DateOfBirthDay.py
Variables       enums/DateOfBirthMonth.py
Variables       enums/DateOfBirthYear.py

*** Variables ***
${BROWSER}        Chrome
${URL}            https://demo.nopcommerce.com/
${CHROME_BINARY}  /Users/bekamakharadze/documents/selenium/chromedriver.exe

*** Keywords ***
Launch Browser
    Open Browser        ${URL}    ${BROWSER}    executable_path=${CHROME_BINARY}
    Maximize Browser Window
    Is Home Page Opened

*** Test Cases ***
Login Test
    Launch Browser
    Click Home Page Login Button
    Is Login Page Opened
    Input Login Email           becca@gmail.com
    Input Login Password        Test123
    Click Login Button
    Close Browser

Register Test
    Launch Browser
    Click Home Page Register Button
    Is Register Page Opened
    Click Male Gender
    Input First Name            Becca
    Input Last Name             Mak
    Select Date Of Birth Day        ${FIRST}
    Select Date Of Birth Month      ${JANUARY}
    Select Date Of Birth Year       ${YEAR_2001}
    Input Register Email        becca@gmail.com
    Select Newsletter Checkbox

Add To Cart Test
    Launch Browser
    Click Computers Button
    Is Computers Page Opened
    Click Desktops Button
    Is Desktop Page Opened
    Click Product Button                Digital Storm VANQUISH 3 Custom Performance PC
    Is Peoduct Page Opened
    Click Add To Cart Button            2

Order Test
    Launch Browser
    Click Prodiuct from Home Page       HTC One M8 Android L 5.0 Lollipop
    Is Peoduct Page Opened
    Click Add To Cart Button            18
    Click Home Page Button
    Click Prodiuct from Home Page       Apple MacBook Pro 13-inch
    Is Peoduct Page Opened
    Click Add To Cart Button            4
    Click Cart Button
    Click Agree To TOS Button
    Click Checkout Button
