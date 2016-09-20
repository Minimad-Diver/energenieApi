from flask_restful import Resource
import RPi.GPIO as GPIO
import time

class Socket(Resource):

    def get(self, socketNumber, socketState):

        try:

            # Set the pins numbering mode
            GPIO.setmode(GPIO.BOARD)
            # Select the GPIO pins used for the encoder K0-K3 data inputs
            GPIO.setup(11, GPIO.OUT)
            GPIO.setup(15, GPIO.OUT)
            GPIO.setup(16, GPIO.OUT)
            GPIO.setup(13, GPIO.OUT)
            # Select the signal used to select ASK/FSK
            GPIO.setup(18, GPIO.OUT)
            # Select the signal used to enable/disable the modulator
            GPIO.setup(22, GPIO.OUT)
            # Disable the modulator by setting CE pin lo
            GPIO.output (22, False)
            # Set the modulator to ASK for On Off Keying
            # by setting MODSEL pin lo
            GPIO.output (18, False)
            # Initialise K0-K3 inputs of the encoder to 0000
            GPIO.output (11, False)
            GPIO.output (15, False)
            GPIO.output (16, False)
            GPIO.output (13, False)
            # K0-K3 states for all sockets
            sockets = {
                'all' : {
                    'on': [True, False, True, True],
                    'off': [False, False, True, True]
                },
                '1' : {
                    'on': [True, True, True, True],
                    'off': [False, True, True, True]
                },
                '2' : {
                    'on': [True, True, True, False],
                    'off': [False, True, True, False]
                },
                '3' : {
                    'on': [True, True, False, True],
                    'off': [False, True, False, True]
                },
                '4' : {
                    'on': [True, True, False, False],
                    'off': [False, True, False, False]
                }
            }
            # Set K0-K3
            GPIO.output (13, sockets[socketNumber][socketState][0])
            GPIO.output (16, sockets[socketNumber][socketState][1])
            GPIO.output (15, sockets[socketNumber][socketState][2])
            GPIO.output (11, sockets[socketNumber][socketState][3])
            # Let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # Keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)
            # Return True
            GPIO.cleanup()
            return { 'socket': socketNumber, 'state': socketState }

        except:

            # Return False
            return { 'socket': socketNumber, 'state': 'error' }
