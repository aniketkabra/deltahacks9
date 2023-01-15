from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
import json

urls = ['https://www.drugs.com/article/prescription-abbreviations.html']

def scrape_text(url):
    print('creating webdriver')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    html = BeautifulSoup(driver.page_source, 'html.parser')
    table_info = html.select('table')
    table_info_pd = pd.read_html(str(table_info[0]))[0]
    print('table dataframe created')
    return table_info_pd

def format_abbr(s):
    s = s.lower()
    s = s.strip(',')
    s = s.replace('.','')
    print('string formatted')
    return s

def create_abbr_table(table_info_pd):
    abbr_str = list(table_info_pd['Abbreviation'].apply(lambda x : str(x)))
    table_info_pd['Abbreviation_str'] = abbr_str
    abbr_formatted = {}
    print('creating dictionary')
    for i in range(len(table_info_pd)):
        abbr = str(table_info_pd['Abbreviation'].iloc[i])
        if len(abbr.split()) >= 2:
            abbr_list = abbr.split()
            for a in abbr_list:
                abbr_formatted[format_abbr(a)] = table_info_pd['Meaning / Intended Meaning'].iloc[i]
        else:
            abbr_formatted[format_abbr(abbr)] = table_info_pd['Meaning / Intended Meaning'].iloc[i]
    print('dictionary created')
    return abbr_formatted

def export_json(abbr_formatted):
    print('exporting json')
    with open("abbr_formatted.json", "w") as outfile:
        json.dump(abbr_formatted, outfile)
    print('json exported')

def main():
    table_info_pd = scrape_text(urls[0])
    abbr_formatted = create_abbr_table(table_info_pd)
    export_json(abbr_formatted)


