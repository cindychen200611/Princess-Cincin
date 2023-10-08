from flask import Flask, render_template, request, redirect

app = Flask(__name__)

chosen = []
def add_to_itinerary():
    if request.method == "POST":
        item = request.form.get('itinerary')
        print('item:', item)
        if item not in chosen:
            chosen.append(item)
        else:
            chosen.remove(item)
        print(chosen)

planet = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Moon']
dis = [57.9, 108, 227, 778.6, 1430, 2900, 4500, 150]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/sites')
def sites():
    return render_template('sites.html', chosen=chosen)

@app.route('/mercury', methods=["POST","GET"])
def mercury():
    add_to_itinerary()
    return render_template('/planets/mercury.html')

# mecury
@app.route('/BeethovenImpactCrater')
def beethoven():
    return render_template('/sites/mercury/beethovenimpactcrater.html')

@app.route('/CalorisBasin')
def caloris():
    return render_template('/sites/mercury/calorisbasin.html')

@app.route('/TolstojCrater')
def tolstoj():
    return render_template('/sites/mercury/tolstojcrater.html')

@app.route('/venus', methods=["POST","GET"])
def venus():
    add_to_itinerary()
    return render_template('/planets/venus.html')

# venus
@app.route('/MaxwellMontes')
def maxwellmontes():
    return render_template('/sites/venus/maxwellmontes.html')

@app.route('/AphroditeTerra')
def aphroditeterra():
    return render_template('/sites/venus/aphroditeterra.html')

@app.route('/BaltisVallis')
def baltisvallis():
    return render_template('/sites/venus/baltisvallis.html')

@app.route('/CarmentaFarra')
def carmentafarra():
    return render_template('/sites/venus/carmentafarra.html')

@app.route('/TheArachnoid')
def thearachnoid():
    return render_template('/sites/venus/thearachnoid.html')

@app.route('/MaatMons')
def maatmons():
    return render_template('/sites/venus/maatmons.html')

@app.route('/mars', methods=["POST","GET"])
def mars():
    add_to_itinerary()
    return render_template('/planets/mars.html')
    
# mars
@app.route('/DevonIsland')
def devonisland():
    return render_template('/sites/mars/devonisland.html')

@app.route('/JezeroCrater')
def jezerocrater():
    return render_template('/sites/mars/jezerocrater.html')

@app.route('/VallesMarineris')
def vallesmarineris():
    return render_template('/sites/mars/vallesmarineris.html')

@app.route('/OlympusMons')
def olympusmons():
    return render_template('/sites/mars/olympusmons.html')

@app.route('/jupiter', methods=["POST","GET"])
def jupiter():
    add_to_itinerary()
    return render_template('/planets/jupiter.html')

# jupiter
@app.route('/theGreatRedSpot')
def theGreatRedSpot():
    return render_template('/sites/jupiter/theGreatRedSpot.html')

@app.route('/JupiterRing')
def JupiterRing():
    return render_template('/sites/jupiter/JupiterRing.html')

@app.route('/saturn', methods=["POST","GET"])
def saturn():
    add_to_itinerary()
    return render_template('/planets/saturn.html')

#saturn
@app.route('/SaturnRing')
def saturnring():
    return render_template('/sites/saturn/saturnring.html')

@app.route('/SaturnNorthernHemisphere')
def Saturnnorthernhemisphere():
    return render_template('/sites/saturn/Saturnnorthernhemisphere.html')

@app.route('/SaturnHexagon')
def saturnhexagon():
    return render_template('/sites/saturn/saturnhexagon.html')

@app.route('/SaturnHurricane')
def saturnhurricane():
    return render_template('/sites/saturn/saturnhurricane.html')

@app.route('/uranus', methods=["POST","GET"])
def uranus():
    add_to_itinerary()
    return render_template('/planets/uranus.html')

# uranus
@app.route('/UranusPlanetaryRings')
def uranusplanetaryrings():
    return render_template('/sites/uranus/uranusplanetaryrings.html')

@app.route('/neptune', methods=["POST","GET"])
def neptune():
    add_to_itinerary()
    return render_template('/planets/neptune.html')

# neptune
@app.route('/theGreatDarkSpot')
def theGreatDarkSpot():
    return render_template('/sites/neptune/theGreatDarkSpot.html')
    
@app.route('/NeptuneRings')
def neptunerings():
    return render_template('/sites/neptune/NeptuneRings.html')

@app.route('/NeptuneMoon_Triton')
def NeptuneMoon_Triton():
    return render_template('/sites/neptune/NeptuneMoon_Triton.html')

@app.route('/moon', methods=["POST","GET"])
def moon():
    add_to_itinerary()
    return render_template('/planets/moon.html')

# moon
@app.route('/LunarSouthPole')
def LunarSouthPole():
    return render_template('/sites/moon/LunarSouthPole.html')

@app.route('/OceanusProcellarum')
def OceanusProcellarum():
    return render_template('/sites/moon/OceanusProcellarum.html')

@app.route('/MareOrientale')
def MareOrientale():
    return render_template('/sites/moon/MareOrientale.html')

@app.route('/Apollo11')
def Apollo11():
    return render_template('/sites/moon/Apollo11.html')

@app.route('/itinerary', methods=["POST", "GET"])
def show_list(chosen=chosen):
    if len(chosen) != 7:
        return redirect('/sites')
        
    start = dis[-1]
    output = []
    
    for j in range(len(chosen)):
        min_dis = 5000
        for i in chosen:
            if i != '':
                if abs(dis[planet.index(i[:i.find('-')-1])] - start) < min_dis:
                    min_dis = abs(dis[planet.index(i[:i.find('-')-1])] - start)
                    mni = chosen.index(i)
        output.append([chosen[mni], min_dis])
        start = dis[planet.index(chosen[mni][:chosen[mni].find('-')-1])]
        chosen[mni] = ''

    chosen.clear()
        
    return render_template('list.html', chosen=output), chosen

app.run(host='0.0.0.0', port=81)
