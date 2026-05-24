from flask import Flask, request, render_template_string
from datetime import datetime, timedelta
import requests
import threading
import time

app = Flask(__name__)

# =========================================
# WEBSITE SYSTEM CONTROL
# =========================================

SYSTEM_ACTIVE = True 

# =========================================
# VIP DAYS
# CHANGE DAYS HERE
# =========================================

VIP_DAYS = 1

# =========================================
# DISCORD SETTINGS
# =========================================

WEBHOOK_URL = "https://discord.com/api/webhooks/1504755222306750496/mYvZ5FMo6K3THbhyCgUt9sbkVVkizZZZ36cd2RJ70BIlAzQur0Q9s7tufGU_61UlL2jb"

DISCORD_IMAGE_URL = "https://res.cloudinary.com/dui2c44p6/image/upload/v1779002265/auclo2ketmqxwldt89tx.png"

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
                    "username": "AXB VIP SYSTEM",

                    "avatar_url": DISCORD_IMAGE_URL,

                    "embeds": [
                        {
                            "title": "❌ VIP ACCESS EXPIRED",

                            "description":
                            "Premium access expired automatically.",

                            "color": 16711680,

                            "thumbnail": {
                                "url": DISCORD_IMAGE_URL
                            },

                            "fields": [

                                {
                                    "name": "🆔 UID",
                                    "value": f"`{uid}`",
                                    "inline": True
                                },

                                {
                                    "name": "📌 STATUS",
                                    "value": "EXPIRED",
                                    "inline": True
                                },

                                {
                                    "name": "🔒 ACCESS",
                                    "value": "LOCKED",
                                    "inline": True
                                }

                            ],

                            "footer": {
                                "text": "AXB PREMIUM SECURITY"
                            }

                        }
                    ]
                }

                try:
                    requests.post(WEBHOOK_URL, json=data)

                except Exception as e:
                    print("WEBHOOK ERROR:", e)

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

<title>AXB Premium</title>

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

    background:
    linear-gradient(135deg,#0a0a0f,#14141d,#1b1b24);
}

.container{

    width:470px;

    background:#111111;

    border-radius:28px;

    padding:35px;

    text-align:center;

    border:2px solid #a855f7;

    box-shadow:
    0 0 25px rgba(168,85,247,0.35);
}

h1{

    color:#c084fc;

    font-size:48px;

    margin-bottom:5px;

    font-weight:bold;
}

.premium{

    color:white;

    font-size:22px;

    margin-bottom:18px;

    font-weight:600;
}

.subtitle{

    color:#cfcfcf;

    margin-bottom:30px;

    font-size:14px;

    line-height:24px;
}

.label{

    color:white;

    text-align:left;

    margin-bottom:10px;

    font-size:14px;

    font-weight:bold;
}

.input-box{

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.1);

    border-radius:14px;

    padding:15px;

    margin-bottom:25px;
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

    color:#999;
}

