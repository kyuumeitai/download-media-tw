import twint
def main():

    c = twint.Config()
    c.Geo = "-33.436970, -70.634705, 400km" #300km de plaza italia
    c.Since = "2019-10-15"
    # c.Debug = True
    c.Store_csv = True
    # c.Custom_csv = ["id", "date", "user_id", "username", "tweet", "hashtags", "location"]
    c.Videos = True
    c.Output = "twittervideos.csv"
    # write to file
    twint.run.Search(c)
if __name__ == '__main__':
    main()
