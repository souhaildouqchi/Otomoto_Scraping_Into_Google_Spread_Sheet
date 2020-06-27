import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Compose
from scrapy.shell import inspect_response
import json
import time

class OtomotoItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    url = scrapy.Field()
    number = scrapy.Field()
    features = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()
    mileage = scrapy.Field()
    version = scrapy.Field()
    capacity = scrapy.Field()
    horse_power = scrapy.Field()
    fuel_type = scrapy.Field()
    transmission = scrapy.Field()
    type = scrapy.Field()
    number_of_doors = scrapy.Field()
    color = scrapy.Field()
    first_owner = scrapy.Field()
    origin_country = scrapy.Field()
    no_accidents = scrapy.Field()
    aso = scrapy.Field()
    condition = scrapy.Field()
    VIN_Number = scrapy.Field()
    region = scrapy.Field()
    city = scrapy.Field()


def filter_out_array(x):
    x = x.strip()
    return None if x == '' else x

def remove_spaces(x):
    return x.replace(' ', '')


def convert_to_integer(x):
    return int(x)

class OtomotoCarLoader(ItemLoader):
    default_output_processor = TakeFirst()
    features_out = MapCompose(filter_out_array)
    price_out = Compose(TakeFirst(), remove_spaces, convert_to_integer)
    region_out = Compose(TakeFirst(),remove_spaces)
    city_out =  Compose(TakeFirst(),remove_spaces)



class OtomotoSpider(scrapy.Spider):

    name = 'otomoto'
    start_urls = ['https://www.otomoto.pl/osobowe/uzywane/?search%5Bfilter_float_price%3Ato%5D=200000&search%5Bfilter_float_mileage%3Ato%5D=200000&search%5Border%5D=created_at_first%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=']

    def parse(self, response):

        for car_page in response.css('.offer-title__link::attr(href)'):
            yield response.follow(car_page, self.parse_car_page)

        for next_page in response.css('.next.abs a::attr(href)'):
            yield response.follow(next_page, self.parse)

    def parse_car_page(self, response):

        loader = OtomotoCarLoader(OtomotoItem(), response=response)

        property_list_map = {
            'Marka pojazdu': 'brand',
            'Model pojazdu': 'model',
            'Rok produkcji': 'year',
            'Wersja': 'version',
            'Przebieg': 'mileage',
            'Pojemność skokowa': 'capacity',
            'Moc': 'horse_power',
            'Rodzaj paliwa': 'fuel_type',
            'Skrzynia biegów': 'transmission',
            'Typ': 'type',
            'Liczba drzwi': 'number_of_doors',
            'Kraj pochodzenia': 'origin_country',
            'Kolor': 'color',
            'Pierwszy właściciel': 'first_owner',
            'Bezwypadkowy': 'no_accidents',
            'Serwisowany w ASO': 'aso',
            'Stan': 'condition',
            'VIN':'VIN_Number'
        }

        for params in response.css('.offer-params__item'):

            property_name = params.css('.offer-params__label::text').extract_first().strip()

            if property_name in property_list_map:
                css = params.css('div::text').extract_first().strip()

                if css == '':
                    css = params.css('a::text').extract_first().strip()

                loader.add_value(property_list_map[property_name], css)

        loader.add_css('features', '.offer-features__item::text')
        loader.add_value('url', response.url)
        loader.add_css('price', '.offer-price__number::text')
        loader.add_css('region','.seller-box__seller-address__label::text',re='([^,]+)$')
        loader.add_css('city','.seller-box__seller-address__label::text',re='(.*),[^,]*$')
        loader.add_css('price_currency', '.offer-price__currency::text')
        number_id = self.parse_number(response)
        print('number_id:', len(number_id), '|', number_id)

        for id in number_id:
            phone_url = "https://www.otomoto.pl/ajax/misc/contact/multi_phone/" + id + '/0/'
            # use `meta=` to send data to `photo_parse`
            yield scrapy.Request(phone_url, callback=self.phone_parse, meta={'loader': loader})

    def parse_number(self, response):
        number_id = response.xpath('//a[@data-path="multi_phone"]/@data-id').extract()
        print("NUMBER [before]:", number_id)

        number_id = list(set(number_id))  # you can use `set()` to get unique values
        print("NUMBER [after] :", number_id)

        return number_id

    def phone_parse(self, response):
        print("[phone_parse] response:", response)

        # get data from `parse_car_page`
        loader = response.meta['loader']

        item = response.xpath('//p/text()').extract()
        print('[phone_parse] item:', type(item), item)

        json_data = json.loads(item[0])
        print('[phone_parse] json:', json_data)

        number = json_data["value"].replace(" ","")
        print("'[phone_parse] number:", number) # THERE IT IS AS STRING

        # add new data to loader
        loader.add_value('number', number)

        yield loader.load_item()

# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(OtomotoSpider)
c.start() 
