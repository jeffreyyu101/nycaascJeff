
# coding: utf-8

# import necessary packages
import pandas as pd

# In[1]:

wks_list = pd.read_csv("wks_2018_list_clean.csv", encoding='windows-1252')
print ("Type write_page(wks_list) to start.")

# In[1]:
    
def write_page(wks_list):
    
    innerHTML = ""
    speakerCount = 0 # recognizes whether speaker data in following rows is part of an above workshop
    currTrack = 1
    wksNum = 0
    # insert data into variables
    for index, row in wks_list.iterrows():
        print(index, row, type(row))
        track = int(row['track'])
        time = row['time']
        numSpeakers = row['num_speakers']
        location = row['location']
        if pd.notna(row['title']):
            title = row['title'][4:]
        description = row['description']
        speaker = row['speaker']
        bio = row['bio']
        if pd.notna(row['img_code']):
            img_code = row['img_code']
        else:
            img_code = ""
        
        if currTrack != track:
            currTrack = track
            wksNum = 0
        
        if (speakerCount == 0): # default state
            wksNum += 1
            speakerCount = numSpeakers
            # add head, body opening, workshop information
            innerHTML = head(title) + BODY_OPENING + workshopIntro(track,title,location,description,time)
            # add speaker in same row
            innerHTML += """
                <section id="workshop-speakers" class="pt-3">
                  <div class="row">
                  """ + workshopSpeakerSection(speaker, img_code, bio) + """
                  """
            
            speakerCount -= 1
        # add extra speakers if occupying below rows
        else:
            innerHTML += """
                  """ + workshopSpeakerSection(speaker, img_code, bio) + """
                  """
            speakerCount -= 1
           
        # ends and submits file when all speakers accounted for
        if (speakerCount == 0):
            innerHTML += """
                      </div>
                    </section><!--workshop-speakers-->
                """
            innerHTML += BODY_CLOSING
    
            # write file
            wksNumStr = "0" + str(wksNum)
            directory = "{track}{num}.html".format(track=int(track), num=wksNumStr)
            f = open(directory, 'w', encoding='utf-8')
            f.write(innerHTML)
            f.close()

# In[2]:

def head(title):
    headHTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="Richard Lu">
    <link rel="icon" href="assets/favicon.ico">

    <title>NYCAASC | {wksTitle} </title>

     <!-- Bootstrap core CSS -->
     <link href="../../assets/bootstrap-4.0.0-dist/css/bootstrap-reboot.min.css" rel="stylesheet">
     <link href="../../assets/bootstrap-4.0.0-dist/css/bootstrap-grid.min.css" rel="stylesheet">
     <link href="../../assets/bootstrap-4.0.0-dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../../assets/css/nycaasc-custom.css" rel="stylesheet">
    <link href="../../assets/css/workshop.css" rel="stylesheet">
    <!-- Streetvertising Font CSS -->
    <link href="../../assets/css/font-streetvertising.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="..//assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
    """.format(wksTitle=title)
    return headHTML

# In[3]:

# Opening of body
    # opening body tags
    # header
    # div.container opening tag
BODY_OPENING = """
<body>
    <header id="header"></header>
    <main>
      <div class="container">    
    """    

# Closing of body
        # div.container closing tag
        # footer
        # google analytics and javascript
        # closing body tags
BODY_CLOSING = """
            <p class="pt-5"><a href="../../conference.html" title="NYCAASC 2018">&larr; Back to NYCAASC 2018 conference page</a></p>
        </div>
    </main>
    <footer id="footer"></footer>
    <script>
            (function(i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r;
                i[r] = i[r] || function() {
                    (i[r].q = i[r].q || []).push(arguments)
                }, i[r].l = 1 * new Date();
                a = s.createElement(o),
                    m = s.getElementsByTagName(o)[0];
                a.async = 1;
                a.src = g;
                m.parentNode.insertBefore(a, m)
            })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
    
            ga('create', 'UA-68409586-1', 'auto');
            ga('send', 'pageview');
    </script>
    <!--Required Popper.js and jQuery-->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <!--Bootstrap 4-->
    <script src="../../assets/bootstrap-4.0.0-dist/js/bootstrap.bundle.min.js"></script>
    <script src="../../assets/bootstrap-4.0.0-dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
    <!--Import site header-->
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
    <script>
        $(function() {
            $("#header").load("../../wks-header.html");
            $("#footer").load("../../wks-footer.html");
        });
    </script>
</body>
</html>
    """    

# In[4]:
    
def workshopIntro(track, title, location, desc, time, triggers="None"):
    innerHTML = """
        <section id="workshop-intro">
          <h1>NYCAASC 2018: Emergence Workshops</h1>
          <p><a href="../../conference.html" title="NYCAASC 2018">NYCAASC 2018</a> > Workshops: Track {trackNum}</p>
          <h2>{wksTitle}</h2>
          <p class="lead">{roomNum}, {time}</p>
          <p>{wksDesc}</p>
        </section><!--#workshop-intro-->    
    """.format(trackNum=int(track), wksTitle=title, roomNum = location, wksDesc = desc, time = time)
    return innerHTML

# In[5]:
    
def workshopSpeakerSection(speaker, img_code, bio=""):
    if img_code == "":
        img_code = "profile-icon"
    innerHTML = """
                <div class="col-xs-12 col-md-4">
                  <div class="bio-circle mb-3">
                    <img src="../../assets/img/wks/2018/{speakerImg}.jpg" alt="{speakerName}" class="img-fluid rounded">
                  </div>
                  <h3>{speakerName}</h3>
                  <p>{speakerBio}</p>
                </div>
    """.format(speakerImg = img_code, speakerName = speaker, speakerBio = bio)
    return innerHTML

# In[6]:
def generateImgCode(img_code):
    code = img_code.lower()
    code = code.replace(' ','-')
    return code