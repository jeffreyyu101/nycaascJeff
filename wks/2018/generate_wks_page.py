
# coding: utf-8

# import necessary packages
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# In[1]:

wks_list = pd.read_csv("wks_2018_list.csv")


def write_wks_page(list_of_workshops, year):
    
    
    navigator = """
    
    <header id="header"></header>
    
    """
    
    # Loop through all lines in the file
    year = year
    for row in list_of_workshops:
        background_img = list_of_workshops['background_img'][x]
        track_title = list_of_workshops['track_title'][x]
        wks_title = list_of_workshops['Title of workshop']
        num_speakers = list_of_workshops['Number of speakers/facilitators'][x]
        speaker_img_url = list_of_workshops['speaker_img_url'][x]
        speaker_img_alt_txt = list_of_workshops['speaker_img_alt_txt'][x]
        speaker_bio_prev = list_of_workshops['speaker_bio_prev'][x]
        speaker_section = speaker_section()
    
    wks_page = header + navigator + wks_info(track, wks_title, wks_descr) + wks_speakers(speaker_img_url, speaker_img_alt_txt, speaker_bio_prev)
  
  #path_to_repo is the path where you are storing the NYCAASC website locally
    directory ="{path_to_repo}/wks/{year}/{track_id}/{wks_num}.html".format("path_to_repo=path_to_repo, year=year, track_id=track_id wks_num=wks_num")
    f = open(directory, 'w')
    f.write(wks_page)
    f.close()

# In[2]:

#Creates individual section for workshop speaker
def speaker_block(speaker_name, speaker_bio, bio_id):
    return """
          <div class="row">
          
              <div class="col-md-4>
                <img class="img-responsive" src="assets/img/wks/{bio_id}.jpg" >
                  
              </div>
              
              <div class="col-md-8">
                <h3>{speaker_name}</h3>
                <p>{speaker_bio}</p>
                <p></p><!--Social media/website links-->
                <p>Other workshops: <a href="">Workshop 1</a>, <a href="">Workshop 2</a></p><!--If applicable-->
              </div>
              
          </div>
          
""".format(speaker_name=speaker_name, speaker_bio=speaker_bio, bio_id = bio_id)

# In[1]:
    
def write_page(wks_list):
    
    # insert data into variables
    track = wks_list['track']
    
    
    
    #assemble HTML string
        #insert data from csv into HTML string templates
    innerHTML = head() + body()
    #write file
    


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

def body():
    # Opening of body
        # opening body tags
        # header
        # div.container opening tag
    bodyOpening = """
<body>
    <header id="header"></header>
    <main>
      <div class="container">    
    """
        
    # #workshop-intro: contains all HTML within #workshop-intro
    workshop_intro = "" # replace with workshopIntro() when HTML assembled
    
    # #workshop-speakers: contains all HTML within #workshop-speakers
    workshop_speakers = """
        <section id="workshop-speakers">
          <div class="row">""" + workshopSpeakerSection + """
          </div>
        </section><!--workshop-speakers-->
    """.format() # replace with workshopSpeakers() when HTML assembled
        
    # Closing of body
        # div.container closing tag
        # footer
        # google analytics and javascript
        # closing body tags
    bodyClosing = """
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
            $("#header").load("../../header.html");
            $("#footer").load("../../footer.html");
        });
    </script>
</body>
</html>
    """
    return bodyOpening + workshop_intro + workshop_speakers + bodyClosing

# In[4]:
    
def workshopIntro(track, title, location, desc, triggers="None"):
    innerHTML = """
        <section id="workshop-intro">
          <h1>NYCAASC 2018: Emergence Workshops</h1>
          <p><a href="../../conference.html" title="NYCAASC 2018">NYCAASC 2018</a> > Workshops: Track {trackNum}</p>
          <h2>{wksTitle}</h2>
          <p class="lead">{roomNum}</p>
          <p><strong>Workshop description</strong>: {wksDesc}</p>
          <p><strong>Trigger warnings</strong>: {wksTriggerWarnings}</p>
        </section><!--#workshop-intro-->    
    """.format(trackNum=track, wksTitle=title, roomNum = location, wksDesc = desc, wksTriggerWarnings = triggers)
    return innerHTML

