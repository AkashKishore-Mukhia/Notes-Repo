# WebDriver

## Driver Sessions

### Creating Sessions

```java
WebDriver driver = new ChromeDriver(chromeOptions);
```

### Quitting Sessions

```java
driver.quit();
```

## Waiting Strategies

Perhaps the most common challenge for browser automation is ensuring that the web application is in a state to execute a particular Selenium command as desired. The processes often end up in a race condition where sometimes the browser gets into the right state first (things work as intended) and sometimes the Selenium code executes first (things do not work as intended). This is one of the primary causes of flaky tests.

All navigation commands wait for a specific readyState value based on the page load strategy (the default value to wait for is "complete") before the driver returns control to the code. The readyState only concerns itself with loading assets defined in the HTML, but loaded JavaScript assets often result in changes to the site, and elements that need to be interacted with may not yet be on the page when the code is ready to execute the next Selenium command.

### Page Load Strategy

The document.readyState property of a document describes the loading state of the current document.

| Strategy | Ready State | Notes |
|----------|-------------|-------|
| normal | complete | Used by default, waits for all resources to download |
| eager | interactive | DOM access is ready, but other resources like images may still be loading |
| none | Any | Does not block WebDriver at all |

**Note:** Similarly, in a lot of single page applications, elements get dynamically added to a page or change visibility based on a click. An element must be both present and displayed on the page in order for Selenium to interact with it.

Selenium provides two different mechanisms for synchronization that are better.

### Implicit Waits

Selenium has a built-in way to automatically wait for elements called an implicit wait. This is a global setting that applies to every element location call for the entire session. The default value is 0, which means that if the element is not found, it will immediately return an error. If an implicit wait is set, the driver will wait for the duration of the provided value before returning the error. Note that as soon as the element is located, the driver will return the element reference and the code will continue executing, so a larger implicit wait value won't necessarily increase the duration of the session.

### Explicit Waits

Explicit waits are loops added to the code that poll the application for a specific condition to evaluate as true before it exits the loop and continues to the next command in the code.

```python
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda _ : revealed.is_displayed())
```
