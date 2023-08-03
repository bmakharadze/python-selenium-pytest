*** Settings ***
Library         SeleniumLibrary
Resource        pages/HomePage.robot
Resource        pages/RegisterPage.robot
Resource        pages/LoginPage.robot
Resource        pages/ComputersPage.robot
Resource        pages/DesktopsPage.robot
Resource        pages/ProductPage.robot
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

*** Test Cases ***
Login Test
    Launch Browser
    Is Home Page Opened
    Click Home Page Login Button
    Is Login Page Opened
    Input Login Email           becca@gmail.com
    Input Login Password        Test123
    Click Login Button
    Close Browser

Register Test
    Launch Browser
    Is Home Page Opened
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

Order Test
    Launch Browser
    Is Home Page Opened
    Click Computers Button
    Is Computers Page Opened
    Click Desktops Button
    Is Desktop Page Opened
    Click Product Button        Digital Storm VANQUISH 3 Custom Performance PC
    Is Peoduct Page Opened
    Click Add To Cart Button
    Click Cart Button
