# import the required library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
 
# initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome()

# open in maximized mode
driver.maximize_window()

start_page = 0

facultad = "Facultad de Ingeniería en Electricidad y Computación"
codigo_facultad = "123456789"

carrera = "Ingeniería en Ciencias Computacionales"
codigo_carrera = "54824"
# carrera = "Computación"
# codigo_carrera = "50525"
# carrera = "Telemática"
# codigo_carrera = "50529"
# carrera = "Telecomunicaciones"
# codigo_carrera = "50528"
# carrera = "Ingeniería Eléctrica"
# codigo_carrera = "50526"
# carrera = "Licenciatura en Sistemas de Información"
# codigo_carrera = "54782"
# carrera = "Tesis de Licenciatura en Redes y Sistemas Operativos"
# codigo_carrera = "54441"
# carrera = "Tesis de Electrónica y Automatización"
# codigo_carrera = "50527"




data = {'NOMBREPROYEC': [], 'FECHA': [], 'URL': [], 'CARRERA': [], 'FACULTAD': []}

while True:
    url_page = "https://www.dspace.espol.edu.ec/handle/" + codigo_facultad + "/" + codigo_carrera + "?offset=" + str(start_page)
    # visit your target site
    driver.get(url_page)

    # find the element with the class name 'btn btn-primary'
    elements = driver.find_elements(By.XPATH, '//td[@headers="t2"]//a')
    print(f"Number of elements found: {len(elements)}")

    # limit the number of elements to 10
    number_max = driver.find_element(By.XPATH, '//div[@class="browse_range"]').text
    number_max = int(number_max.split()[-1])  # extract the number from the text
    print(f"Number of elements in the range: {number_max}")


    time.sleep(3)  # wait for the page to load
    # open in another tab
    for element in elements:
        # get the href attribute of the element
        href = element.get_attribute('href')
        print(f"Opening link: {href}")

        # open the link in a new tab
        driver.execute_script("window.open(arguments[0], '_blank');", href)

        # switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(2)  # wait for the page to load

        title = driver.find_element(By.XPATH, '//tbody//td[@class="metadataFieldValue dc_title"]').text
        data['NOMBREPROYEC'].append(title)
        fecha = driver.find_element(By.XPATH, '//tbody//td[@class="metadataFieldValue dc_date_issued"]').text
        data['FECHA'].append(fecha)
        url = driver.find_element(By.XPATH, '//tbody//td[@class="metadataFieldValue dc_identifier_uri"]').text
        data['URL'].append(url)
        data['CARRERA'].append(carrera)
        data['FACULTAD'].append(facultad)

        time.sleep(2) # wait

        # close the current tab
        driver.close()
        # switch back to the original tab
        driver.switch_to.window(driver.window_handles[0])

    start_page += 20  # increment the page offset
    if start_page > number_max or start_page == 60:
        break

df = pd.DataFrame.from_dict(data)
df.to_csv('scrap_dspace/results/dspace_data_' + "_".join(carrera.split()) + '.csv', index=False)

# wait for the page to load completely
time.sleep(2)

# release the resources allocated by Selenium and shut down the browser
driver.quit()