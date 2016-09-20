# energenieApi
energenieApi is simple app written in Python (Flask-RESTful) that allows
controlling Energenie sockets using Pi-mote control board connected to Raspberry Pi
## Installation
**You will need to run this app as root as it's the easiest way to access GPIO**
```
git clone ...
virtual env energenieApi
cd energenieApi
pip install -i requirements.txt
python app.py
```
## Usage
Make a GET request via curl:
``
curl http://127.0.0.1/socket/all/on
``
the app will respond with JSON, for example:
```JSON
{
    "socket": "all",
    "state": "on"
}
```
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
## History

## Credits
Socket class is based on the sample code provided on the [Energenie website](https://energenie4u.co.uk/catalogue/download_software/ENER002-2PI.py)
## License
Free for all, don't know what licanse suits this but as far as I'm concerned it's Open Source