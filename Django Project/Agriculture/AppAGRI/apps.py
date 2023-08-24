from django.apps import AppConfig

import os
import asyncio
from mqttasgi.server import Server
from mqttasgi.utils import get_application
import logging
from threading import Thread
from dotenv import load_dotenv, find_dotenv
import AppAGRI.jobSchedule.jobs as jobsch

load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)

def mqtt_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    if os.environ.get('RUN_MAIN'):
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
        mqtt_app = os.environ.get("MQTT_APPLICATION", None)
        
        logging.basicConfig(
            level={
                0: logging.WARN,
                1: logging.INFO,
                2: logging.DEBUG,
            }.get(verbosity, logging.DEBUG),
            format="%(asctime)-15s %(levelname)-8s %(message)s",
        )
        
        if mqtt_app == None :
            logger.debug(f'[mqttasgi][start][failed] - MQTT_APPLICATION not specify in project environement')
            return
        
        mqtt_app = get_application(mqtt_app)
        server = Server(
            mqtt_app,
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
    


class AppagriConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppAGRI'
    def ready(self) -> None:
        t = Thread(target=mqtt_thread)
        t.daemon = True  # Dies when main thread (only non-daemon thread) exits.
        t.start()
        
        jobsch.start()
        pass
