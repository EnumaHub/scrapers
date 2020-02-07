# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Disco2Item(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()
    
class Pescaderia(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()
    
class Chacinados(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Pollo(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Fiambres(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class FrutasYVerduras(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Queso(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Lacteos(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Congelados(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Pastas(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Canasta(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Perfumeria(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()

class Mascotas(scrapy.Item):
	nombre = scrapy.Field()
	precios = scrapy.Field()	
	tipo = scrapy.Field()
	imagen = scrapy.Field()
	sitio = scrapy.Field()