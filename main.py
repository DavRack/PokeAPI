import os
import flask
import requests
import berriesStatistics
import multiprocessing
import matplotlib.pyplot as plt
import base64
import io 

from dotenv import load_dotenv
load_dotenv()


app = flask.Flask(__name__)

def getAllBerries():
    response = requests.get(url='https://pokeapi.co/api/v2/berry?offset=0&limit=-1')
    berries = response.json().get("results",[])
    return berries

def getBerryInfo(berry):
    response = requests.get(url=berry["url"])
    berryInfo = response.json()
    return berryInfo

def getBerriesInfo(berries):
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    try:
        berriesInfo = pool.map(getBerryInfo, berries)
    except:
        flask.abort(400)
    return berriesInfo

def getBerriesGrowthTime(berriesInfo):
    berriesGrowthTime = list(map(lambda berry: berry["growth_time"], berriesInfo))
    return berriesGrowthTime


@app.route("/allBerryStats")
def allBerryStats():
    # get all berries
    berries = getAllBerries()
    berriesInfo = getBerriesInfo(berries)
    berriesGrowthTime = getBerriesGrowthTime(berriesInfo)

    # calculate statistics
    result = {
        "berries_names": berriesStatistics.getBerriesNames(berriesInfo),
        "min_growth_time": berriesStatistics.getMinGrowthTime(berriesGrowthTime),
        "median_growth_time":berriesStatistics.getMedianGrowthTime(berriesGrowthTime),
        "max_growth_time":berriesStatistics.getMaxGrowthTime(berriesGrowthTime),
        "variance_growth_time":berriesStatistics.getVarianceGrowthTime(berriesGrowthTime),
        "mean_growth_time": berriesStatistics.getMeanGrowthTime(berriesGrowthTime),
        "frequency_growth_time": berriesStatistics.getFrequencyGrowthTime(berriesGrowthTime),
    }
    resp = flask.jsonify(result)
    resp.headers["Content-Type"] = "application/json"
    return resp

@app.route("/allBerryFrequency")
def allBerryFrequency():
    # get all berries
    berries = getAllBerries()
    berriesInfo = getBerriesInfo(berries)
    berriesGrowthTime = getBerriesGrowthTime(berriesInfo)
    plt.hist(berriesGrowthTime)
    plt.ylabel('Frequency')
    plt.xlabel('Growth time')
    plt.title("Berries growth time frequency")
    # plt.show()
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes,  format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read()).decode()
    return f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
      </head>
      <body>
        <img src="data:image/png;base64,{pic_hash}">
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host=os.getenv("host"), port=int(os.getenv("port") or 3000), debug=os.getenv("debug") == "True")
