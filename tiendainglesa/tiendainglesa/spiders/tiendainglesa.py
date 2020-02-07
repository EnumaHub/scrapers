import scrapy
from ..items import *

import datetime

fecha_hoy = datetime.datetime.now()

class tiendainglesa(scrapy.Spider):
    name= "tiendainglesa"
    page_variable = 1
    start_urls = ["https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Carnes-Vacunas/1894/173/busqueda?0,0,*:*,1894,173,176,,%5B%5D,false,%5B%5D,%5B%5D,0"]

    def parse(self, response):
        items = TiendainglesaItem()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()
        

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]            
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Carnes-Vacunas/1894/173/busqueda?0,0,*:*,1894,173,176,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Pescados---Mariscos/1894/173/179/busqueda?0,0,*:*,1894,173,179,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_pescaderia, dont_filter=True)



    def parse_pescaderia(self, response):
        items = Pescaderia()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Pescados---Mariscos/1894/173/179/busqueda?0,0,*:*,1894,173,179,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_pescaderia)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Embutidos/1894/173/busqueda?0,0,*:*,1894,173,178,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_chacinados, dont_filter=True)

    def parse_chacinados(self, response):
        items = Chacinados()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Embutidos/1894/173/busqueda?0,0,*:*,1894,173,178,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_chacinados, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Aves/1894/173/busqueda?0,0,*:*,1894,173,175,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_pollo, dont_filter=True)

    def parse_pollo(self, response):
        items = Pollo()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Carnes/Aves/1894/173/busqueda?0,0,*:*,1894,173,175,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_pollo)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Fiambres/1894/busqueda?0,0,*:*,1894,231,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_fiambres, dont_filter=True)

    def parse_fiambres(self, response):
        items = Fiambres()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Fiambres/1894/busqueda?0,0,*:*,1894,231,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_fiambres, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Frutas/1894/busqueda?0,0,*:*,1894,195,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_frutas, dont_filter=True)

    def parse_frutas(self, response):
        items = Frutas()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Frutas/1894/busqueda?0,0,*:*,1894,195,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_frutas, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Verduras/1894/busqueda?0,0,*:*,1894,196,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_verduras, dont_filter=True)

    def parse_verduras(self, response):
        items = Verduras()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Verduras/1894/busqueda?0,0,*:*,1894,196,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_verduras, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Frescos/Quesos/1894/busqueda?0,0,*:*,1894,237,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_quesos, dont_filter=True)

    def parse_quesos(self, response):
        items = Quesos()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Quesos/1894/busqueda?0,0,*:*,1894,237,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_quesos, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request('https://www.tiendainglesa.com.uy/Categoria/Frescos/L%C3%A1cteos/1894/busqueda?0,0,*:*,1894,209,0,,%5B%5D,false,%5B%5D,%5B%5D,0',
                          callback=self.parse_lacteos, dont_filter=True)

    def parse_lacteos(self, response):
        items = Lacteos()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Frescos/L%C3%A1cteos/1894/busqueda?0,0,*:*,1894,209,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_lacteos, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Congelados/busqueda?0,0,*:*,181,0,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_congelados, dont_filter=True)

    def parse_congelados(self, response):
        items = Congelados()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Congelados/busqueda?0,0,*:*,181,0,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_congelados, dont_filter=True)
        else:
            tiendainglesa.page_variable = 2
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Almac%C3%A9n/busqueda?0,0,*:*,78,0,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_canasta, dont_filter=True)

    def parse_canasta(self, response):
        items = Canasta()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Almac%C3%A9n/busqueda?0,0,*:*,78,0,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_canasta, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Limpieza/busqueda?0,0,*:*,1895,0,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_limpieza, dont_filter=True)

    def parse_limpieza(self, response):
        items = Limpieza()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Limpieza/busqueda?0,0,*:*,1895,0,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_limpieza, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Perfumer%C3%ADa/busqueda?0,0,*:*,569,0,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_perfumeria, dont_filter=True)

    def parse_perfumeria(self, response):
        items = Perfumeria()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Perfumer%C3%ADa/busqueda?0,0,*:*,569,0,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_perfumeria, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Beb%C3%A9s/Pa%C3%B1ales/529/busqueda?0,0,*:*,529,612,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_paniales, dont_filter=True)

    def parse_paniales(self, response):
        items = Paniales()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Beb%C3%A9s/Pa%C3%B1ales/529/busqueda?0,0,*:*,529,612,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_paniales, dont_filter=True)
        else:
            tiendainglesa.page_variable = 1
            yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Hogar-y-Tiempo-Libre/Mascotas/1005/busqueda?0,0,*:*,1005,503,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
                          callback=self.parse_mascotas, dont_filter=True)

    def parse_mascotas(self, response):
        items = Mascotas()

        items.setdefault('precios', [])

        proximo = response.selector.css('#W0078TEXTBLOCK12 a::text').extract_first()

        nombres = response.selector.xpath('//span[@class="wCartProductName"]/a/text()').extract()
        precios = response.selector.xpath('//div[@class="ProductPrice MarginR25"]/text()').extract()
        imagenes = response.selector.css('.ImageProductComponent::attr(src)').extract()

        cant = len(nombres)
        for n in range(cant):
            items['precios'].clear()
            items['nombre'] = nombres[n]
            items.setdefault('precios', []).append({'precio': precios[n], 'fecha': fecha_hoy})
            #items['tipo'] = tipos[n]
            items['imagen'] = imagenes[n]
            yield items

        next_page= 'https://www.tiendainglesa.com.uy/Categoria/Hogar-y-Tiempo-Libre/Mascotas/1005/busqueda?0,0,*:*,1005,503,0,,%5B%5D,false,%5B%5D,%5B%5D,' + str(tiendainglesa.page_variable)
        tiendainglesa.page_variable += 1

        if proximo == '>':
            yield response.follow(next_page, callback=self.parse_mascotas)
        #else:
        #    tiendainglesa.page_variable = 2
        #    yield scrapy.Request("https://www.tiendainglesa.com.uy/Categoria/Beb%C3%A9s/Pa%C3%B1ales/529/busqueda?0,0,*:*,529,612,0,,%5B%5D,false,%5B%5D,%5B%5D,0",
        #                 callback=self.parse_pescaderia)