# pyviztest
## A Visual Testing Library in Python. Works with Playwright and Selenium. Can be integrated with Allure Report.
[![Project PyVizTest](https://github.com/sanosuke009/pyviztest/actions/workflows/python-app.yml/badge.svg)](https://github.com/sanosuke009/pyviztest/actions/workflows/python-app.yml)

## Goal Of Project pyviztest

### Forewords
[Kumar Aaditya](https://github.com/kumaraditya303) created a [pytest fixture](https://pypi.org/project/pytest-playwright-snapshot/) for [Playwright](https://playwright.dev/python/) using the power of [pixelmatch library](https://pypi.org/project/pixelmatch/) for Visual Testing, and [Symon Storozhenko](https://github.com/symon-storozhenko) enhanced it to create [pytest-playwright-visual](https://pypi.org/project/pytest-playwright-visual/). I really loved both, so I tried to realign the same concept by developing a library and added a few more functionality to make the use of it more flexible, and also compatible with [Playwright](https://playwright.dev/python/) and [Selenium](https://www.selenium.dev/). All thanks go to both of them for being the harbinger of the visual testing libraries in python. I merely followed the path and improvized.

### Features
#### So, previously created [pytest-playwright-visual](https://pypi.org/project/pytest-playwright-visual/) had the power to be summoned anywhere inside the tests which had it as a parameter, and to
1. Create Golden Snapshot (The reference image of the UI which needs to be compared with during test execution) of the AUT(Applicayion under test).
2. Update existing Golden Snapshot.
3. Take snapshot in runtime and compare it with the Golden Snapshot. If both do not match, it creates an image where the difference is highlighted.

#### In addition to these features, pyviztest is capable of doing a few more things!
4. Supports Windows, Linux and MacOS systems.
5. Supports Playwright and Selenium. You just need to provide the Page and WebDriver instances.
6. Supports custom snapshot directories.
7. Supports option to Create & Update snapshots(particular and all) without failing the tests.
8. Supports option to add multiple snapshot validation in a single test case, and if one of them fails it will still validate others.
9. Supports integration with Allure Report.
10. Supports auto-naming of the snapshots with respect to the test suite and test case name.
11. Provides api to return Golden, Actual and Difference Snapshots in bytes, to easily integrate with any custom report.
12. Supports comparing images with different in sizes without failing the test abruptly.
13. Supports comparing snapshots of multiple web elements together or the full page.

### Upcoming Next:
1. Support for Appium.
2. Support for element specific identification.
3. A fixture along with the usual library.

## How To Use

### Installation Guide

### Example Code
#### Playwright:

#### Selenium:

### Best Practices

## Troubleshooting

