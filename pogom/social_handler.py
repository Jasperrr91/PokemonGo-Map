import paho.mqtt.client as mqtt
import json
from pogom.utils import get_args

args = get_args()

def emitPokemon(data):
    if args.mosquitto:
        client = mqtt.Client()
        # client.on_connect = on_connect
        # client.on_message = on_message

        client.connect("test.mosca.io", 1883, 60)
        client.subscribe("pgomapcatch/#", 0)
        client.subscribe("pgomapgeo/#", 0)

        client.publish(('pgomapcatch/all/catchable/' + str(data['pokemon_id'])),
                       str(data['latitude']) + "," + str(data['longitude']) + "," + str(
                           data['encounter_id']) + "," + str(data['pokemon_id']) + "," + str(
                           data['expiration_timestamp_ms']) + "," + str(data['pokemon_name']))
        json_data = json.dumps(data)
        print json_data
        client.publish("pgo/all/catchable/" + str(data['pokemon_id']), json_data)