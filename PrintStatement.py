from math import floor
import json


def statment(invoice, plays):

    totalAmout = 0
    volumeCreadits = 0
    result = 'Statement for {}'.format(invoice['customer'])

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        thisAmount = anountFor(perf, play)

        volumeCreadits += max(perf['audience'] - 30, 0)

        if play['type'] == 'comedy':
            volumeCreadits += floor(perf['audience'] / 5)

        result += '{}: {:.2f}  {} seats'.format(play['name'], thisAmount / 100, perf['audience'])
        totalAmout += thisAmount

    result += 'Amount owed is {}'.format(totalAmout / 100)
    result += 'You earned {} credits'.format(volumeCreadits)

    return result

def anountFor(aperformance_dict, play_dict):
    result = 0
    if play_dict['type'] == 'tragedy':
        result = 40000
        if aperformance_dict['audience'] > 30:
            result += 1000 * (aperformance_dict['audience'] - 30)

    elif play_dict['type'] == 'comedy':
        result = 30000
        if aperformance_dict['audience'] > 20:
            result += 10000 + 500 * (aperformance_dict['audience'] - 20)
        result += 300 * aperformance_dict['audience']

    else:
        print('PerformancesTypeError')
    return result





if __name__ == '__main__':
    with open('invoices.json', 'r', encoding='utf-8') as f:
        invoice = json.load(f)

    with open('plays.json', 'r', encoding='utf-8') as f:
        plays = json.load(f)

    result = statment(invoice, plays)
    textResult = 'Statement for BigCoHanlet: 650.00  55 seatsAs You Like It: 580.00  35 seatsOthello: 500.00  40 seatsAmount owed is 1730.0You earned 47 credits'
    if result == textResult:
        print('Test is ok')
    else:
        print('Test do not ok')
        print(textResult)
        print(result)


