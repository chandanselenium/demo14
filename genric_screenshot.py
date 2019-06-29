import time

def takeScreenshot(driver):
    file_name = str(round(time.time() * 10)) + '.png'
    file_path = "E:\\actitime1\\screenshot\\"
    path = file_path + file_name
    driver.save_screenshot(path)
