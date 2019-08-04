from math import floor
import json


def statment(invoice, plays):

    totalAmout = 0
    volumeCreadits = 0
    result = 'Statement for {}'.format(invoice['customer'])

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        thisAmount = 0

        if play['type'] == 'tragedy':
            thisAmount = 40000
            if perf['audience'] > 30:
                thisAmount += 1000* (perf['audience'] -30)

        elif play['type'] == 'comedy':
            thisAmount = 30000
            if perf['audience'] > 20:
                thisAmount += 10000 + 500 * (perf['audience'] - 20)
            thisAmount += 300 * perf['audience']

        else:
            print('PerformancesTypeError')

        volumeCreadits += max(perf['audience'] - 30, 0)

        if play['type'] == 'comedy':
            volumeCreadits += floor(perf['audience'] / 5)

        result += '{}: {:.2f}  {} seats'.format(play['name'], thisAmount / 100, perf['audience'])
        totalAmout += thisAmount

    result += 'Amount owed is {}'.format(totalAmout / 100)
    result += 'You earned {} credits'.format(volumeCreadits)

    return result

def anountFor(performance):






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


