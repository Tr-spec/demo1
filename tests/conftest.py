import pytest
from selenium import webdriver
import time
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

## this fixture will execute every time when we are using BaseClass
@pytest.fixture(scope="class") ## scope ="class" means this fixture can be used on class not on method          ## Fixture scope can be class or method
def setup(request):
    global driver
    ## below line is working as input
    browser_name=request.config.getoption("browser_name")   #pytest --browser_name "firefox"
     # parameter which can be passed with pytest command
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    elif browser_name == "safari":
        print("Safari driver")
    else:
        driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    ## cls => class => fixture attached class or a class which is using this fixture For now BaseClass
    ## adding attribute driver to BaseClass and assing value of driver we created here
    request.cls.driver = driver         ## request => to class which is using fixture
    yield
    time.sleep(10)
    driver.close()



# This hook is used to take automatically screenshot and place in HTML report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    global driver
    driver = driver.Chrome()
    driver.get_screenshot_as_file(name)