# In[5]:
    
def workshopSpeakerSection(speaker, bio):
    innerHTML = """
        <div class="col-xs-12 col-md-4">
          <div class="bio-circle d-flex justify-content-center align-items-center mb-3">
            <span>200x200</span>
            <img src="" alt="" class="img-fluid">
          </div>
          <h3>{speakerName}</h3>
          <p>{speakerBio}</p>
        </div>
    """.format(speakerName = speaker, speakerBio = bio)
    return innerHTML


# In[ ]:

#Compile all of the speakers of one workshop
def get_all_speakers(list_of_workshops, num_speakers):
    #Create a list of all of the speaker names
    list_of_names = list_of_workshops.iloc[3,5,7]
    #Create a list of all of the speaker bios
    list_of_bios = list_of_workshops.iloc[4,6,8]
    list_of_ids = list_of_workshops #create id creator function to add to dataframe
    total_speaker_blocks = """"""
    #Create a speaker block string for each speaker
    for x in range(num_speakers):
        total_speaker_blocks += speaker_block(list_of_names[x], list_of_bios[x], list_of_ids[x])
    return total_speaker_blocks


# In[8]:

def speaker_section(num_speaker, speaker_block):
    speaker_chunk = """<div class="row">"""
    for speaker in range(num_speaker):
        if ((speaker % 3) == 0) & speaker !=0:
            speaker_chunk += """</div> \n <div class="row">"""
          
            speaker_chunk += str(speaker_block[speaker]) #future present_block(function)
          
        else: 
            speaker_chunk += speaker_block[speaker]
            speaker_chunk += """</div>"""
    return speaker_chunk
#add end div
#def for taking first lower(initial), and lower(lastname) to construct different directores
#def for creating short bio


# In[9]:

#speaker_block = ['A', 'B', 'C', 'D', 'E']
#speaker_block = ['A', 'B', 'C', 'D', 'E', 'F']
#speaker_block = ['A', 'B']
#num_speaker = len(speaker_block)
#print speaker_section(num_speaker, speaker_block)


# In[2]:

#Creates speaker directory ID from track id and speaker name (probably not necessary)
def speaker_directory (track_id, speaker_first, speaker_last):
    first_names = speaker_first.split(' ')
    first_initials = ""
    for name in first_names:
        first_initials += name[0]
  
    return track_id + first_initials + speaker_last


# In[11]:

#Creates shortened bio (probably not necessary)
def short_bio(bio):
    charcount = 0
    wordcount = 0
    for char in bio:
        charcount += 1
        if wordcount < 20:
            if char == ' ':
                wordcount += 1 
        else:
              return bio[:charcount-2] + "..." #return first 20 words of bio
      
        return bio[:50] + "..." #return first 50 chars by default


# In[12]:

def speaker_chunk(speaker_img_url, speaker_img_alt_txt, speaker_bio_prev):
    return """
  <div class="col-sm-6 col-md-4">
     <div class="thumbnail">
         <img src="{speaker_img_url}" alt="{speaker_img_alt_txt}">
                  <div class="caption">
                    <h3>Thumbnail label</h3>
                    <p>{speaker_bio_prev}</p>
                    <p><a href="#" class="btn btn-primary" role="button">Read Full Bio</a></p>
                  </div>
      </div>
   </div>""".format(speaker_img_url=speaker_img_url, speaker_img_alt_txt=speaker_img_alt_txt, speaker_bio_prev=speaker_bio_prev)


# In[13]:

#Creates formatted opening section with workshop track, title, description
def wks_info (track, wks_title, wks_descr):
    trackString = ""
    if track == 1:
        trackString = "Track 1"
    elif track == 2:
        trackString = "Track 2"
    elif track == 3:
        trackString = "Track 3"
    
    return """
    <h2>""" + trackString + """Track 1: Community</h2>

    <h2>{wks_title}</h2>

    <p>{wks_descr}</p>
      """.format(track=track, wks_title=wks_title, wks_descr=wks_descr)