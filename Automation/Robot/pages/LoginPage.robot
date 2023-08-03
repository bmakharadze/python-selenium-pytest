*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${email_input}      xpath://*[@id="Email"]
${password_input}   xpath://*[@id="Password"]
${login_btn}        xpath://*[contains(text(), 'Log in')][1]

*** Keywords ***
Is Login Page Opened
    Element Should Be Visible    ${email_input}

Input Login Email
    [Arguments]     ${email}
    Input Text      ${email_input}    ${email}

Input Login Password
    [Arguments]     ${password}
    Input Text      ${password_input}    ${password}

Click Login Button
    Click Element    ${login_btn}
