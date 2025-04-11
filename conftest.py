import pytest
import os
from datetime import datetime

import pytest
import os
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and (report.failed or report.passed):
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{screenshots_dir}/{item.name}_{timestamp}.png"
            driver.save_screenshot(filename)

            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(filename))
            else:
                report.extra = [pytest_html.extras.image(filename)]


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

