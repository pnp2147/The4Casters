import pandas as pd

def merge_rochester():
    print("Reading Rochester. . .")
    roc1 = pd.read_excel("Data/Rochester/1948To1955Rochester.xlsx", dtype=str)
    roc2 = pd.read_excel("Data/Rochester/1956To1965Rochester.xlsx", dtype=str)
    roc3 = pd.read_excel("Data/Rochester/1966To1975Rochester.xlsx", dtype=str)
    roc4 = pd.read_excel("Data/Rochester/1976To1985Rochester.xlsx", dtype=str)
    roc5 = pd.read_excel("Data/Rochester/1986To1995Rochester.xlsx", dtype=str)
    roc6 = pd.read_excel("Data/Rochester/1996To2005Rochester.xlsx", dtype=str)
    roc7 = pd.read_excel("Data/Rochester/2006To2015Rochester.xlsx", dtype=str)
    roc8 = pd.read_excel("Data/Rochester/2015to2024Rochester.xlsx", dtype=str)

    roc_master = pd.concat([roc1, roc2, roc3, roc4, roc5, roc6, roc7, roc8])

    return roc_master

def merge_buffalo():
    print("Reading Buffalo. . .")
    buf1 = pd.read_csv("Data/Buffalo/1942to1944_Buffalo.csv", dtype=str)
    buf2 = pd.read_csv("Data/Buffalo/1945to1954_Buffalo.csv", dtype=str)
    buf3 = pd.read_csv("Data/Buffalo/1955to1964_Buffalo.csv", dtype=str)
    buf4 = pd.read_csv("Data/Buffalo/1965to1974_Buffalo.csv", dtype=str)
    buf5 = pd.read_csv("Data/Buffalo/1975to1984_Buffalo.csv", dtype=str)
    buf6 = pd.read_csv("Data/Buffalo/1985to1994_Buffalo.csv", dtype=str)
    buf7 = pd.read_csv("Data/Buffalo/1995to2004_Buffalo.csv", dtype=str)
    buf8 = pd.read_csv("Data/Buffalo/2005to2014_Buffalo.csv", dtype=str)
    buf9 = pd.read_csv("Data/Buffalo/2015to2024_Buffalo.csv", dtype=str)

    buf_master = pd.concat([buf1, buf2, buf3, buf4, buf5, buf6, buf7, buf8, buf9])

    return buf_master

def merge_syracuse():
    print("Reading Syracuse. . .")
    syr1 = pd.read_csv("Data/Syracuse/1942to1944_Syracuse.csv", dtype=str)
    syr2 = pd.read_csv("Data/Syracuse/1945to1954_Syracuse.csv", dtype=str)
    syr3 = pd.read_csv("Data/Syracuse/1955to1064_Syracuse.csv", dtype=str)
    syr4 = pd.read_csv("Data/Syracuse/1965to1974_Syracuse.csv", dtype=str)
    syr5 = pd.read_csv("Data/Syracuse/1975to1984_Syracuse.csv", dtype=str)
    syr6 = pd.read_csv("Data/Syracuse/1985to1994_Syracuse.csv", dtype=str)
    syr7 = pd.read_csv("Data/Syracuse/1995to2004_Syracuse.csv", dtype=str)
    syr8 = pd.read_csv("Data/Syracuse/2005to2014_Syracuse.csv", dtype=str)
    syr9 = pd.read_csv("Data/Syracuse/2015to2023_Syracuse.csv", dtype=str)

    syr_master = pd.concat([syr1, syr2, syr3, syr4, syr5, syr6, syr7, syr8, syr9])

    return syr_master

def main():
    syracuse = merge_syracuse()
    buffalo = merge_buffalo()
    rochester = merge_rochester()
    print("Merging all files. . .")
    master = pd.concat([syracuse, buffalo, rochester])
    master.to_csv("MasterData.csv", index=False)
    print("Merge Complete.")

main()