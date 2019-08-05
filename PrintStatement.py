from math import floor
import json


def statment(invoice, plays):

    return rederPlainText(createStatementData(invoice, plays))



def createStatementData(invoice, plays):
    result = {}
    result['customer'] = invoice['customer']
    result['performances'] = invoice['performances']
    result['plays'] = plays
    return result

def rederPlainText(statementData):
    result = 'Statement for {}'.format(statementData['customer'])

    for perf in statementData['performances']:
        result += '{}: {:.2f}  {} seats'.format(playFor(perf, statementData['plays'])['name'], anountFor(perf, statementData['plays']) / 100,
                                                perf['audience'])

    totalAmout = appleSauce()
    volumeCreadits = totalVolumeCreadits()

    result += 'Amount owed is {}'.format(totalAmout / 100)
    result += 'You earned {} credits'.format(volumeCreadits)

    return result

def appleSauce():
    result =0
    for perf in invoice['performances']:
        result += anountFor(perf, plays)
    return result

def totalVolumeCreadits():
    result =0
    for perf in invoice['performances']:
        result += volumeCreaditsFor(perf, plays)
    return result


def volumeCreaditsFor(perf, plays):
    result = 0
    result += max(perf['audience'] - 30, 0)
    if playFor(perf, plays)['type'] == 'comedy':
        result += floor(perf['audience'] / 5)
    return result



def anountFor(aperformance_dict, plays):
    result = 0
    if playFor(aperformance_dict, plays)['type'] == 'tragedy':
        result = 40000
        if aperformance_dict['audience'] > 30:
            result += 1000 * (aperformance_dict['audience'] - 30)

    elif playFor(aperformance_dict, plays)['type'] == 'comedy':
        result = 30000
        if aperformance_dict['audience'] > 20:
            result += 10000 + 500 * (aperformance_dict['audience'] - 20)
        result += 300 * aperformance_dict['audience']

    else:
        print('PerformancesTypeError')
    return result

def playFor(aperformance_dict, plays):
    return plays[aperformance_dict['playID']]




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


