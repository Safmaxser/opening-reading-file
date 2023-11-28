import pprint


def open_recipe_book(path_file):
    cook_book = {}
    with open(path_file, encoding='UTF-8') as f:
        while True:
            dish_name = f.readline().strip()
            quantity_ingredients = f.readline().strip()
            list_ingredients = []
            for number in range(int(quantity_ingredients)):
                ingredient_list = f.readline().strip().split(' | ')
                ingredient = {}
                ingredient['ingredient_name'] = ingredient_list[0]
                ingredient['quantity'] = int(ingredient_list[1])
                ingredient['measure'] = ingredient_list[2]
                list_ingredients.append(ingredient)
            cook_book[dish_name] = list_ingredients
            if not f.readline():
                break
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    dict_dishes = {}
    for dishe in dishes:
        list_ingredients = cook_book.get(dishe)
        if list_ingredients != None:
            for ingredient in list_ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in dict_dishes.keys():
                    dict_dishes[ingredient_name]['quantity'] += quantity
                else:
                    dict_ingredient = {}
                    dict_ingredient['measure'] = measure
                    dict_ingredient['quantity'] = quantity
                    dict_dishes[ingredient_name] = dict_ingredient
    return dict_dishes


cook_book = open_recipe_book('recipes.txt')
pp = pprint.PrettyPrinter()
pp.pprint(cook_book)
print()

dict_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
pp.pprint(dict_dishes)