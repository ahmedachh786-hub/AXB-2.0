from flask import Flask, request, render_template_string
from datetime import datetime, timedelta
import requests
import threading
import time

app = Flask(__name__)

# =========================================
# DISCORD WEBHOOK URL
# =========================================

WEBHOOK_URL = "https://discord.com/api/webhooks/1504755222306750496/mYvZ5FMo6K3THbhyCgUt9sbkVVkizZZZ36cd2RJ70BIlAzQur0Q9s7tufGU_61UlL2jb"

# =========================================
# APNI IMAGE LINK YAHAN LAGAO
# =========================================

DISCORD_IMAGE_URL = "https://i.imgur.com/aFN5vjO.jpeg"

# =========================================
# UID DATABASE
# =========================================

uids_data = {}

# =========================================
# AUTO UID EXPIRE SYSTEM
# =========================================

def auto_expire():

    while True:

        current_time = datetime.now()

        remove_uids = []

        for uid, expire_time in list(uids_data.items()):

            if current_time >= expire_time:

                data = {
                    "username": "AXD VIP SYSTEM",

                    "avatar_url": DISCORD_IMAGE_URL,

                    "embeds": [
                        {
                            "title": "⚠ VIP ACCESS EXPIRED",

                            "description":
                            f"❌ VIP access expired for UID `{uid}`.\n\n"
                            f"🔒 Renewal required to continue premium access.",

                            "color": 16711680,

                            "thumbnail": {
                                "url": DISCORD_IMAGE_URL
                            },

                            "fields": [
                                {
                                    "name": "👤 USER UID",
                                    "value": f"`{uid}`",
                                    "inline": True
                                },

                                {
                                    "name": "📌 STATUS",
                                    "value": "EXPIRED",
                                    "inline": True
                                }
                            ],

                            "footer": {
                                "text": "POWERED BY AXB • VIP SYSTEM"
                            }
                        }
                    ]
                }

                try:
                    requests.post(WEBHOOK_URL, json=data)
                except:
                    pass

                remove_uids.append(uid)

        for uid in remove_uids:
            del uids_data[uid]

        time.sleep(10)

threading.Thread(target=auto_expire, daemon=True).start()

