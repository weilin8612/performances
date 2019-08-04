#
#
# plays = {'hamlet': {'name': 'Hanlet', 'type': 'tragedy'},
#          'as-like': {'name': 'As You Like It', 'type': 'comedy'},
#          'othello': {'name': 'Othello', 'type': 'tragedy'}
# }
#
# invoices = {'customer': 'BigCo',
#              'performances': [{'playID': 'hamlet',
#                                'audience': 55
#                                 },
#                               {'playID': 'as-like',
#                                'audience': 35
#                                },
#                               {'playID': 'othello',
#                                'audience': 40}
#                               ]
#
# }
#
# print(type(invoices))

# import json
#
# with open('plays.json', 'w', encoding='utf-8') as f:
#     json.dump(plays, f)
#
# with open('invoices.json', 'w', encoding='utf-8') as f:
#     json.dump(invoices, f)
#
# with open('plays.json', 'r', encoding='utf-8') as f:
#     result = json.load(f)
#     print(result)

def f(n):
    '''
        >>> f(8)
        8
        >>> f(-8)
        0

    sd
    '''
    return max(n, 0)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    from difflib import ndiff
    str1 = 'abcdefg'
    str2 = 'gbctefz'
    diff = ndiff(str1, str2)
    print(''.join(diff))
