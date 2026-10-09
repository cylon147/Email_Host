import sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "https://YOUR-HOST/img"
OUT = sys.argv[2] if len(sys.argv) > 2 else "homekit_email_v4.html"
FIRST = sys.argv[3] if len(sys.argv) > 3 else "{{first_name|there}}"
UNSUB = sys.argv[4] if len(sys.argv) > 4 else "{{unsubscribe_url}}"
HOUSE3D = "https://claude.ai/artifact/DzG6K8xxprQvTwKup2ZLnB"
CTA = "https://drivercentral.io/platforms/control4-drivers/homekit/?utm_source=email&amp;utm_medium=svm_buyers&amp;utm_campaign=homekit_launch_v4"
SHOW = "https://drivercentral.io/trial-and-showroom?utm_source=email&amp;utm_medium=svm_buyers&amp;utm_campaign=homekit_launch_v4"

BG = "#0e1530"
def img(name, w, alt, extra=""):
    return f'<img src="{BASE}/{name}" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;{extra}">'

def scene(time, quote, body, name, alt):
    # inline-block card: two per row on desktop, stacked on phones, no media query needed
    return f'''<!--[if mso]><td width="268" valign="top"><![endif]--><div style="display:inline-block;width:100%;max-width:268px;vertical-align:top;margin:0 0 6px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:0 6px 14px 6px;">{img(name,256,alt,"border-radius:10px;")}<div style="font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#a9b4d0;padding:10px 0 2px 0;">{time}</div><div style="font-size:15px;line-height:1.5;color:#e9edf7;"><strong style="color:#ffffff;">{quote}</strong> {body}</div></td></tr></table></div><!--[if mso]></td><![endif]-->'''

def stat(big, small):
    return f'<td width="33%" align="center" valign="top" bgcolor="{BG}" style="padding:18px 4px;"><div style="font-size:38px;font-weight:bold;color:#ffb454;line-height:1;">{big}</div><div style="font-size:13px;color:#c3cce2;padding-top:6px;line-height:1.4;">{small}</div></td>'

def step(n, title, body):
    return f'<!--[if mso]><td width="176" valign="top"><![endif]--><div style="display:inline-block;width:100%;max-width:176px;vertical-align:top;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:0 8px 14px 6px;"><div style="font-size:26px;font-weight:bold;color:#ffb454;line-height:1;">{n}</div><div style="font-size:14px;line-height:1.5;color:#ffffff;padding-top:6px;"><strong>{title}</strong><br><span style="color:#c3cce2;">{body}</span></div></td></tr></table></div><!--[if mso]></td><![endif]-->'

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><meta name="supported-color-schemes" content="dark"><title>HomeKit Bridge for Control4</title></head>
<body bgcolor="#070b18" style="margin:0;padding:0;background-color:#070b18;font-family:Arial,Helvetica,sans-serif;color:#e9edf7;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;mso-hide:all;">Watch the house wake up. Your clients' Control4, inside the Apple Home app.</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#070b18" style="background-color:#070b18;"><tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="width:100%;max-width:600px;background-color:{BG};border-radius:16px;">

<tr><td bgcolor="{BG}" style="padding:20px 24px 12px 24px;font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:#a9b4d0;border-radius:16px 16px 0 0;">DTI Automation &nbsp;&middot;&nbsp; HomeKit Bridge for Control4</td></tr>

<tr><td bgcolor="{BG}" style="padding:0;"><a href="{HOUSE3D}" style="text-decoration:none;display:block;">{img("house_demo.gif",600,"A 3D cutaway of a Control4 smart home waking up: lamps on, TV playing, garage opening, car coming home.")}</a></td></tr>
<tr><td align="center" bgcolor="{BG}" style="padding:12px 24px 0 24px;font-size:14px;"><a href="{HOUSE3D}" style="color:#ffb454;text-decoration:none;font-weight:bold;">Open the 3D house and tap the lights yourself &rarr;</a></td></tr>

<tr><td bgcolor="{BG}" style="padding:22px 24px 6px 24px;"><div style="font-size:30px;line-height:1.12;font-weight:bold;color:#ffffff;letter-spacing:-0.5px;">Your clients already open Apple Home every day.<br><span style="color:#ffb454;">Now their Control4 is in it.</span></div></td></tr>

<tr><td bgcolor="{BG}" style="padding:10px 24px 8px 24px;font-size:16px;line-height:1.65;color:#d3dbee;">Hi {FIRST},<br><br>You bought our Siri Voice Module, so you already sell voice. <strong style="color:#ffffff;">HomeKit Bridge</strong> is the next step: it publishes the Control4 project itself into the Home app. Lights, locks, thermostats, shades, garage doors, sensors, the alarm, even rooms as Apple TVs. Tiles for the family, Siri for everyone, and your programming underneath, untouched.</td></tr>

<tr><td bgcolor="{BG}" style="padding:20px 24px 4px 24px;"><div style="font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:#ffb454;padding-bottom:6px;">One client. One day. Four sentences.</div><div style="font-size:21px;font-weight:bold;color:#ffffff;line-height:1.25;">Control4 does the work. Siri takes the credit.</div></td></tr>