# =========================================
# WEBSITE HTML
# =========================================

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AXD VIP ACCESS</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{

    height:100vh;

    display:flex;

    justify-content:center;

    align-items:center;

    overflow:hidden;

    background:
    radial-gradient(circle at top left,#ff0000,#1a0000 35%),
    radial-gradient(circle at bottom right,#ffcc00,#220000 40%),
    linear-gradient(135deg,#240000,#120000,#330000);

    animation:bgmove 8s infinite alternate;
}

@keyframes bgmove{

    0%{
        background-position:left top,right bottom;
    }

    100%{
        background-position:right top,left bottom;
    }
}

.container{

    width:450px;

    background:rgba(10,10,10,0.92);

    border-radius:30px;

    padding:35px;

    text-align:center;

    border:1px solid rgba(255,255,255,0.08);

    backdrop-filter:blur(12px);

    box-shadow:
    0 0 25px rgba(255,0,0,0.25),
    0 0 60px rgba(255,200,0,0.15);
}

h1{

    color:white;

    font-size:42px;

    margin-bottom:10px;

    letter-spacing:2px;

    text-shadow:
    0 0 12px rgba(255,0,0,0.7),
    0 0 25px rgba(255,200,0,0.4);
}

.subtitle{

    color:#d4d4d4;

    margin-bottom:35px;

    font-size:15px;
}

.label{

    color:#ffffff;

    text-align:left;

    margin-bottom:10px;

    font-weight:bold;
}

.input-box{

    display:flex;

    align-items:center;

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:15px;

    padding:14px;

    margin-bottom:25px;

    transition:0.3s;
}

.input-box:hover{

    border:1px solid rgba(255,0,0,0.5);

    box-shadow:
    0 0 20px rgba(255,0,0,0.3);
}

.input-box input{

    width:100%;

    background:transparent;

    border:none;

    outline:none;

    color:white;

    font-size:16px;
}

.input-box input::placeholder{
    color:#888;
}

.btn{

    width:100%;

    padding:16px;

    border:none;

    border-radius:18px;

    background:
    linear-gradient(90deg,#ff0000,#ff9900,#ff0000);

    background-size:300% 300%;

    color:white;

    font-size:22px;

    font-weight:bold;

    cursor:pointer;

    transition:0.3s;

    animation:gradientmove 4s infinite;
}

@keyframes gradientmove{

    0%{
        background-position:0% 50%;
    }

    50%{
        background-position:100% 50%;
    }

    100%{
        background-position:0% 50%;
    }
}

.btn:hover{

    transform:scale(1.03);

    box-shadow:
    0 0 20px rgba(255,0,0,0.5),
    0 0 40px rgba(255,200,0,0.3);
}

.powered{

    margin-top:20px;

    font-size:22px;

    font-weight:bold;

    color:#ffcc00;

    letter-spacing:4px;

    text-shadow:
    0 0 10px rgba(255,200,0,0.7);
}

.status-box{

    margin-top:20px;

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);

    padding:15px;

    border-radius:15px;

    color:white;

    font-size:18px;
}

.error-box{

    margin-top:20px;

    background:rgba(255,0,0,0.12);

    border:1px solid rgba(255,0,0,0.25);

    padding:15px;

    border-radius:15px;

    color:#ff6666;
}

</style>

</head>

<body>

<div class="container">

<h1>AXD VIP</h1>

<div class="subtitle">
Enter your UID to activate VIP Access
</div>

<form method="POST">

<div class="label">UID NUMBER</div>

<div class="input-box">
<input type="text" name="uid" placeholder="Enter your UID">
</div>

<button class="btn" type="submit">
CLAIM ACCESS
</button>

</form>

<div class="powered">
POWERED BY AXB
</div>

{% if success %}

<div class="status-box">

✅ UID <strong>{{uid}}</strong> Activated Successfully

</div>

{% endif %}

{% if error %}

<div class="error-box">

❌ THIS UID HAS ALREADY BEEN USED

</div>

{% endif %}

</div>

</body>
</html>

"""

# =========================================
# MAIN ROUTE
# =========================================

@app.route("/", methods=["GET", "POST"])

def home():

    success = False
    error = False
    uid = None

    if request.method == "POST":

        uid = request.form.get("uid")

        if uid:

            if uid in uids_data:

                error = True

            else:

                success = True

                expire_time = datetime.now() + timedelta(days=1)

                uids_data[uid] = expire_time

                expire_date = expire_time.strftime("%d-%m-%Y %H:%M:%S")

                # =========================================
                # DISCORD VIP EMBED
                # =========================================

                data = {
                    "username": "AXD VIP SYSTEM",

                    "avatar_url": DISCORD_IMAGE_URL,

                    "embeds": [
                        {

                            "title": "🔥 VIP ACCESS ",

                            "description":
                            f"✨ VIP access activated successfully.\n\n"
                            f"👑 Premium access granted for UID `{uid}`.",

                            "color": 16753920,

                            "thumbnail": {
                                "url": DISCORD_IMAGE_URL
                            },

                            "image": {
                                "url": DISCORD_IMAGE_URL
                            },

                            "fields": [

                                {
                                    "name": "👤 USER UID",
                                    "value": f"`{uid}`",
                                    "inline": True
                                },

                                {
                                    "name": "⚡ ACCESS",
                                    "value": "VIP PREMIUM",
                                    "inline": True
                                },

                                {
                                    "name": "🟢 STATUS",
                                    "value": "ACTIVE",
                                    "inline": True
                                },

                                {
                                    "name": "📅 VALIDITY",
                                    "value": "1 DAY ACCESS",
                                    "inline": True
                                },

                                {
                                    "name": "⏰ EXPIRES ON",
                                    "value": expire_date,
                                    "inline": False
                                }

                            ],

                            "author": {
                                "name": "AXB  BYPASS  SYSTEM",
                                "icon_url": DISCORD_IMAGE_URL
                            },

                            "footer": {
                                "text": "POWERED BY AXB • PREMIUM ACCESS"
                            }

                        }
                    ]
                }

                try:
                    requests.post(WEBHOOK_URL, json=data)
                except:
                    pass

    return render_template_string(
        HTML,
        success=success,
        error=error,
        uid=uid
    )

# =========================================
# RUN SERVER
# =========================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)