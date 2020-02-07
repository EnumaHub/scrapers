import scrapy
from ..items import *

import datetime

fecha_hoy = datetime.datetime.now()

class disco2(scrapy.Spider):
    name = "disco2"
    page_variable = 2
    start_urls = ['https://www.disco.com.uy/frescos/carniceria/carnes-rojas?PageNumber=1']
    

    def parse(self, response):

        items = Disco2Item()

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        
        items.setdefault('precios', [])
        #for producto in productos:
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()
        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/carniceria/carnes-rojas?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/pescaderia?PageNumber=1",
                          callback=self.parse_pescaderia)

    def parse_pescaderia(self, response):
        items = Pescaderia()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/pescaderia?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_pescaderia, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/carniceria/chacinados?PageNumber=1",
                          callback=self.parse_chacinados)


    def parse_chacinados(self, response):
        items = Chacinados()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/carniceria/chacinados?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_chacinados, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request('https://www.disco.com.uy/frescos/carniceria/pollo?PageNumber=1',
                          callback=self.parse_pollo)


    def parse_pollo(self, response):
        items = Pollo()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/carniceria/pollo?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_pollo, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/fiambres/fiambres?PageNumber=1",
                          callback=self.parse_fiambres)

    def parse_fiambres(self, response):
        items = Fiambres()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/fiambres/fiambres?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_fiambres, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/frutas-y-verduras?PageNumber=1",
                          callback=self.parse_frutas_y_verduras)

    def parse_frutas_y_verduras(self, response):
        items = FrutasYVerduras()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/frutas-y-verduras?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_frutas_y_verduras, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/quesos?PageNumber=1",
                          callback=self.parse_quesos, dont_filter=True)

    def parse_quesos(self, response):
        items = Queso()


        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()


        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/quesos?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_quesos, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/lacteos?PageNumber=1", 
                          callback=self.parse_lacteos, dont_filter=True)

    def parse_lacteos(self, response):
        items = Lacteos()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/lacteos?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_lacteos, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/congelados?PageNumber=1",
                          callback=self.parse_congelados, dont_filter=True)

    def parse_congelados(self, response):
        items = Congelados()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/congelados?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_congelados, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/frescos/pastas?PageNumber=1",
                          callback=self.parse_pastas, dont_filter=True)


    def parse_pastas(self, response):
        items = Pastas()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/frescos/pastas?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_pastas, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/almacen/canasta-familiar?PageNumber=1",
                          callback=self.parse_canasta, dont_filter=True)


    def parse_canasta(self, response):
        items = Canasta()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/almacen/canasta-familiar?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_canasta, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/perfumeria-y-limpieza/perfumeria?PageNumber=1",
                          callback=self.parse_perfumeria, dont_filter=True)


    def parse_perfumeria(self, response):
        items = Perfumeria()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/perfumeria-y-limpieza/perfumeria?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_perfumeria, dont_filter=True)
        else:
            disco2.page_variable = 2
            yield scrapy.Request("https://www.disco.com.uy/mascotas?PageNumber=1",
                          callback=self.parse_mascotas, dont_filter=True)

    def parse_mascotas(self, response):
        items = Mascotas()
        

        proximo = response.selector.xpath('//*[@id="paginador"]/ul/li[8]/text()').extract()

        #for producto in productos:
        items.setdefault('precios', [])
        
        nombres = response.selector.xpath('//h3[@class="Product-title"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="Product-prices"]/span/text()').extract()
        tipos = response.selector.xpath('//div[@class="Product-brand"]/text()').extract()
        imagenes = response.selector.xpath('//a[@class="Product-image"]//img/@src').extract()
        sitio = response.selector.xpath('//li[@class="titulo-lista"]/text()').extract()

        n = 0
        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            items['sitio'] = sitio[2]
            yield items

        next_page = 'https://www.disco.com.uy/mascotas?PageNumber=' + str(disco2.page_variable)
        disco2.page_variable += 1

        if len(proximo) != 0:
            yield response.follow(next_page, callback=self.parse_mascotas, dont_filter=False)
        #else:
        #   return scrapy.Request("https://www.disco.com.uy/perfumeria-y-limpieza/perfumeria?PageNumber=1",
        #                  callback=self.parse_pescaderia)