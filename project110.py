import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import csv

file = pd.read_csv("project110.csv")
data = file["reading_time"].tolist()
fig = ff.create_distplot([data],["Reading Time"],show_hist = False)
fig.show()
population_mean = statistics.mean(data)
sd = statistics.stdev(data)
print(population_mean)
print(sd)

def randomsetofmean():
    dataset = []
    for i in range(0,30):
        randomindex = random.randint(0,len(data))
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    dataset_sd = statistics.stdev(dataset)
    return mean


# print("Mean Of Sample: ", mean)
# print("Standard Deviation Of Sample: ", dataset_sd)

def showfigure(meanlist):
    df = meanlist
    fig = ff.create_distplot([df],["Reading Time"],show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0,100):
        setofmeans = randomsetofmean()
        meanlist.append(setofmeans)
    showfigure(meanlist)
    mean = statistics.mean(meanlist)
    sd_meanlist = statistics.stdev(meanlist)
    print("Standard Deviation Of Sampling Distribution: ", sd_meanlist)
    print("Mean Of Sampling Distribution: ", mean)
setup()