import os.path
import json
import os

if os.path.isfile('./conf/conf.json') is False:
    with open('./conf/conf.json', 'w') as newconf:
        conf = {}
        conf['dbpassword']  = os.environ['DB_PASSWORD']
        conf['log']  = os.environ['LOG_LVL']
        json.dump(conf, newconf, indent=4)

with open('./conf/conf.json', 'r') as mainconf:
    conf = json.load(mainconf)

#salt = conf['salt']  이거 만들어줘야함 conf.json에서