'''
title           : JM_data_parseC.py
description     : Mutant ape from the OpenSea API is parsed with this program
author          : josh mack
date_created    : 20211026
date_modified   : 202110
version         : 2.0
python_version  : 3.9
'''


global shooting_stat, defense_stat, vision_stat, finish_stat

def parse_mutant_data(mutant_dict):

    stat = []
    stat.clear()
    mutant_id = mutant_dict['token_id']
    owner_address = mutant_dict['owner']['address']
    traits = mutant_dict['traits']
    sell_orders = mutant_dict['sell_orders']
    rarity_url = 'https://rarity.tools/mutant-ape-yacht-club/view/{}'.format(mutant_id)


    def constructor(stat):
        try:
            for s in range(len(traits)):
                if traits[s]["trait_type"] == stat:
                    return traits[s]['value']
        except:
            return 'ERROR'
    try:
        last_sale_time = mutant_dict['last_sale']['event_timestamp']
    except:
        last_sale_time = ' '
    try:
        last_sale_price = int(mutant_dict['last_sale']['total_price'])
        last_sale_price = last_sale_price/1000000000000000000
        last_sale_price = '{} ETH'.format(last_sale_price)
    except:
        last_sale_price = ' '
    try:
        cprice = [a_dict['current_price'] for a_dict in sell_orders]
        current = cprice[0]
        current_price = str(int(current)/1000000000000000000)
        current_price_eth = '{} ETH'.format(current_price)
    except:
        current_price_eth = ' '
    try:
        cdate = [[a_dict['created_date'] for a_dict in sell_orders]]
        list_date = cdate[0][0]
        list_date = list_date.replace('T', ' ')
    except:
        list_date = ' '
    shooting_stat = constructor('Shooting')
    finish_stat = constructor('Finish')
    defense_stat = constructor('Defense')
    vision_stat = constructor('Vision')
    cumulative_stat = shooting_stat+finish_stat+defense_stat+vision_stat
    result = {'rarity_url': rarity_url,
              'mutant_id': mutant_id,
              'owner_address': owner_address,
              'num_sales': mutant_dict['num_sales'],
              'last_sale_date': last_sale_time[:10],
              'last_sale_price': last_sale_price,
              'list_date': list_date[:19],
              'list_price': current_price_eth,
              'background': constructor('Background'),
              'fur': constructor('Fur'),
              'clothes': constructor('Clothes'),
              'mouth': constructor('Mouth'),
              'head': constructor('Head'),
              'head_accessory': constructor('Head Accessory'),
              'eyes': constructor('Eyes'),
              'jewellery': constructor('Jewellery'),
              'shooting': constructor('Shooting'),
              'finish': constructor('Finish'),
              'defense': constructor('Defense'),
              'vision': constructor('Vision'),
              'cumulative': cumulative_stat}
    return result

def parse_mutant_data(mutant_dict):

    sell_orders = mutant_dict['sell_orders']
    mutant_id = mutant_dict['token_id']


    try:
        last_sale_time = mutant_dict['last_sale']['event_timestamp']
        last_sale_price = int(mutant_dict['last_sale']['total_price'])
        last_sale_price = last_sale_price / 1000000000000000000
        last_sale_price = '{} ETH'.format(last_sale_price)
    except:
        last_sale_time = ' '
        last_sale_price = ' '
    try:
        cprice = [a_dict['current_price'] for a_dict in sell_orders]
        current = cprice[0]
        current_price = str(int(current)/1000000000000000000)
        current_price_eth = '{} ETH'.format(current_price)
    except:
        current_price_eth = ' '
    try:
        cdate = [[a_dict['created_date'] for a_dict in sell_orders]]
        list_date = cdate[0][0]
        list_date = list_date.replace('T', ' ')
    except:
        list_date = ' '

    result = {'mutant_id': mutant_id,
              'num_sales': mutant_dict['num_sales'],
              'last_sale_date': last_sale_time[:10],
              'last_sale_price': last_sale_price,
              'list_date': list_date[:19],
              'list_price': current_price_eth}

    return result