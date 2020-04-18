# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from .items import *

import datetime

fecha_hoy = datetime.datetime.now()

class Disco2Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['carnes_rojas_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Disco2Item):
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][-1]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}}, upsert=True)
            except TypeError:
                pass
                       
            self.collection.update_one({'nombre': nombre_objeto}, {'$set': { 'sitio' : item['sitio']}})            

            if objeto_base == None:
                self.collection.insert(dict(item))            
            return item                               
        else:
            return item

class pescaderia_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['pescaderia_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Pescaderia):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class chacinados_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['chacinados_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Chacinados):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class pollo_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['pollo_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Pollo):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class fiambres_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['fiambres_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Fiambres):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class frutas_y_verduras_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['frut_y_verd_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, FrutasYVerduras):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class queso_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['queso_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Queso):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class lacteos_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['lacteos_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Lacteos):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class congelados_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['congelados_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Congelados):            
            snombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class pastas_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['pastas_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Pastas):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class canasta_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['canasta_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Canasta):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)
                        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))

            return item                               
        else:
            return item

class perfumeria_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['perfumeria_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Perfumeria):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class mascotas_Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['disco']
        self.collection = db['mascotas_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Mascotas):            
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][0]['precio']        
            objeto_base = fetch_data(nombre_objeto)        
            try:
                if precio_objeto != objeto_base['precios'][-1]['precio']:
                    print('paso')
                    self.collection.update_one({'nombre': nombre_objeto}, {'$push': {'precios': {'precio': precio_objeto, 'fecha': fecha_hoy}}})
            except TypeError:
                pass

            if objeto_base == None:
                self.collection.insert(dict(item))
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item