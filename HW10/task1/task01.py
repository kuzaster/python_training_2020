import json
from itertools import tee

import requests
from bs4 import BeautifulSoup

MAIN_URL = "https://markets.businessinsider.com"
URL_SP500 = "https://markets.businessinsider.com/index/components/s&p_500"


def get_dollar_rate():
    req = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?")
    usa = BeautifulSoup(req.content, "lxml").find("valute", id="R01235").value.string
    return float(usa.replace(",", "."))


def get_soup_parser(url):
    return BeautifulSoup(requests.get(url).content, "lxml")


def generate_main_table_blocks(main_soap):
    pages_block = main_soap.find("div", attrs={"class": "finando_paging"})
    pages_urls = (f'{URL_SP500}{a["href"]}' for a in pages_block.find_all("a"))
    soups = (get_soup_parser(url) for url in pages_urls)
    table_blocks = (
        soup.find("table", attrs={"class": "table table-small"}) for soup in soups
    )
    return tuple(table_blocks)


def get_company_urls(blocks_table):
    for block in blocks_table:
        yield from (f'{MAIN_URL}{tag_a["href"]}' for tag_a in block.find_all("a"))


def get_company_names_and_tickers(blocks_table):
    company_urls = get_company_urls(blocks_table)
    soups = (get_soup_parser(url) for url in company_urls)

    idents_block = (
        company.find("h1", attrs={"class": "price-section__identifiers"})
        for company in soups
    )
    block_1, block_2 = tee(idents_block, 2)
    names = (idents.span.string.strip() for idents in block_1)
    tickers = (idents.find_all("span")[2].string[2:] for idents in block_2)
    return zip(names, tickers)


def get_1_year_indexes(blocks_table):
    for block in blocks_table:
        yield from (
            comp.find_all("td")[9].text.split()[1] for comp in block.find_all("tr")[1:]
        )


def get_prices_rub(blocks_table):
    company_urls = get_company_urls(blocks_table)
    soups = (get_soup_parser(url) for url in company_urls)
    us_rate = get_dollar_rate()

    price_block = (
        company.find("div", attrs={"class": "price-section__values"})
        for company in soups
    )
    prices = (
        round(float(block.span.string.replace(",", "")) * us_rate, 2)
        for block in price_block
    )
    return prices


def get_10_the_most_grown_companies(blocks_table):
    comp_names = get_company_names_and_tickers(blocks_table)
    indexes_1_year = get_1_year_indexes(blocks_table)
    d = zip(comp_names, indexes_1_year)
    # bad way:
    # result = ({"name": k[0][0], 'ticker': k[0][1], 'growth': k[1]}
    #       for k in sorted(d, key=lambda k: float(k[1].strip('\%')), reverse=True)[:10])
    # return result


def get_the_most_expensive_companies(blocks_table):
    comp_names = get_company_names_and_tickers(blocks_table)
    comp_prices = get_prices_rub(blocks_table)
    z = zip(comp_names, comp_prices)
    # bad way:
    # sorted_prices = sorted(zip(comp_names, comp_prices), key=lambda k: k[1], reverse=True)[:10]
    # result = ({"name": k[0][0], 'ticker': k[0][1], 'price': k[1]} for k in sorted_prices)
    # return result


MAIN_SOUP = get_soup_parser(URL_SP500)
table_block = MAIN_SOUP.find("table", attrs={"class": "table table-small"})
ALL_TABLE_BLOCKS = generate_main_table_blocks(MAIN_SOUP)  # tuple


# json_1 = get_10_the_most_grown_companies(ALL_TABLE_BLOCKS)
# with open("grown.json", "w") as f:
#     json.dump(tuple(json_1), f)
# json_2 = get_the_most_expensive_companies(ALL_TABLE_BLOCKS)
# with open("expensive.json", "w") as f:
#     json.dump(tuple(json_2), f)
