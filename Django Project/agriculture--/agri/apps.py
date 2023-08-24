from django.apps import AppConfig
import os
from threading import Thread
import asyncio
from mqttasgi.server import Server
from mqttasgi.utils import get_application
import logging
from dotenv import load_dotenv, find_dotenv

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())

def mqtt_thread():
    host = os.environ.get("MQTT_HOSTNAME", "localhost")
    port = int(os.environ.get("MQTT_PORT", 1883))
    username = os.environ.get("MQTT_USERNAME", None)
    password = os.environ.get("MQTT_PASSWORD", None)
    client_id = os.environ.get("MQTT_CLIENT_ID", None)
    verbosity = int(os.environ.get("VERBOSITY", 2))
    cleansession = os.environ.get("MQTT_CLEAN", "True").lower() == "true"
    cert = os.environ.get("TLS_CERT", None)
    key = os.environ.get("TLS_KEY", None)
    cacert = os.environ.get("TLS_CA", None)
    mqtt_app = os.environ.get('MQTTASGI_APP')

    if(mqtt_app == None):
        return
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    logging.basicConfig(
        level={
            0: logging.WARN,
            1: logging.INFO,
            2: logging.DEBUG,
        }.get(verbosity, logging.DEBUG),
        format="%(asctime)-15s %(levelname)-8s %(message)s",
    )

    # mqtt_app = ProtocolTypeRouter({
    #     'mqtt' : MyMqttConsumer.as_asgi()
    # })

    server = Server(
        get_application(mqtt_app),
        host,
        port,
        username,
        password,
        client_id,
        logger=logger,
        clean_session=cleansession,
        cert=cert,
        key=key,
        ca_cert=cacert,
    )

    server.run()


class AgriConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agri'
    def ready(self) -> None:
        if os.environ.get("RUN_MAIN") :
            thread = Thread(target=mqtt_thread)
            thread.daemon = True
            thread.start()
        # pass

