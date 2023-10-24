import argparse
import openpyxl
import re
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    driver = webdriver.Chrome()
    return driver

def login_and_search(driver, oab_number, oab_state):
    driver.get("https://pje-consulta-publica.tjmg.jus.br")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "fPP:Decoration:numeroOAB")))

    oab_input = driver.find_element(By.ID, "fPP:Decoration:numeroOAB")
    oab_input.send_keys(oab_number)

    state_select = Select(driver.find_element(By.ID, "fPP:Decoration:estadoComboOAB"))
    state_select.select_by_visible_text(oab_state)

    search_button = driver.find_element(By.ID, "fPP:searchProcessos")
    search_button.click()

def get_process_data(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//tbody[@id='fPP:processosTable:tb']//tr")))
    process_links = driver.find_elements(By.XPATH, '//tbody[@id="fPP:processosTable:tb"]//tr[contains(@class, "rich-table-row")]/td[2]/a')
    
    for link in process_links:
        link.click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "_viewRoot:status")))
        driver.switch_to.window(driver.window_handles[-1])
        
        process_id = driver.find_element(By.CSS_SELECTOR, '.rich-stglpanel-body tbody > tr:nth-child(1) td:nth-child(1) .col-sm-12').text
        process_distribution_date = driver.find_element(By.CSS_SELECTOR, '.rich-stglpanel-body tbody > tr:nth-child(1) td:nth-child(2) .col-sm-12').text

        data = {
            "process_id": process_id,
            "process_distribution_date": process_distribution_date,
            "movimentations": []
        }
        
        movimentation_links = driver.find_elements(By.CSS_SELECTOR, 'tbody[id*=":processoEvento:tb"] tr td:nth-child(1)')
        for mv_link in movimentation_links:
            data['movimentations'].append(mv_link.text)

        save_data_to_excel(data)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

def save_data_to_excel(data):
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        
        sheet['A1'] = "Número Processo"
        sheet['B1'] = "Data Distribuição"
        sheet['C1'] = "Movimentações"

        sheet['A2'] = re.sub(r'\D', '', data["process_id"])
        sheet['B2'] = data["process_distribution_date"]
        
        for index, v in enumerate(data["movimentations"]):
            sheet[f"C{index+2}"] = v
        
        workbook.save('dados.xlsx')
        workbook.close()
    except Exception as e:
        handle_exception(e)

def handle_exception(e):
    exception_message = str(e)
    stack_trace = traceback.format_exc()
    print(f"Exception Message: {exception_message}")
    print("Stack Trace:")
    print(stack_trace)

def main(oab_number, oab_state):
    driver = init_driver()

    try:
        login_and_search(driver, oab_number, oab_state)
        get_process_data(driver)

    except Exception as e:
        handle_exception(e)

    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for OAB number on a website")
    parser.add_argument("oab_number", type=str, help="OAB number")
    parser.add_argument("oab_state", type=str, help="OAB state")

    args = parser.parse_args()
    main(args.oab_number, args.oab_state)
