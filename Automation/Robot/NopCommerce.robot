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

*** Test Cases ***
Login Test
    Open Browser        ${URL}    ${BROWSER}    executable_path=${CHROME_BINARY}
    Maximize Browser Window
    Click Home Page Login Button
    Input Login Email           becca@gmail.com
    Input Login Password        Test123
    Click Login Button
    Close Browser

Register Test
    Open Browser        ${URL}    ${BROWSER}    executable_path=${CHROME_BINARY}
    Click Home Page Register Button
    Click Male Gender
    Input First Name            Becca
    Input Last Name             Mak
    Select Date Of Birth Day        ${FIRST}
    Select Date Of Birth Month      ${JANUARY}
    Select Date Of Birth Year       ${YEAR_2001}
    Input Register Email        becca@gmail.com
    Select Newsletter Checkbox

Order Test
    Open Browser        ${URL}    ${BROWSER}    executable_path=${CHROME_BINARY}
    Maximize Browser Window
    Click Computers Button
    Click Desktops Button
    Click Product Button        Digital Storm VANQUISH 3 Custom Performance PC
    Click Add To Cart Button
    Click Cart Buttn
