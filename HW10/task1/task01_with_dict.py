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


def get_1_year_indexes(block_table):
    yield from (
        comp.find_all("td")[9].text.split()[1]
        for comp in block_table.find_all("tr")[1:]
    )


def generate_main_table_blocks(main_soap):
    pages_block = main_soap.find("div", attrs={"class": "finando_paging"})
    pages_urls = (f'{URL_SP500}{a["href"]}' for a in pages_block.find_all("a"))
    soups = (get_soup_parser(url) for url in pages_urls)
    table_blocks = (
        soup.find("table", attrs={"class": "table table-small"}) for soup in soups
    )
    return tuple(table_blocks)


def get_company_urls(block_table):
    yield from (f'{MAIN_URL}{tag_a["href"]}' for tag_a in block_table.find_all("a"))


def get_company_names_and_tickers(url):
    soups = get_soup_parser(url)

    idents_block = soups.find("h1", attrs={"class": "price-section__identifiers"})
    names = idents_block.span.string.strip()
    tickers = idents_block.find_all("span")[2].string[2:]
    return names, tickers


def get_prices_rub(url):
    soups = get_soup_parser(url)
    us_rate = get_dollar_rate()

    price_block = soups.find("div", attrs={"class": "price-section__values"})
    price = round(float(price_block.span.string.replace(",", "")) * us_rate, 2)
    return price


MAIN_SOUP = get_soup_parser(URL_SP500)
table_block = MAIN_SOUP.find("table", attrs={"class": "table table-small"})
ALL_TABLE_BLOCKS = generate_main_table_blocks(MAIN_SOUP)  # tuple
dict_result = {}
for table in ALL_TABLE_BLOCKS:
    one_year_indexes = get_1_year_indexes(table)
    for url in get_company_urls(table):
        name, ticker = get_company_names_and_tickers(url)
        price = get_prices_rub(url)
        one_year_index = next(one_year_indexes)
        dict_result[name] = (ticker, price, one_year_index)
    break

# some sorted actions with dict_result...
