*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Click Product Button
    [Arguments]     ${product_name}
    Click Element    xpath://*[contains(text(), '${product_name}')][1]
