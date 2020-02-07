# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from .items import *

import datetime

fecha_hoy = datetime.datetime.now()

class TiendainglesaPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['carnes_rojas_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, TiendainglesaItem):
            nombre_objeto = item['nombre']
            precio_objeto = item['precios'][-1]['precio']        
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


class PescaderiaPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

class PolloPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

class ChacinadosPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

class FiambresPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

class FrutasPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['fritas_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Frutas):
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

class VerdurasPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['verduras_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Verduras):
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

class QuesosPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['quesos_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Quesos):
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

class LacteosPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

class CongeladosPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['congelados_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Congelados):
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

class CanastaPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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
                #self.collection.update({'nombre': item['nombre']}, dict(item), upsert=True)
            
            return item                               
        else:
            return item

class LimpiezaPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['limpieza_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Limpieza):
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

class PerfumeriaPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

class PanialesPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
        self.collection = db['paniales_tb']        

    def process_item(self, item, spider):
        def fetch_data(nombre_objeto):
            return self.collection.find_one({'nombre': nombre_objeto})

        if isinstance(item, Paniales):
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

class MascotasPipeline(object):    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['tiendainglesa']
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

