import webbrowser
# The script opens predefined websites using python dictionaries
l = {
        "https://www.bleepingcomputer.com/",
        "https://securityaffairs.co/wordpress/",
        "https://hbr.org/",
        "https://www.theregister.com/",
        "https://www.hackread.com/",
        "https://www.information-age.com/",
        "https://www.darkreading.com/",
        "https://hackaday.com/",
        "https://www.nextgov.com/",
        "https://www.technologyreview.com/",
        "https://www.infosecurity-magazine.com/",
        "https://www.cyberscoop.com/",
        "https://krebsonsecurity.com/",
        }

for x in l:
    webbrowser.open(x)
