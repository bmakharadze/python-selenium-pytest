*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}          Chrome
${url}              http://www.newtours.demoaut.com/
${chrome_binary}    /Users/bekamakharadze/documents/selenium/chromedriver.exe

*** Test Cases ***
Mouse Actions Test
    Open Browser                http://swisnl.github.io/jQuery-contextMenu/demo.html
    Maximize Browser Window
    Open Context Menu           xpath://span[@class='context-menu-one btn btn-neutral']
    Go To                       https://testautomationpractice.blogspot.com/ maximize browser window
    Double Click Element        xpath://button[contains(text (), 'Copy Text')]

User Defined Keywords Test
    ${PageTitle}=       launchBrowser     ${url}      ${browser}     ${chrome_binary}
    Log To Console      ${PageTitle}
    Log                 ${PageTitle}
    Input Text          name:userName   mercury
    Input Text          name:password   mercury

Scrolling Test
    Open Browser        https://www.countries-ofthe-world.com/flags-of-the-world.html      ${browser}     executable_path=${chrome_binary}
    Maximize Browser Window
    Execute Javascript      window.scrollTo(0, 2500)
    Scroll Element Into View    xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img

Test Alert Handling
    Open Browser        https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert      ${browser}     executable_path=${chrome_binary}
    Maximize Browser Window
    Click Button        xpath=//button[text()="Try it"]
    Handle Alert        accept
    Page Should Contain    You pressed OK!

Handling Alerts
    Open Browser        https://testautomationpractice.blogspot.com/       ${browser}     executable_path=${chrome_binary}
    Click Element       //*[@id="HTML9"]/div[1]/button[1]
    Handle Alert        accept

Alert And Frame Test
    Open Browser        https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert       ${browser}     executable_path=${chrome_binary}
    Select Frame        //*[@id="iframeResult"]
    Click Button        xpath=//button[text()="Try it"]
    Handle Alert        accept
    Capture Page Screenshot

*** Keywords ***
launchBrowser
    [Arguments]         ${appurl}   ${appbrowser}   ${executable_path}
    Open Browser        ${appurl}   ${appbrowser}   executable_path=${executable_path}
    Maximize Browser Window
    ${title}=           Get Title
    [Return]            ${title}