<tr><td bgcolor="{BG}" align="center" style="padding:12px 12px 0 12px;font-size:0;">
<!--[if mso]><table role="presentation" cellpadding="0" cellspacing="0"><tr><![endif]-->
{scene("06:45","&ldquo;Good morning.&rdquo;","Shade up, pendant on, fan on, thermostat to 23&deg;. Four Control4 devices, one Home scene.","house_morning.jpg","Morning scene: pendant on, shade up, fan spinning.")}
{scene("18:20","&ldquo;I&rsquo;m home.&rdquo;","Garage up, front door unlocked, both lamps on. Said from the car, in CarPlay.","house_home.jpg","Evening scene: garage open, car inside, lamps on.")}
<!--[if mso]></tr><tr><![endif]-->
{scene("20:30","&ldquo;Movie time.&rdquo;","Lights off, shade down, the living room shows up as an Apple TV with input selection and remote control.","house_movie.jpg","Movie scene: lights down, TV glowing.")}
{scene("23:00","&ldquo;Good night.&rdquo;","Everything off, door locked, alarm armed, thermostat to 19&deg;. The security tile shows one partition, armed.","house_night.jpg","Night scene: everything off, door locked, alarm armed.")}
<!--[if mso]></tr></table><![endif]-->
</td></tr>

<tr><td bgcolor="{BG}" style="padding:10px 24px 0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#141d3d" style="background-color:#141d3d;border-radius:14px;"><tr><td style="padding:0;border-radius:14px 14px 0 0;">{img("house_controller.jpg",552,"Close-up of the Control4 controller on the wall, status light glowing blue.","border-radius:14px 14px 0 0;")}</td></tr><tr><td bgcolor="#141d3d" style="padding:18px 20px 20px 20px;border-radius:0 0 14px 14px;"><div style="font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:#8fb0ff;padding-bottom:6px;">Where the bridge lives</div><div style="font-size:19px;font-weight:bold;color:#ffffff;line-height:1.3;padding-bottom:8px;">This is the entire install.</div><div style="font-size:14px;line-height:1.55;color:#d3dbee;">The driver runs on the controller. No hub, no Raspberry Pi, no server, no second box on the rack. Pairings, the setup code and every published device survive reboots and updates.</div></td></tr></table></td></tr>

<tr><td bgcolor="{BG}" style="padding:24px 24px 0 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #2a3a6e;border-bottom:1px solid #2a3a6e;"><tr>{stat("0","extra boxes<br>to buy")}{stat("30","days free<br>on a real project")}{stat("Free","Showroom licence<br>for your demo room")}</tr></table></td></tr>

<tr><td align="center" bgcolor="{BG}" style="padding:26px 24px 6px 24px;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="#ffb454" style="background-color:#ffb454;border-radius:999px;"><a href="{CTA}" style="display:inline-block;padding:16px 34px;font-size:17px;font-weight:bold;color:#2a1700;text-decoration:none;">Start the 30-day free trial</a></td></tr></table></td></tr>
<tr><td align="center" bgcolor="{BG}" style="padding:8px 24px 8px 24px;font-size:13px;line-height:1.7;color:#a9b4d0;">Showroom? <a href="{SHOW}" style="color:#ffb454;">Claim the free Showroom licence</a><br>Want to play first? <a href="{HOUSE3D}" style="color:#ffb454;">Open the interactive 3D house</a></td></tr>

<tr><td bgcolor="{BG}" align="center" style="padding:14px 18px 0 18px;font-size:0;">
<!--[if mso]><table role="presentation" cellpadding="0" cellspacing="0"><tr><![endif]-->
{step("1","Add the driver","Download from DriverCentral, drop it into the project.")}
{step("2","Pick a licence","DriverCentral (needs the Cloud driver) or a DTI activation key (needs internet on the controller).")}
{step("3","Publish and scan","Choose the devices, scan the setup code in the Home app. Done.")}
<!--[if mso]></tr></table><![endif]-->
</td></tr>
<tr><td bgcolor="{BG}" style="padding:0 24px;font-size:12px;line-height:1.6;color:#a9b4d0;">Needs Control4 OS 4.0 or later and an iPhone or iPad on the same network as the controller. Home app automations need an Apple TV or HomePod as the home hub.</td></tr>

<tr><td bgcolor="{BG}" style="padding:22px 24px 26px 24px;font-size:15px;line-height:1.65;color:#d3dbee;">If it does not do something your project needs, reply and tell me. It comes straight to me and that is how the feature list got this long.<br><br><strong style="color:#ffffff;">Prakash Rola</strong><br>DTI Automation Pvt. Ltd.</td></tr>

<tr><td bgcolor="#0a1024" style="background-color:#0a1024;border-radius:0 0 16px 16px;padding:18px 24px 24px 24px;font-size:11px;line-height:1.6;color:#8d99b8;">You are receiving this because you bought the Siri Voice Module from DTI Automation on DriverCentral.<br>DTI Automation Pvt. Ltd., 201 Goldcroft, Opp. Only Paratha's, Jetalpur Rd., Vadodara, India.<br><a href="{UNSUB}" style="color:#c3cce2;">Unsubscribe</a><br><br>Apple, HomeKit, the Home app, Siri, Apple TV, HomePod and CarPlay are trademarks of Apple Inc. This driver is not made by, endorsed by or affiliated with Apple. The house is an illustration. MSRP $250 after the trial; DriverCentral lists a 30-day return period.</td></tr>

</table></td></tr></table></body></html>'''
open(OUT, "w").write(html)
print(OUT, len(html))
