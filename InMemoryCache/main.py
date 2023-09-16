from LRUCache import LRUCache


def main():
    cache = LRUCache()
    cache.put_item(1, '2')
    cache.put_item(2, '2')
    cache.put_item(3, '3')
    cache.put_item(500, '4')
    cache.put_item(601, '3')
    
    print(f'ITEM AT 601: {cache.get_item(601)}')
    print(f'ITEM AT 1: {cache.get_item(1)}')
    print(f'ITEM AT 2: {cache.get_item(2)}')
    print(f'ITEM AT 3: {cache.get_item(3)}')
    print(f'ITEM AT 500: {cache.get_item(500)}')
    
    cache.put_item(601, '3')
    cache.put_item(3, '3')
    
    cache.put_item(700, 3)
    cache.put_item(700, 3)
    
    cache.put_item(69, '3')
    cache.put_item('34', '3')
    
    cache.put_item('HIMANSHU', 3)
    cache.put_item('JDDA', 3)
    cache.get_item('5000')
    cache.get_item('KBC')
    
    cache.remove_item('KBC')
    cache.remove_item('34')
    cache.put_item('HX', 3)
    cache.remove_item('34')
    cache.remove_item('HX')
    cache.remove_item('JDDA')
    cache.remove_item('HIMANSHU')
    cache.remove_item(69)
    cache.put_item(500, '4')
    cache.remove_item(700)
    cache.put_item(1, '2')
    cache.put_item(2, '2')
    cache.put_item(3, '3')
    cache.put_item(601, '3')
    
if __name__ == "__main__":
    main()