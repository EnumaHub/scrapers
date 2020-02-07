# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiendainglesaItem(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Pescaderia(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Pollo(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Chacinados(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Fiambres(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Frutas(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Verduras(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Quesos(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Lacteos(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Congelados(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Canasta(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Limpieza(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Perfumeria(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()

class Paniales(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()
    
class Mascotas(scrapy.Item):
    nombre = scrapy.Field()
    precios = scrapy.Field()    
    #tipo = scrapy.Field()
    imagen = scrapy.Field()