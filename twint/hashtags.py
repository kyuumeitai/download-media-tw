import twint
def main():
    # hashtags = [
    #     'ChileViolaLosDerechosHumanos', 'LosMilicosNoSonTusAmigos',
    #     'ChileNoQuiereMigajas', 'ChileDesperto', 'RenunciaPiñera',
    #     'ChileQuiereCambios'
    # ]
    hashtags = ['ChileDesperto', 'ChileNoQuiereMigajas']


    fromDay = 17
    today = 27

    for hashtag in hashtags:
        for day in range(fromDay, today+1):
            baseMonthStr = "2019-10-"
            print(''.join([baseMonthStr, str(day)]))
            print(hashtag)
            c = twint.Config()
            #c.Geo = "-33.436970, -70.634705, 400km" #300km de plaza italia
            c.Since = ''.join([baseMonthStr, str(day)])
            c.Until = ''.join([baseMonthStr, str(day+1)])
            c.Count = True
            c.Search = hashtag
            c.Debug = True
            c.Store_csv = True
            # c.Videos = True
            c.Output = ''.join(['../data/', hashtag, '-', baseMonthStr, str(day), '.csv'])
            twint.run.Search(c)
if __name__ == '__main__':
    main()