.btn{

    width:100%;

    padding:16px;

    border:none;

    border-radius:15px;

    background:
    linear-gradient(90deg,#7b2ff7,#ffffff,#7b2ff7);

    color:#111;

    font-size:20px;

    font-weight:bold;

    cursor:pointer;
}

.btn:hover{

    opacity:0.95;
}

.lock-box{

    margin-top:20px;

    background:
    linear-gradient(145deg,#1a0000,#2a0000);

    border:1px solid rgba(255,0,0,0.25);

    padding:25px;

    border-radius:18px;

    color:white;

    box-shadow:
    0 0 20px rgba(255,0,0,0.15);
}

.lock-title{

    font-size:24px;

    color:#ff4d4d;

    font-weight:bold;

    margin-bottom:10px;
}

.lock-sub{

    color:#ffb3b3;

    font-size:15px;

    line-height:24px;
}

.powered{

    margin-top:18px;

    font-size:12px;

    color:#aaaaaa;

    letter-spacing:2px;
}

.status-box{

    margin-top:20px;

    background:rgba(0,255,0,0.08);

    border:1px solid rgba(0,255,0,0.2);

    padding:14px;

    border-radius:12px;

    color:#8cff8c;

    font-size:16px;
}

.error-box{

    margin-top:20px;

    background:rgba(255,0,0,0.08);

    border:1px solid rgba(255,0,0,0.2);

    padding:14px;

    border-radius:12px;

    color:#ff8080;

    font-size:15px;
}

.copy-btn{

    margin-left:8px;

    cursor:pointer;

    color:#c084fc;

    font-size:15px;
}

</style>

</head>

<body>

<div class="container">

<h1>AXB</h1>

<div class="premium">
Premium
</div>

{% if system_active %}

<div class="subtitle">
Enter your UID below<br>
to unlock premium access
</div>

<form method="POST">

<div class="label">
Enter Your UID
</div>

<div class="input-box">
<input type="text" name="uid" placeholder="Enter UID Here">
</div>

<button class="btn" type="submit">
CLAIM ACCESS
</button>

</form>

{% else %}

<div class="lock-box">

<div class="lock-title">
🔒 WEBSITE LOCKED
</div>

<div class="lock-sub">
Premium Access Is Temporarily Disabled
</div>

</div>

{% endif %}

<div class="powered">
Powered By AXB
</div>

{% if success %}

<div class="status-box">

✅ UID
<strong id="uidText">{{uid}}</strong>

<span class="copy-btn" onclick="copyUID()">📋</span>

Activated Successfully

</div>

{% endif %}

{% if error %}

<div class="error-box">

❌ This UID Has Already Been Used

</div>

{% endif %}

</div>

<script>

function copyUID(){

    const uid = document.getElementById("uidText").innerText;

    navigator.clipboard.writeText(uid);

    alert("UID Copied");
}

</script>

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

    if request.method == "POST" and SYSTEM_ACTIVE:

        uid = request.form.get("uid")

        if uid:

            if uid in uids_data:

                error = True

            else:

                success = True

                expire_time = datetime.now() + timedelta(days=VIP_DAYS)

                uids_data[uid] = expire_time

                expire_date = expire_time.strftime("%d-%m-%Y %H:%M:%S")

                # =========================================
                # DISCORD WEBHOOK
                # =========================================

                data = {
                    "username": "AXB VIP SYSTEM",

                    "avatar_url": DISCORD_IMAGE_URL,

                    "embeds": [
                        {

                            "title": "💎 VIP ACCESS ACTIVATED",

                            "description":
                            "A new premium user has been activated successfully.",

                            "color": 10494192,

                            "thumbnail": {
                                "url": DISCORD_IMAGE_URL
                            },

                            "fields": [

                                {
                                    "name": "🆔 UID",
                                    "value": f"`{uid}`",
                                    "inline": True
                                },

                                {
                                    "name": "🟢 STATUS",
                                    "value": "ACTIVE",
                                    "inline": True
                                },

                                {
                                    "name": "👑 ACCESS",
                                    "value": "PREMIUM VIP",
                                    "inline": True
                                },

                                {
                                    "name": "📅 ACTIVE DAYS",
                                    "value": f"{VIP_DAYS} DAYS",
                                    "inline": True
                                },

                                {
                                    "name": "⏰ EXPIRES ON",
                                    "value": expire_date,
                                    "inline": False
                                }

                            ],

                            "footer": {
                                "text": "AXB PREMIUM SECURITY"
                            }

                        }
                    ]
                }

                try:

                    requests.post(
                        WEBHOOK_URL,
                        json=data
                    )

                except Exception as e:

                    print("DISCORD ERROR:", e)

    return render_template_string(
        HTML,
        success=success,
        error=error,
        uid=uid,
        system_active=SYSTEM_ACTIVE
    )

# =========================================
# RUN SERVER
# =========================================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5059)
